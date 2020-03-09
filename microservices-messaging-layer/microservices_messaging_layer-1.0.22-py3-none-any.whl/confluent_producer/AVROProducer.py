# Created by Antonio Di Mariano (antonio.dimariano@gmail.com) at 03/03/2020

from confluent_kafka.avro import AvroProducer
from avro import schema
import sys, requests, json
from confluent_kafka import KafkaError
from .ConfluentProducer import ConfluentProducer


class AVROPRODUCER(ConfluentProducer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.schema_registry_url = kwargs.get('schema_registry_url', None)

        if self.basic_auth_user_info is not None:
            username, password = self.__get_basic_auth_credentials()
            BASIC_AUTH = {"username": username, "password": password}
            producer_conf = {'bootstrap.servers': self.brokers_uri,
                             'schema.registry.url': self.schema_registry_url,
                             'log.connection.close': 'false',
                             'security.protocol': self.security_protocol,
                             'ssl.ca.location': self.ssl_ca_location,
                             'sasl.mechanisms': self.sasl_mechanisms,
                             'sasl.username': self.sasl_username,
                             'sasl.password': self.sasl_password,
                             'schema.registry.basic.auth.credentials.source': self.basic_auth_credentials_source,
                             'schema.registry.basic.auth.user.info': self.basic_auth_user_info

                             }
        else:
            BASIC_AUTH = None
            producer_conf = {'bootstrap.servers': self.brokers_uri,
                             'schema.registry.url': self.schema_registry_url,
                             'log.connection.close': 'false',
                             'security.protocol': self.security_protocol,
                             'ssl.ca.location': self.ssl_ca_location

                             }
        schema_id, default_value_schema = self.__get_latest_schema_for_topic(topic=self.topic + "-value",
                                                                             SCHEMA_REGISTRY_URL=self.schema_registry_url,
                                                                             BASIC_AUTH=BASIC_AUTH)
        schema_id, default_key_schema = self.__get_latest_schema_for_topic(topic=self.topic + "-key",
                                                                           SCHEMA_REGISTRY_URL=self.schema_registry_url,
                                                                           BASIC_AUTH=BASIC_AUTH)

        self.producer = AvroProducer(producer_conf,
                                     default_key_schema=default_key_schema, default_value_schema=default_value_schema)

        self.default_value_schema = default_value_schema

    def __get_basic_auth_credentials(self):
        """
        the BASIC AUTH credentials are store as USERNAME:PASSWORD
        """
        try:
            username = self.basic_auth_user_info.split(':')[0]
            password = self.basic_auth_user_info.split(':')[1]
            return username, password
        except Exception as error:
            sys.stderr.write('%% EXCEPTION getting BASIC AUTH credentials %s \n' % error)
            return 0

    def __make_call_to_the_schema_registry(self, url, headers, auth=None):
        try:
            response = requests.get(
                url=url,
                headers=headers,
                auth=auth)

            return response.json()
        except Exception as error:
            sys.stderr.write('%% EXCEPTION getting making call to schema registry  %s \n' % error)
            return 0

    def __get_latest_schema_for_topic(self, topic, SCHEMA_REGISTRY_URL, BASIC_AUTH=None):
        """

        This method makes two request to the SCHEMA_REGISTY in order
        to get the latest schema version of the given topic.
        The first request lists all the available versions. The second one is the one
        to get the latest schema version.
        If the BASIC_AUTH is not False means that it is a dictionary with username and password as keys.
        They are required when we work with a Confluent Cloud brokers and not with a on-premise ones

        :param topic:
        :param SCHEMA_REGISTRY_URL:
        :param BASIC_AUTH:
        :return:
        """
        try:
            auth = None
            subject = topic
            if BASIC_AUTH:
                from requests.auth import HTTPBasicAuth
                auth = HTTPBasicAuth(BASIC_AUTH.get('username', None), BASIC_AUTH.get('password', None))
            latest_schema_version_request = self.__make_call_to_the_schema_registry(
                url="{}/subjects/{}/versions".format(SCHEMA_REGISTRY_URL, subject),
                headers={
                    "Content-Type": "application/vnd.schemaregistry.v1+json"}, auth=auth)

            if latest_schema_version_request:
                latest_schema_request = self.__make_call_to_the_schema_registry(
                    url="{}/subjects/{}/versions/{}".format(SCHEMA_REGISTRY_URL, subject,
                                                            latest_schema_version_request[-1]),
                    headers={
                        "Content-Type": "application/vnd.schemaregistry.v1+json",
                    },
                    auth=auth)
                if latest_schema_version_request:
                    return latest_schema_request.get("id"), schema.Parse(latest_schema_request.get("schema"))
                else:
                    return 0
            else:
                return 0
        except Exception as error:
            sys.stderr.write('%% EXCEPTION getting getting the latest schema for topic %s %s \n' % topic, error)
            return 0

    def produce_message(self, **kwargs):
        """
        This method accepts a list of messages.
        The producer is now running asynchronous and flush() is only called at the end of the loop.

        Thanks to @Magnus Edenhil
        Calling flush() after each send is ok, but it effectively makes it a synchronous producer which
        has its problems: https://github.com/edenhill/librdkafka/wiki/FAQ#why-is-there-no-sync-produce-interface

        produce() is asynchronous, all it does is enqueue the message on an internal queue which is later (>= queue.buffering.max.ms)
        served by internal threads and sent to the broker (if a leader is available, else wait some more).

        https://github.com/confluentinc/confluent-kafka-python/issues/137

        value must be a list. A check for the type(value) is done so as to be sure to have a list.

        :param kwargs:
        :return:
        """
        callback_function = kwargs.get('delivery_callback', self.delivery_callback)
        value = kwargs.get('value')
        if type(value) is dict:
            list_of_messages = [value]
        elif type(value) is list:
            list_of_messages = kwargs.get('value', None)
        else:
            return 0

        key = kwargs.get('key', None)
        for value in list_of_messages:
            try:
                self.producer.produce(topic=self.topic, value=value, key=key, callback=callback_function)

            except BufferError as error:
                print("Buffer full error:", error)
                self.producer.poll(10)
                self.producer.produce(topic=self.topic, value=value, key=key, callback=callback_function)
            self.producer.poll(0)

        sys.stderr.write('%% Waiting for %d deliveries\n' % len(self.producer))
        self.producer.flush()  # wait for any remaining delivery reports.
        return {"topic": self.topic, "sent": True}

    def sync_produce_message(self, **kwargs):
        """

        This function will make a synchronous producer because it calls flush() after each send

        Thanks to @Magnus Edenhil we know that calling flush() after each send is ok, but it effectively makes it a synchronous producer which
        has its problems: https://github.com/edenhill/librdkafka/wiki/FAQ#why-is-there-no-sync-produce-interface

        :param kwargs:
        :return:
  :
        """
        message = kwargs.get('message', None)
        try:
            self.producer.produce(self.topic, value=json.dumps(message), callback=self.delivery_callback)
            self.producer.poll(0)
            self.producer.flush()
            return {"topic": self.topic, "sent": True}
        except BufferError as e:
            sys.stderr.write('%% Local producer queue is full ' \
                             '(%d messages awaiting delivery): try again\n' %
                             len(self.producer))
            return 0
