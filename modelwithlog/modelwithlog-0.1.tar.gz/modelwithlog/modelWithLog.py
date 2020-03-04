import logging

from django.db import models
from django.utils.timezone import now


class ModelWithLog(models.Model):
    logger = None

    class Meta:
        abstract = True

    log = models.TextField(null=True, blank=True, default='', verbose_name='Log')

    @staticmethod
    def get_formatted_message(message):
        return '[{0}] {1}\r\n'.format(now().strftime('%Y-%m-%d %H:%M:%S'), message)

    def _log(self, message, level):
        self.logger.log(level, self.get_formatted_message(message))
        self.log += self.get_formatted_message(message)
        self.save()

    def info(self, message):
        self._log(message, level=logging.INFO)

    def debug(self, message):
        self._log(message, level=logging.INFO)

    def warning(self, message):
        self._log(message, level=logging.WARNING)

    def error(self, message):
        self._log(message, level=logging.ERROR)

    def critical(self, message):
        self._log(message, level=logging.CRITICAL)
