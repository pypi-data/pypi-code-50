import json
import os
import time

from google.cloud import pubsub_v1
from qai.issues.add_issues import (
    add_issues_format_insensitive,
    add_issues_format_insensitive_batch,
)
from qai.issues.validation import Validator
from qai.qconnect.qremoteconnection import QRemoteConnection
from qai.qconnect.qrest import QRest
from singleton_decorator import singleton
from toolz import partial


# 'self' means nothing outside of a class
# but pubsub demands a unary callback, so we need to be clever
# when we use this in the class we partially apply with the class instance
def process_message(self, message):
    # TODO develop a way to report errors since we act the message from start
    message.ack()
    json_message = safe_extract(message)
    json_data = json_message['data']
    try:
        # if it has items it is a dict
        _ = json_data.items()
        # if it is a dict, make it an array
        els = [json_data]
    except AttributeError:
        # can't call .items(), so it's already an array
        els = json_data
    resp_list = []

    if self.batching:
        resp_list = add_issues_format_insensitive_batch(self, els, self.debug, verbose=self.verbose)
        # update message timestamp and data
        json_message['metadata']['timestamp'] = int(time.time())
        json_message['data'] = json.dumps(resp_list)
        self.publish_message(json.dumps(json_data))

    for el in els:
        el = add_issues_format_insensitive(self, el, self.validator, debug=self.debug, verbose=self.verbose)
        resp_list.append(el)
    # update message timestamp and data
    json_message['metadata']['timestamp'] = int(time.time())
    json_message['data'] = resp_list[0]
    self.publish_message(json.dumps(json_message))


def safe_extract(message):
    try:
        data_string = message.data.decode()
        try:
            json_data = json.loads(data_string)
        except Exception as e:
            json_data = {}
            print(e)
            print("error parsing json", data_string)
    except TypeError:
        json_data = {}
        print('''error decoding bytestring from pubsub this is pretty bad''', message.data)
    return json_data


@singleton
class QPubSub(QRemoteConnection):
    def __init__(
            self,
            analyzer,
            category="",
            white_lister=None,
            config_path=["conf", "config.json"],
            batching=False,
            debug=False,
            verbose=False,
            sentence_token_limit=1024,
            ignore_html=True,
            ignore_inside_quotes=False,
    ):
        config_file = os.path.join(os.getcwd(), *config_path)
        super().__init__(analyzer, category, white_lister, config_file)

        self.project_id = str(self.configs["PROJECT_ID"])
        self.subscription_name = str(self.configs["SUBSCRIPTION_NAME"])
        self.topic_name = str(self.configs["TOPIC_NAME"])
        self.max_messages = int(self.configs["MAX_MESSAGES"])

        self.batching = batching
        self.debug = debug
        self.verbose = verbose
        self.sentence_token_limit = sentence_token_limit
        self.ignore_html = ignore_html
        self.ignore_inside_quotes = ignore_inside_quotes
        nlp_obj = getattr(analyzer, "nlp", None)
        self.validator = Validator(nlp_obj=nlp_obj, sentence_token_limit=sentence_token_limit, ignore_html=ignore_html)

        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(self.project_id, self.subscription_name)
        self.flow_control = pubsub_v1.types.FlowControl(max_messages=self.max_messages)

        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(self.project_id, self.topic_name)

    def publish_message(self, message):
        def get_callback(f, data):
            def callback(f):
                try:
                    print('Call back @ ' + str(time.time()))
                    # print('Published   ' + data)
                except:  # noqa
                    print("Please handle {} for {}.".format(f.exception(), data))

            return callback

        future = self.publisher.publish(self.topic_path, data=message.encode("utf-8"))
        future.add_done_callback(get_callback(future, message))

    def get_future(self):
        pubsub_arity_callback = partial(process_message, self)
        streaming_pull_future = self.subscriber.subscribe(self.subscription_path, callback=pubsub_arity_callback,
                                                          flow_control=self.flow_control)
        print("QPubSub get_future() called: Listening for messages on {}..\n".format(self.subscription_path))
        return streaming_pull_future

    def connect(self):
        pubsub_arity_callback = partial(process_message, self)
        streaming_pull_future = self.subscriber.subscribe(self.subscription_path, callback=pubsub_arity_callback,
                                                          flow_control=self.flow_control)
        print("QPubSub connect() called: Listening for messages on {}..\n".format(self.subscription_path))
        try:
            return streaming_pull_future.result()
        except Exception as e:
            streaming_pull_future.cancel()
            print("Listening for messages on {} threw an exception: {}.".format(self.subscription_name, e))

    def connect_with_rest(self, rest_connection: QRest):
        self.get_future()
        rest_connection.connect()
