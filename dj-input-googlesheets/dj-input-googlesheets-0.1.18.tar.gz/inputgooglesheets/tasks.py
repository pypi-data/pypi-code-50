from __future__ import absolute_import, unicode_literals
import logging
import functools
from celery import shared_task
from django.conf import settings
from django.utils.module_loading import import_string


logger = logging.getLogger(__name__)


LOCK_KEY = '744ed748-7685-41ca-a714-f0bfb6db0b80:{}'


def get_lock(key):
    "Returns a lock object configured with the key that must be locked."
    lock_key = LOCK_KEY.format(key)
    lock_creator = import_string(settings.DISTRIBUTED_LOCK_CREATOR)
    return lock_creator(lock_key)


def get_spreadsheet_and_lock(pk):
    """Returns a spreadsheet and a lock configured with the key of the
    spreadsheet. If the spreadshed is disabled or does not exist, writes
    a warn log informing it and returns a tuple of two `None` values.

    Parameters
    ----------
    pk: int
        The pk value of the spreadsheet to return.

    Returns
    -------
    spreadsheet: inputgooglesheets.models.Spreadsheet
        Spreadsheet.
    lock: any
        A lock object configured for the speadsheet pk.
    """
    from .models import Spreadsheet
    try:
        result = Spreadsheet.objects.get(pk=pk)
        if not result.enabled:
            logger.warn("The spreadsheet '{}' is disabled.".format(pk))
            return None, None
        return result, get_lock(pk)
    except Spreadsheet.DoesNotExist:
        logger.warn("Spreadsheet '{}' does not exist.".format(pk))
        return None, None


def with_spreadsheet_and_lock(fn):
    def spreadsheet_and_lock(pk):
        spreadsheet, lock = get_spreadsheet_and_lock(pk)
        if lock and lock.acquire(blocking=False):
            try:
                return fn(spreadsheet)
            finally:
                lock.release()
        else:
            logger.warn("Already importing spreadsheet '{}'. Omiting import.".format(pk))
    return functools.update_wrapper(spreadsheet_and_lock, fn)


@shared_task
@with_spreadsheet_and_lock
def start_import(spreadsheet):
    from .utils import Utils
    count = Utils.start_import(spreadsheet)
    logger.info("Imported spreadsheet '{}'. {} rows imported".format(spreadsheet.pk, count))


@shared_task
@with_spreadsheet_and_lock
def continue_import(spreadsheet):
    from .utils import Utils
    count = Utils.continue_import(spreadsheet)
    logger.info("Finished importing spreadsheet '{}': {} rows imported".format(spreadsheet.pk, count))


@shared_task
def import_all_google_spreadsheets():
    from .models import Spreadsheet
    lock = get_lock('')
    if lock.acquire(blocking=False):
        try:
            for spreadsheet in Spreadsheet.objects.filter(enabled=True, automatically_imported=True):
                continue_import.delay(spreadsheet.pk)
        finally:
            lock.release()
