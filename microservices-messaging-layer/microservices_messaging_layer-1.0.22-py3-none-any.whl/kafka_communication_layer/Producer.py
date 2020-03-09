import json
import logging
import sys

from kafka import KafkaProducer


def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d]\n' % \
                         (msg.topic(), msg.partition()))


class Producer:

    def __init__(self, *args, **kwargs):
        self.__servers = kwargs.get('servers', None)
        self.topic = kwargs.get('topic', None)
        self.security_protocol = kwargs.get('security_protocol','')
        self.ssl_ca_location = kwargs.get('ssl_ca_location','./configuration/cacert.pem')

        if self.security_protocol == 'ssl':
            security_protocol = 'SSL'
            ssl_check_hostname = True
        else:
            security_protocol = ''
            ssl_check_hostname = ''
        if not self.topic:
            sys.stderr.write('%% Topic name not specified: \n')
            raise ValueError("Topic name not specified")
        logging.basicConfig(
            format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
            level=logging.ERROR
        )
        logging.getLogger('kafka').setLevel(logging.INFO)
        self.producer = KafkaProducer(bootstrap_servers=self.__servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      security_protocol=security_protocol,
                                      ssl_check_hostname=ssl_check_hostname,
                                      ssl_cafile= self.ssl_ca_location

        )

    async def produce_message(self, **kwargs):
        message = kwargs.get('message', None)
        if message is not None:

            try:
                self.producer.send(self.topic, message)

            except BufferError as e:
                sys.stderr.write('%% Local producer queue is full ' \
                                 '(%d messages awaiting delivery): try again\n' %
                                 len(self.producer))
                return None
            self.producer.flush()
            return {"topic": self.topic, "sent": True}
        else:
            print("[produce_message]Message is empty")

    async def produce_message(self, **kwargs):
        message = kwargs.get('message', None)
        for value in message:
            try:
                self.producer.send(self.topic, value)

            except BufferError as e:
                sys.stderr.write('%% Local producer queue is full ' \
                                 '(messages awaiting delivery): try again\n')
        self.producer.flush()
        return {"topic": self.topic, "sent": True}
