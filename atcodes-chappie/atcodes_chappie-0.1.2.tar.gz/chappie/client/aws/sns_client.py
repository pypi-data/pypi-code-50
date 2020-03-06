import boto3, json, os, requests, uuid, sys
from cerberus import Validator
from urllib.request import urlopen
from urllib.parse import urlparse

from .s3_client import S3Client

# TODO Find a solution for loading M2Crypto in Lambda
# from M2Crypto import X509
# from base64 import b64decode
# from M2Crypto.Err import M2CryptoError

class SNSClient():

    SNS_MESSAGE_TYPE_SUB_NOTIFICATION = "SubscriptionConfirmation"
    SNS_MESSAGE_TYPE_NOTIFICATION = "Notification"
    SNS_MESSAGE_TYPE_UNSUB_NOTIFICATION = "UnsubscribeConfirmation"

    MIN_MESSAGE_SIZE_TO_BUFFER = 48000 # in Bytes. Anything bigger than a small json.

    def __init__(self):
        # NOTE Assumoing endpoint url is in aws conf file
        self.sns_client = boto3.client('sns')
        self.sqs_client = boto3.client('sqs')
        self.app_name = ''
        self.topic = ''
        self.protocol = ''
        # self.subscription = ''
        self.endpoint_url = ''
        self.message_filter = '__all__'

    def initialize(self):
        """
        create queues based on Filters
            - apply subscription and filter policies
            - store list of created queues as safe_queue_url_list
        Remove abandoned queues
            - list all queues starting with 'AppName_'
            - For all existing queues not in 'safe_queue_url _list', delete the queues
            NOTE: AWS specification says that there must be a 60 sec delay before creating a queue with the same name as a deleted Queue

        Create a S3 bucket to handle Buffering of large messages

        Update subscription of MicroSerice to the SNS Topics
        """
        safe_queue_url_list = []
        if type(self.message_filter) == list:
            for event in self.message_filter:
                queue_url, token_queue_url = self.initialize_queue(event)
                safe_queue_url_list.append(queue_url)
                safe_queue_url_list.append(token_queue_url)

        existing_queues = self.sqs_client.list_queues(QueueNamePrefix=self.get_queue_name_prefix())

        if existing_queues.get("QueueUrls") is not None:
            for queue_url in existing_queues["QueueUrls"]:
                if queue_url not in safe_queue_url_list:
                    queue_attributes = self.sqs_client.get_queue_attributes(
                            QueueUrl=queue_url,
                            AttributeNames=['All']
                    )
                    queue_arn = queue_attributes["Attributes"].get('QueueArn')

                    try:
                        self.initialize_subscription(self.topic, 'sqs', queue_arn, '__none__')
                        self.sqs_client.delete_queue(
                            QueueUrl=queue_url
                        )
                    except Exception as e:
                        print(e)
        try:
            S3Client().create_bucket(self.get_queue_buffer_bucket())
        except Exception as e:
            print(e)

        self.initialize_subscription(self.topic, self.protocol, self.endpoint_url, self.message_filter)

    def initialize_queue(self, event):
        """
        Create a queue for each event
            if event is not fifo:
                Queue will subscribe to the SNS topic and filter messages by event Name
            If event is fifo:
                No subsctiption. App logig should handle queue management

        A Token Queue is always created while creating a queue.
            App logic should handle creating/deleting tokens and managing concurrency of processess handling the event

        Ensure to purge queue after initialize
            - NOTE that purge queue might make system unstable for up to 60 seconds (Aws docs: https://docs.aws.amazon.com/cli/latest/reference/sqs/purge-queue.html )
        """
        fifo = event.get('fifo', False)
        if fifo == False:
            queue = self.sqs_client.create_queue(
                    QueueName=self.get_queue_name(event),
                    Attributes={
                        "VisibilityTimeout": str(event.get('visibility_timeout', 30)),
                        "ReceiveMessageWaitTimeSeconds": "20",
                    }
                )
        else:
            queue = self.sqs_client.create_queue(
                    QueueName=self.get_queue_name(event),
                    Attributes={
                        "VisibilityTimeout": str(event.get('visibility_timeout', 30)),
                        "ReceiveMessageWaitTimeSeconds": "20",
                        "FifoQueue": "true",
                        "ContentBasedDeduplication": "true"
                    }
                )

        # Note use default visibility. Time between token receive and delete should be very short
        token_queue = self.sqs_client.create_queue(
                QueueName=self.get_token_queue_name(event),
                Attributes={
                    "FifoQueue": "true",
                    "ContentBasedDeduplication": "true",
                    "ReceiveMessageWaitTimeSeconds": "20",
                }
            )

        queue_url = queue.get('QueueUrl')
        token_queue_url = token_queue.get('QueueUrl')

        # purge queues
        try:
            self.sqs_client.purge_queue(QueueUrl=queue_url)
        except Exception as e:
            print(e)

        try:
            self.sqs_client.purge_queue(QueueUrl=token_queue_url)
        except Exception as e:
            print(e)

        if queue_url is not None:  ## NOTE this may be needed for error handling.
            queue_attributes = self.sqs_client.get_queue_attributes(
                    QueueUrl=queue_url,
                    AttributeNames=['All']
            )
            queue_arn = queue_attributes["Attributes"].get('QueueArn')

            if fifo == False:
                self.initialize_subscription(self.topic, 'sqs', queue_arn, [event])

                policy_json = self.allow_sns_to_write_to_sqs(self.topic, queue_arn)

                response = self.sqs_client.set_queue_attributes(
                    QueueUrl = queue_url,
                    Attributes = {
                        'Policy' : policy_json
                    }
                )

            return queue_url, token_queue_url
        else:
            print("Unable to initialize queue for event:", event)
            return None, None

    def initialize_subscription(self, topic, protocol, endpoint_url, message_filter):
        """
        Find subscription. Create one if not found.
        Update filter policy to listen to all events in the message_filter
        """
        if endpoint_url != '' and topic != '':
            try:
                response = self.sns_client.list_subscriptions_by_topic(TopicArn=topic)
                next_token = response.get("NextToken") # TODO loop with nexttoken

                while True:
                    for subscription in response["Subscriptions"]:
                        if subscription["Endpoint"] == endpoint_url:
                            subscription_arn = subscription["SubscriptionArn"]
                            self.update_filter_policy(subscription_arn, message_filter)
                            # self.update_filter_policy(subscription_arn, [item["name"] for item in message_filter])
                            return subscription_arn
                    if next_token is not None:
                        response = self.sns_client.list_subscriptions_by_topic(TopicArn=topic,
                                                                            NextToken=next_token)
                        next_token = response.get("NextToken") # TODO loop with nexttoken
                    else:
                        break

                # NOTE this happens only if no existing subscriptions are found
                if message_filter != '__none__':
                    # Do not subscribe
                    subscription = self.sns_client.subscribe(
                        TopicArn=topic,
                        Protocol=protocol,
                        Endpoint=endpoint_url,
                        ReturnSubscriptionArn=True
                    )
                    subscription_arn = subscription["SubscriptionArn"]
                    self.update_filter_policy(subscription_arn, message_filter)
                    #  self.update_filter_policy(subscription_arn, [item["name"] for item in message_filter])
                    return subscription_arn

            except Exception as e:
                print(e)
                return None
        else:
            return None

    def update_filter_policy(self, subscription_arn, message_filter):
        """
        Implements event filter for the subscription
        Set raw attribute for subscription (reduce message size)
        """
        if len(subscription_arn.split(':')) < 7:
            raise Exception("Invalid subscription: " + subscription_arn)

        if message_filter == "__none__":
            # unsubscribe
            try:
                self.sns_client.unsubscribe(SubscriptionArn=subscription_arn)
            except Exception as e:
                print(e)
            return
        elif message_filter == "__all__":
            filter_policy = {}
        else:
            filter_policy = {
                "fliegen_workflow_event": [item["name"] for item in message_filter]
            }

        try:
            self.sns_client.set_subscription_attributes(
                SubscriptionArn=subscription_arn,
                AttributeName="FilterPolicy",
                AttributeValue=json.dumps(filter_policy)
            )
            self.sns_client.set_subscription_attributes(
                SubscriptionArn=subscription_arn,
                AttributeName="RawMessageDelivery",
                AttributeValue="true"
            )
        except Exception as e:
            print (e)

    def add_process(self, event):
        """
        Check if number of active process is < concurrency limit
        if yes:
            - increment process counter.
            - return process token
        if No:
            - return None
        """

        token_queue_url_dict = self.sqs_client.get_queue_url(QueueName=self.get_token_queue_name(event))
        token_queue_url = token_queue_url_dict["QueueUrl"]

        token_queue_attributes = self.sqs_client.get_queue_attributes(
                                        QueueUrl=token_queue_url,
                                        AttributeNames=['All']
                                    )
        num_processes = int(token_queue_attributes["Attributes"].get('ApproximateNumberOfMessages')) \
                            + int(token_queue_attributes["Attributes"].get('ApproximateNumberOfMessagesNotVisible'))
         # This is a fifo Queue so the number should be accurate. However there may be some discrepancy due to async access

        if num_processes < event.get('concurrency_limit', 1):
            print("New FliegenToken to start task for '%s'"%(event.get('name')))
            return self.sqs_client.send_message(
                QueueUrl=token_queue_url,
                MessageBody=str(uuid.uuid4()),
                MessageGroupId='FliegenToken'
            )
        else:
            return None

    def remove_process(self, event):
        """
        delete token and decrement the active process count
        return None
        """
        token_queue_url_dict = self.sqs_client.get_queue_url(QueueName=self.get_token_queue_name(event))
        token_queue_url = token_queue_url_dict["QueueUrl"]

        response = self.sqs_client.receive_message(
                QueueUrl=token_queue_url,
        )

        # NOTE handle situation when message No message is recieved
        if response.get("Messages") is not None:
            messages_list = response.get("Messages")
            message_handle = messages_list[0]["ReceiptHandle"]

            print("Destroying FliegenToken after processing '%s'"%(event.get('name')))
            return self.sqs_client.delete_message(
                QueueUrl=token_queue_url,
                ReceiptHandle=message_handle
            )
        else:
            return None

    def publish_message(self, message, fliegen_workflow_event='default'):
        """
        Send small messages are sent to the SNS Topic.
        Large messages are stored in a special s3 bucket (with 4 hour expiry) using File manager
            - FileManager returns a params dict with storage data
        The FileManager return value is packaged in the message payload.
        """
        payload = json.dumps(message.get("payload"))
        if sys.getsizeof(payload) > self.MIN_MESSAGE_SIZE_TO_BUFFER:
            file_manager = S3Client()
            file_manager.bucket = self.get_queue_buffer_bucket()
            file_manager.expires = 4  # number of hours to live

            payload = file_manager.upload_file(
                    file_data=payload.encode(),
                    path=self.app_name + '/' + fliegen_workflow_event + '/',
                    filename=str(uuid.uuid4()),
                    params_dict = {
                        "Service": "s3"
                    })
            message["payload"] = payload

        message = {"default": json.dumps(message)} # TODO check if multiple json dumps is needed when using raw_data
        message_attributes = {
            'fliegen_workflow_event': {
                    'StringValue': fliegen_workflow_event,
                    'DataType': 'String'
            }
        }

        try:
            return_value = self.sns_client.publish(
                            TopicArn=self.topic,
                            Message=json.dumps(message),
                            MessageStructure='json',
                            MessageAttributes=message_attributes)
            return return_value
        except Exception as e:
            print(e)
            return None

    def extract_message(self, request):
        """
        NOTE Extract message does not pull actual message if it is buffered in S3
            - this is done for code optimization
        Implements SNS Confirmation workflow.
        Return message data that is packaged in a wrapper (for http endpoint, it's request object)
        """
        try:
            ### TODO Find a solution for loading M2Crypto in Lambda
            ### NOTE This issue is addressed by forcing auth to be passed inside notification_message["Message"]
            ### if self.verify_sns_notification(request):

            notification_message = json.loads(request.body)

            if request.META.get("HTTP_X_AMZ_SNS_MESSAGE_TYPE", None) == self.SNS_MESSAGE_TYPE_SUB_NOTIFICATION or \
                        request.META.get("HTTP_X_AMZ_SNS_MESSAGE_TYPE", None) == self.SNS_MESSAGE_TYPE_UNSUB_NOTIFICATION:
                SubscribeURL = notification_message.get('SubscribeURL')

                if SubscribeURL:
                    confirmation_response = requests.get(SubscribeURL)
                return None
            else:
                if type(notification_message) == str:
                    message = json.loads(notification_message)
                elif type(notification_message) == dict:
                    message = notification_message
                else:
                    print("Unable to interpret Message: ", notification_message)
                    message = None

                return message

        except Exception as e:
            print(e)
            raise(e)

    def retrieve_message(self, event):
        """
        Look into message queue and pull out the next message to process.
        If payload is a FileManager Params dict
            - read actual message form S3 bucket.
            - replace payload in message
        return Message and message Handle
        If no more messages Exist return None
            - NOTE important as this is the termination criteria for recursion
        """
        buffered_message_template = {
            "Service": {"type": "string", "required": True},  # TODO change to report_name
            "Bucket": {"type": "string", "required": True},
            "Key": {"type": "string", "required": True},
        }
        valid_buffered_message = Validator(buffered_message_template, allow_unknown=False)

        queue_url_dict = self.sqs_client.get_queue_url(QueueName=self.get_queue_name(event))
        queue_url = queue_url_dict["QueueUrl"]

        response = self.sqs_client.receive_message(
                QueueUrl=queue_url,
        )

        if response.get("Messages") is not None: #TODO check if this is the right condition
            messages_list = response.get("Messages")

            body = json.loads(messages_list[0]["Body"])
            if type(body) == str:
                body = json.loads(body)
            if body.get("Message") is not None:
                message = json.loads(body.get("Message"))
            else:
                message = body

            payload = message.get('payload')
            if valid_buffered_message.validate(payload):
                file_manager = S3Client()
                file_manager.bucket = self.get_queue_buffer_bucket()

                payload = file_manager.download_file(payload)
                payload = json.loads(payload)
                message["payload"] = payload

            return {
                "message": message,
                "message_handle": messages_list[0]["ReceiptHandle"]
            }
        else:
            print("Processed all messages from queue for event '%s'!"%(event['name']), response)
            return None

    def delete_message(self, event, message_handle):
        """
        NOTE: Buffered data will auto expire in 4 Hrs
        Delete message from queue given the message_handle
        return None
        """
        queue_url_dict = self.sqs_client.get_queue_url(QueueName=self.get_queue_name(event))
        queue_url = queue_url_dict["QueueUrl"]

        return self.sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message_handle
        )

    def push_message(self, message, queue_url):
        """
        Small messages are pushed into the queue as-is.
        Large messages are stored in a special s3 bucket (with 4 hour expiry) using File manager
            - FileManager returns a params dict with storage data
        The FileManager return value is packaged in the message payload.
        """
        payload = json.dumps(message.get("payload"))
        if sys.getsizeof(payload) > self.MIN_MESSAGE_SIZE_TO_BUFFER:
            file_manager = S3Client()
            file_manager.bucket = self.get_queue_buffer_bucket()
            file_manager.expires = 4  # number of hours to live

            payload = file_manager.upload_file(
                    file_data=payload.encode(),
                    path=self.app_name + '/' + queue_url.split('/')[-1] + '/',
                    filename=str(uuid.uuid4()),
                    params_dict = {
                        "Service": "s3"
                    })

            message["payload"] = payload

        return self.sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message),
            # MessageBody=message,
            MessageGroupId='FliegenPushFifo'
        )

    def get_queue_buffer_bucket(self):
        """
        Create a bucket for each Notification topic (different for each MicroService).
        Messages recieved in the topic will be stored in a file in this bucket.
        ENsure naming is consistent with S3 naming rules
        """
        # app_name = self.app_name
        topic_name = self.topic.split(':')[-1]

        # bucket_name = app_name + '-' + topic_name
        bucket_name = topic_name
        bucket_name = bucket_name.lower()
        bucket_name = bucket_name.replace('_', '-')
        return bucket_name

    def get_queue_name_prefix(self):
        """
        Standardise prefix (helps with searching for queues)
        """
        app_name = self.app_name
        topic_name = self.topic.split(':')[-1]
        if topic_name == '' or topic_name == None:
            raise Exception('Topic Name is weird for some reason. Ouch!, ' + topic_name )

        return app_name + '_' + topic_name + '_'

    def get_queue_name(self, event):
        """
        ensure fifo queues have .fifo suffix
        """
        if event.get('fifo', False):
            return self.get_queue_name_prefix() + event['name'] + '.fifo'
        else:
            return self.get_queue_name_prefix() + event['name'] # + '.fifo'

    def get_token_queue_name(self, event):
        """
        Keep token queue name similar to the queue name
        """
        return self.get_queue_name_prefix() + event['name'] + '_' + 'tokens.fifo'

    def get_event_queue(self, event):
        """
        Get the queue endpoint for a specific event
        """
        queue_url_dict = self.sqs_client.get_queue_url(QueueName=self.get_queue_name(event))
        return queue_url_dict["QueueUrl"]

    def process_event(self, event, message):
        """
        If event is declared as a FIFO queue, the message is pushed into its FIFO queue
            Standard queue messages are auto pushed to SQS via subscription.
        """
        if event.get('fifo', False):
            queue_url = self.get_event_queue(event=event)
            self.push_message(message=message, queue_url=queue_url)

    def allow_sns_to_write_to_sqs(self, topicarn, queuearn):
        """
        Standard policy to allow SNS topic to send message to standard SQS Queue
        """
        policy_document = """{{
                "Version":"2012-10-17",
                "Statement":[
                    {{
                        "Sid":"MyPolicy",
                        "Effect":"Allow",
                        "Principal" : {{"AWS" : "*"}},
                        "Action":"SQS:SendMessage",
                        "Resource": "{}",
                        "Condition":{{
                            "ArnEquals":{{
                                "aws:SourceArn": "{}"
                            }}
                        }}
                    }}
                ]
            }}""".format(queuearn, topicarn)

        return policy_document

    # NOTE These are utils specific to SNS
    def canonical_message_builder(self, content, format):
        """ Builds the canonical message to be verified.

            Sorts the fields as a requirement from AWS

            Args:
                content (dict): Parsed body of the response
                format (list): List of the fields that need to go into the message
            Returns (str):
                canonical message
        """
        m = ""

        for field in sorted(format):
            try:
                m += field + "\n" + content[field] + "\n"
            except KeyError:
                # Build with what you have
                pass

        return str(m)

    def verify_sns_notification(self, request):
        """ Takes a notification request from Amazon push service SNS and verifies the origin of the notification.

            Kudos to Artur Rodrigues for suggesting M2Crypto: http://goo.gl/KAgPPc

            Args:
                request (HTTPRequest): The request object that is passed to the view function
            Returns (bool):
                True if he message passes the verification, False otherwise
            Raises:
                ValueError: If the body of the response couldn't be parsed
                M2CryptoError: If an error raises during the verification process
                URLError: If the SigningCertURL couldn't be opened
        """
        cert = None
        pubkey = None
        canonical_message = None
        canonical_sub_unsub_format = ["Message", "MessageId", "SubscribeURL", "Timestamp", "Token", "TopicArn", "Type"]
        canonical_notification_format = ["Message", "MessageId", "Subject", "Timestamp", "TopicArn", "Type"]
        content = json.loads(request.body)

        if content.get("Signature"):
            decoded_signature = b64decode(content.get("Signature"))

            # Depending on the message type, canonical message format varies: http://goo.gl/oSrJl8
            if request.META.get("HTTP_X_AMZ_SNS_MESSAGE_TYPE", None) == self.SNS_MESSAGE_TYPE_SUB_NOTIFICATION or \
                    request.META.get("HTTP_X_AMZ_SNS_MESSAGE_TYPE", None) == self.SNS_MESSAGE_TYPE_UNSUB_NOTIFICATION:

                canonical_message = self.canonical_message_builder(content, canonical_sub_unsub_format)

            elif request.META.get("HTTP_X_AMZ_SNS_MESSAGE_TYPE", None) == self.SNS_MESSAGE_TYPE_NOTIFICATION:

                canonical_message = self.canonical_message_builder(content, canonical_notification_format)

            else:
                raise ValueError("Message Type (%s) is not recognized" % request.META.get("HTTP_X_AMZ_SNS_MESSAGE_TYPE", None))

            # Load the certificate and extract the public key
            cert = X509.load_cert_string(str(urlopen(content["SigningCertURL"]).read()))
            pubkey = cert.get_pubkey()
            pubkey.reset_context(md='sha1')
            pubkey.verify_init()

            # Feed the canonical message to sign it with the public key from the certificate
            pubkey.verify_update(canonical_message)

            # M2Crypto uses EVP_VerifyFinal() from openssl as the underlying verification function.
            # http://goo.gl/Bk2G36: "EVP_VerifyFinal() returns 1 for a correct signature, 0 for failure and -1
            # if some other error occurred."
            verification_result = pubkey.verify_final(decoded_signature)

            if verification_result == 1:
                return True
            elif verification_result == 0:
                return False
            else:
                raise M2CryptoError("Some error occured while verifying the signature.")
        else:
            return True # For localstack testing
