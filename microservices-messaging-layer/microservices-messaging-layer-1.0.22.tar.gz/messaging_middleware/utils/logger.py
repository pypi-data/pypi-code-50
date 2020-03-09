import logging
import sys, os

from messaging_middleware.avro_communication_layer.Producer import Producer


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):

        if Logger.__instance is None:
            logger = logging.getLogger()
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            logger.debug('Logger ready, my Lord.')

            Logger.__instance = object.__new__(cls)
            Logger.__instance.logger = logger
            logging.basicConfig(
                format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
                level=logging.INFO
            )
            logging.getLogger('urllib3').setLevel(logging.ERROR)
            logging.getLogger('requests').setLevel(logging.ERROR)
            logger.producer = Logger.__instance._init_logger_producer()

        return Logger.__instance




    def _init_logger_producer(self):
        producer = Producer(bootstrap_servers=os.environ.get('brokers'),
                            schema_registry_url=os.environ.get('schema_registry'),
                            topic=os.environ.get('monitoring_topic', 'tcservicesmonitor'),
                            security_protocol=os.environ.get('security_protocol', 'plaintext'),
                            sasl_mechanisms=os.environ.get('sasl_mechanisms', None),
                            sasl_username=os.environ.get('sasl_username', None),
                            sasl_password=os.environ.get('sasl_password', None),
                            basic_auth_credentials_source=os.environ.get(
                                'schema_registry_basic_auth_credentials_source',
                                None),
                            basic_auth_user_info=os.environ.get('schema_registry_basic_auth_user_info',
                                                                None)

                            )
        return producer

    def logmsg(self, level=None, *args):
        # self.logger.setLevel(logging.WARNING)
        """
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        """
        if level == 'debug':
            return self.logger.debug(args)
        elif level == 'info':
            return self.logger.info(args)
        elif level == 'warn':
            return self.logger.warning(args)
        elif level == 'error':
            return self.logger.error(args)
        elif level == 'critical':
            return self.logger.critical(args)
        else:
            return self.logger.debug(args)

    def produce_msg(self, message):
        try:
            return self.logger.producer.produce_message(value=message['value'], key=message['key'])
        except Exception as error:
            self.logmsg('error','EXCEPTION producing message:',error)
            return 0
    def retry(self, **kwargs):
        pass
