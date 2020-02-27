# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""Custom logger handlers
"""
import os

from dealer.git import git
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging.handlers.transports.background_thread import BackgroundThreadTransport

from arnoldpaperboy.utils.resource import logging_k8s_container, stringify_label


SKIP_LOGRECORD_ATTRS = [
    'args',
    'levelname',
    'levelno',
    'message',
    'msecs',
    'msg',
    'process',
    'processName',
    'relativeCreated',
    'thread',
    'threadName',
]

MAGIC_PREFIX = "ong$eD8eigieg2caiy5kinaN_"


class StackdriverLoggingHandler(CloudLoggingHandler):
    """Log to stackdriver with additional labels.

    Logs to stackdriver with k8s resource related information in the ```resource.labels``` field,
    and other additional information in the root message labels field. To add any key-value pair to
    the log struct's labels field, add it as dictionary to the logger's ```extra``` kwarg.
    Due to the limitations of python logger and google.cloud.logger's implementation of
    stackdriver support, it is not possible to add extra json-structured info to the jsonPayLoad,
    nor to put source related info (file, lineno) to stackdriver's sourceLocation field. Therefore
    everything will be added as a flat k:v list in the ```labels``` field.

    Example:
        logger.info('Starting processing of new scene', extra={'sceneId': 'TheSceneID'})

        this will add a labels.sceneId = 'TheSceneID' to the log struct in stackdriver.
    """

    def __init__(self, *args, tier='', app='', **kwargs):
        """Init

        Args:
            args (tuple): arguments
            tier (str): environment tier
            app (str): app name
            kwargs (dict): keyword arguments
        """
        super(StackdriverLoggingHandler, self).__init__(*args, **kwargs)
        # monkey-patch the cloud logger's grace period for sending pending logs, the default 5s is
        # too short if there are many messages
        self.transport = BackgroundThreadTransport(self.client, self.name, grace_period=30)

        try:
            tag = str(git.tag)
        except TypeError:
            tag = os.environ.get('{}_VERSION'.format(app.upper()), '')

        self.resource = logging_k8s_container()

        if self.labels is None:
            self.labels = {}

        self.labels.update(
            app=app,
            tier=tier,
            tag=tag,
        )

    def emit(self, record):
        """Actually log the specified logger record.

        Args:
            record (logger.LogRecord): The record to be logged.
        """
        message = super(StackdriverLoggingHandler, self).format(record)

        labels = self.labels.copy()

        record_attrs = {
            k.replace(MAGIC_PREFIX, ''): v for k, v in vars(record).items()
            if '{}{}'.format(MAGIC_PREFIX, k) not in vars(record)
        }

        for key, value in record_attrs.items():
            if key not in SKIP_LOGRECORD_ATTRS and value:
                labels[key] = stringify_label(value)

        self.transport.send(
            record, message, resource=self.resource, labels=labels)
