# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 19/02/2020
# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 2019-07-03
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# =============================================================================
#
# Produce  messages from Confluent Cloud
# Using Confluent Python Client for Apache Kafka
#
# =============================================================================

import json
import logging
import sys
from confluent_kafka import Producer


class ConfluentProducer:

    def __init__(self, *args, **kwargs):
        self.brokers_uri = kwargs.get('brokers_uri', None)
        self.topic = kwargs.get('topic', None)
        self.security_protocol = kwargs.get('security_protocol', 'plaintext')
        self.ssl_ca_location = kwargs.get('ssl_ca_location', './configuration/cacert.pem')

        # -- for CCLOUD --
        # mechanisms = PLAIN for CCLOUD
        self.sasl_mechanisms = kwargs.get('sasl_mechanisms', None)
        self.sasl_username = kwargs.get('sasl_username', None)
        self.sasl_password = kwargs.get('sasl_password', None)
        self.basic_auth_credentials_source = kwargs.get('basic_auth_credentials_source', None)
        self.basic_auth_user_info = kwargs.get('basic_auth_user_info', None)
        # -----------------
        if not self.topic:
            sys.stderr.write('%% Topic name not specified: \n')
            raise ValueError("Topic name not specified")
        logging.getLogger('kafka').setLevel(logging.INFO)
        if self.basic_auth_user_info is not None:
            producer_conf = {'bootstrap.servers': self.brokers_uri,
                             'log.connection.close': 'false',
                             'security.protocol': self.security_protocol,
                             'ssl.ca.location': self.ssl_ca_location,
                             'sasl.mechanisms': self.sasl_mechanisms,
                             'sasl.username': self.sasl_username,
                             'sasl.password': self.sasl_password

                             }
        else:
            producer_conf = {'bootstrap.servers': self.brokers_uri,
                             'log.connection.close': 'false',
                             'security.protocol': self.security_protocol,
                             'ssl.ca.location': self.ssl_ca_location,

                             }

        # Create MsgProducer instance
        self.producer = Producer(**producer_conf)

    def delivery_callback(self, err, msg):
        if err:
            sys.stderr.write("Failed to deliver message: {}".format(err))
        else:

            sys.stderr.write("Produced record to topic {} partition [{}] @ offset {}"
                             .format(msg.topic(), msg.partition(), msg.offset()))

    def produce_message(self, **kwargs):
        """
               This method accepts a list of messages.
               The producer is now running asynchronous and flush() is only called at the end of the loop.

               Thanks to @Magnus Edenhil we know that calling flush() after each send is ok, but it effectively makes it a synchronous producer which
               has its problems: https://github.com/edenhill/librdkafka/wiki/FAQ#why-is-there-no-sync-produce-interface

               produce() is asynchronous, all it does is enqueue the message on an internal queue which is later (>= queue.buffering.max.ms)
               served by internal threads and sent to the broker (if a leader is available, else wait some more).

               https://github.com/confluentinc/confluent-kafka-python/issues/137

                value must be a list. A check for the type(value) is done so as to be sure to have a list.

               :param kwargs:
               :return:
        """
        value = kwargs.get('value')
        if type(value) is dict:
            list_of_messages = [value]
        elif type(value) is list:
            list_of_messages = kwargs.get('value', None)
        else:
            return 0
        for message in list_of_messages:
            try:
                self.producer.produce(self.topic, value=json.dumps(message), callback=self.delivery_callback)
            except BufferError as e:
                sys.stderr.write('%% Local producer queue is full ' \
                                 '(%d messages awaiting delivery): try again\n' %
                                 len(self.producer))

            self.producer.poll(0)

        sys.stderr.write('%% Waiting for %d deliveries\n' % len(self.producer))
        self.producer.flush()
        return {"topic": self.topic, "sent": True}

    def sync_produce_message(self, **kwargs):
        """
        This function will make a synchronous producer because it calls flush() after each send 
        
        Thanks to @Magnus Edenhil we know that calling flush() after each send is ok, but it effectively makes it a synchronous producer which
        has its problems: https://github.com/edenhill/librdkafka/wiki/FAQ#why-is-there-no-sync-produce-interface
         
        :param kwargs: 
        :return: 
        """
        message = kwargs.get('message', None)
        try:
            self.producer.produce(self.topic, value=json.dumps(message), callback=self._delivery_callback)
            self.producer.poll(0)
            self.producer.flush()
            return {"topic": self.topic, "sent": True}
        except BufferError as e:
            sys.stderr.write('%% Local producer queue is full ' \
                             '(%d messages awaiting delivery): try again\n' %
                             len(self.producer))
            return 0
