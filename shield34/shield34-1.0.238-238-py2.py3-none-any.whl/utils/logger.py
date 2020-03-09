import logging

class Shield34Logger():

    logger = logging.getLogger('shield34')
    @staticmethod
    def set_logger(logger):
        Shield34Logger.logger = logger
