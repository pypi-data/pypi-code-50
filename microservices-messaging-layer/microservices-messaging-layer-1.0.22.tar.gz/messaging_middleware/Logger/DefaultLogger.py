import logging
import os
from messaging_middleware.confluent_producer.AVROProducer import AVROPRODUCER


class Logger:
    def __init__(self, **kwargs):
        init_kafka = kwargs.get('init_kafka', 0)
        self.avro_producer = None
        if init_kafka:
            self.avro_producer = self.__init_avro_producer(**kwargs)
        self.__init_logging_and_setup_levels()

    def __init_avro_producer(self, **kwargs):
        """
        this inits an Confluent Kafka AVRO producer
        :param kwargs:
        :return:
        """
        avro_producer = AVROPRODUCER(brokers_uri=kwargs.get('brokers_uri'),
                                     schema_registry_url=kwargs.get('schema_registry_url'),
                                     topic=kwargs.get('monitoring_topic', 'tcservicesmonitor'),
                                     security_protocol=kwargs.get('security_protocol', 'plaintext'),
                                     sasl_mechanisms=kwargs.get('sasl_mechanisms', None),
                                     sasl_username=kwargs.get('sasl_username', None),
                                     sasl_password=kwargs.get('sasl_password', None),
                                     basic_auth_credentials_source=kwargs.get(
                                         'schema_registry_basic_auth_credentials_source',
                                         None),
                                     basic_auth_user_info=kwargs.get('schema_registry_basic_auth_user_info',
                                                                     None)

                                     )
        return avro_producer

    def __init_logging_and_setup_levels(self):
        """
        This inits and configures the logging and eventually assign it to self.logger
        :return:
        """
        logger = logging.getLogger()
        try:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
            handler.setFormatter(formatter)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            self.logger = logger
            logger.debug('--=Logger ready my Lord=--')

            logging.getLogger('urllib3').setLevel(logging.ERROR)
            logging.getLogger('requests').setLevel(logging.ERROR)
            return 1
        except Exception as error:
            logger.error('Error setting logging:', error)
            return 0

    def print_log(self, level=None, *args):
        """
        This prints out a log message
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

    def produce_msg(self, message_to_produce, schema_key):
        """
        This first prints out a log message and then produce the message_to_produce to Kafka
        :param level:
        :param args:
        :param message_to_produce:
        :param schema_key:
        :return:
        """
        if self.avro_producer:
            self.avro_producer.produce_message(value=message_to_produce, key=schema_key)
        else:
            raise Exception("Init Avro Producer first!")