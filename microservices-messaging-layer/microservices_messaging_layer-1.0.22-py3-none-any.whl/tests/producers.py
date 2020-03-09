# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 04/03/2020
import os
from messaging_middleware.confluent_producer.ConfluentProducer import ConfluentProducer
from messaging_middleware.confluent_producer.AVROProducer import AVROPRODUCER
from messaging_middleware.Logger.Logger import Logger
from datetime import datetime, timezone

default_key_value = {"service_name": "test"}


class OutboundCommunicationLayer:

    def __init__(self, topic, brokers_uri, security_protocol='plaintext', schema_registry_url=None):

        if schema_registry_url is None:
            self.producer = ConfluentProducer(
                brokers_uri=brokers_uri,
                topic=topic, security_protocol=security_protocol)
        else:
            self.avro_producer = AVROPRODUCER(
                brokers_uri=brokers_uri,
                schema_registry_url=schema_registry_url,
                topic=topic, security_protocol=security_protocol)

    def produce_topic(self, value):
        self.producer.produce_message(message=value)

    def produce_avro_topic(self, value, key=default_key_value):

        self.avro_producer.produce_message(value=value, key=key)




if __name__ == "__main__":
    o = OutboundCommunicationLayer(topic='my-test-2', brokers_uri=os.environ.get('brokers'),
                                   schema_registry_url=os.environ.get('schema_registry_url'))
    o.produce_avro_topic(value={"my_text": "ciaociaociaociao"}, key=default_key_value)

    logger = Logger(init_kafka=1, brokers_uri=os.environ.get('brokers'),
                    schema_registry_url=os.environ.get('schema_registry_url'))
    logger.print_log('info', 'My log ', 10)
    logger.print_log('debug', 'my second log')
    message_to_produce = {
        "service_name": "my-test-microservice",
        "last_operation": "last-completed-operation",
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "operation_result": "SUCCESS",
        "operation_description": "The operation description",
        "error_description": ""
    }


    logger.produce_msg(message_to_produce=message_to_produce, schema_key={
        "service_name": "my-test-service"})
