#-*-coding:utf-8-*-
import logging
import os
from endi.scripts.utils import command



def generate_archives_command(arguments, env):
    """
    Generate archive files based on payment database entries
    """
    logger = logging.getLogger(__name__)
    logger.debug("Generating archive files")
    from zope.sqlalchemy import mark_changed
    from endi_payment.archive import FileArchiveService
    from endi_payment.database import LocalSessionContext
    from endi_payment.models import (
        EndiPaymentHistory,
        EndiPaymentArchiveSeal,
    )
    storage = env['request'].registry.settings[FileArchiveService.settings_key]
    logger.debug("  + Working with directory {}".format(storage))
    os.system('rm -f {}/*.csv'.format(storage))

    with LocalSessionContext() as dbsession:
        seals = dbsession.query(EndiPaymentArchiveSeal).all()
        logger.debug(" Deleting {} seals".format(len(seals)))
        for seal in seals:
            dbsession.delete(seal)

        entries = dbsession.query(EndiPaymentHistory).order_by(
            EndiPaymentHistory.id
        ).all()

        logger.debug(" + {} entries".format(len(entries)))
        for index, entry in enumerate(entries):
            if index > 0:
                entry.previous_entry_hash = entries[index - 1].get_hash()
            else:
                entry.previous_entry_hash = ''
            archive_service = FileArchiveService(
                None, env['request']
            )
            archive_service.filename = "payment_storage_{}_{}.csv".format(
                entry.date.year, entry.date.month
            )
            archive_service.filepath = os.path.join(
                archive_service.storage_path, archive_service.filename
            )
            seal = archive_service.archive(entry)
            dbsession.add(seal)
            dbsession.merge(entry)
        dbsession.commit()
    from endi_base.models.base import DBSESSION
    session = DBSESSION()
    mark_changed(session)


def entry_point():
    """enDI payment archive generation tool
    Usage:
        endi-payment <config_uri> gen_archive
    """
    try:
        return command(generate_archives_command, entry_point.__doc__)
    finally:
        pass
