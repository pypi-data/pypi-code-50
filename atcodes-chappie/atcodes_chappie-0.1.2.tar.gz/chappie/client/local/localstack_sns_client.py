import boto3, json, os, requests, uuid, sys
from cerberus import Validator
from urllib.request import urlopen
from urllib.parse import urlparse

from .local_client import LocalClient


# TODO for completeness and test needs, might have to implement cached queues in local stack too
class LocalstackSNSClient():

    SNS_MESSAGE_TYPE_SUB_NOTIFICATION = "SubscriptionConfirmation"
    SNS_MESSAGE_TYPE_NOTIFICATION = "Notification"
    SNS_MESSAGE_TYPE_UNSUB_NOTIFICATION = "UnsubscribeConfirmation"

    MIN_MESSAGE_SIZE_TO_BUFFER = 48000 # in Bytes. Anything bigger than a small json.

    def __init__(self):
        # NOTE Setting local endpoint_url
        if os.environ.get('DOCKER_RUNTIME') is None:
            self.sns_client = boto3.client('sns', endpoint_url="http://localhost:4575")
            self.sqs_client = boto3.client('sqs', endpoint_url="http://localhost:4576")
        else:
            self.sns_client = boto3.client('sns', endpoint_url="http://host.docker.internal:4575")
            self.sqs_client = boto3.client('sqs', endpoint_url="http://host.docker.internal:4576")

        self.app_name = ''
        self.topic = ''
        self.protocol = ''
        self.endpoint_url = ''
        self.message_filter = '__all__'

    def initialize(self):
        """
        create queues based on Filters
            - apply subscription and filter policies
            - store list of created queues and associated TokenQueues as safe_queue_url_list
        Remove abandoned queues
            - list all queues starting with 'AppName_'
            - For all existing queues not in 'safe_queue_url _list', delete the queues and their associated token queue
            NOTE: AWS specification says that there must be a 60 sec delay before creating a queue with the same name as a deleted Queue

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
                        # self.sns_client.delete_endpoint(
                        #     EndpointArn=queue_arn
                        # )
                        self.initialize_subscription(self.topic, 'sqs', queue_arn, '__none__')
                        self.sqs_client.delete_queue(
                            QueueUrl=queue_url
                        )
                    except Exception as e:
                        print(e)

        self.initialize_subscription(self.topic, self.protocol, self.endpoint_url, self.message_filter)

    def initialize_queue(self, event):
        """
        Create a queue for each event
            Queue will subscribe to the SNS topic and filter messages by event Name
        A Token Queue is always created while creating a queue.
            Some downstream process (in Alma?) should handle creating/deleting tokens and managing concurrency of processess handling the event

        Ensure to purge queue after initialize
            - NOTE that purge queue might make system unstable for up to 60 seconds (Aws docs: https://docs.aws.amazon.com/cli/latest/reference/sqs/purge-queue.html )
        """
        fifo = event.get('fifo', False)
        if fifo == False:
            queue = self.sqs_client.create_queue(
                    QueueName=self.get_queue_name(event),
                    Attributes={
                        "VisibilityTimeout": str(event.get('visibility_timeout', 30)),
                        "ReceiveMessageWaitTimeSeconds": "1",
                    }
                )
        else:
            queue = self.sqs_client.create_queue(
                    QueueName=self.get_queue_name(event),
                    Attributes={
                        "VisibilityTimeout": str(event.get('visibility_timeout', 30)),
                        "ReceiveMessageWaitTimeSeconds": "1",
                        "FifoQueue": "true",
                        "ContentBasedDeduplication": "true"
                    }
                )

        token_queue = self.sqs_client.create_queue(
                QueueName=self.get_token_queue_name(event),
                Attributes={
                    "FifoQueue": "true",
                    "ContentBasedDeduplication": "true",
                    "ReceiveMessageWaitTimeSeconds": "1",
                }
            )

        queue_url = queue.get('QueueUrl')
        token_queue_url = token_queue.get('QueueUrl')

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
                next_token = response.get("NextToken")

                while True:
                    for subscription in response["Subscriptions"]:
                        if subscription["Endpoint"] == endpoint_url:
                            subscription_arn = subscription["SubscriptionArn"]
                            self.update_filter_policy(subscription_arn, message_filter)

                            return subscription_arn
                    if next_token is not None:
                        response = self.sns_client.list_subscriptions_by_topic(TopicArn=topic,
                                                                            NextToken=next_token)
                        next_token = response.get("NextToken")
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
                AttributeValue=json.dumps(filter_policy))
            self.sns_client.set_subscription_attributes(
                SubscriptionArn=subscription_arn,
                AttributeName="RawMessageDelivery",
                AttributeValue="true"
            )
        except Exception as e:
            print(e)

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
            print("Approved addition of FliegenToken (%d) to start task for '%s'"%(num_processes, event.get('name')))
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

        token_queue_attributes = self.sqs_client.get_queue_attributes(
                                        QueueUrl=token_queue_url,
                                        AttributeNames=['All']
                                    )
        num_processes = int(token_queue_attributes["Attributes"].get('ApproximateNumberOfMessages')) \
                            + int(token_queue_attributes["Attributes"].get('ApproximateNumberOfMessagesNotVisible'))

        response = self.sqs_client.receive_message(
                QueueUrl=token_queue_url,
        )

        # NOTE handle situation when message No message is recieved
        if response.get("Messages") is not None:
            messages_list = response.get("Messages")
            message_handle = messages_list[0]["ReceiptHandle"]

            print("Destroying FliegenToken for '%s'. %d Active Processes."%(event.get('name'), num_processes))
            return self.sqs_client.delete_message(
                QueueUrl=token_queue_url,
                ReceiptHandle=message_handle
            )
        else:
            return None

    def publish_message(self, message, fliegen_workflow_event='default'):
        """
        Send small messages are sent to the SNS Topic.
        Large messages are stored in /tmp in local file system using File manager
            - FileManager returns a params dict with storage data
        The FileManager return value is packaged in the message payload.
        """
        payload = json.dumps(message.get("payload"))
        if sys.getsizeof(payload) > self.MIN_MESSAGE_SIZE_TO_BUFFER:
            file_manager = LocalClient()
            file_manager.folder = '/tmp/'

            payload = file_manager.upload_file(
                    file_data=payload.encode(),
                    path=fliegen_workflow_event + '/',
                    filename=str(uuid.uuid4()),
                    params_dict={
                        "Service": 'local'
                    })

            message["payload"] = payload

        message = json.dumps(message) # TODO check which works for localtack
        # message = {"default": json.dumps(message)}
        message_attributes = {
            'fliegen_workflow_event': {
                    'StringValue': fliegen_workflow_event,
                    'DataType': 'String'
            }
        }
        if len(self.topic.split(':')) < 6:
            raise Exception("Invalid topic: " + self.topic)

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
        NOTE Extract message does not pull actual message if it is buffered in file
            - this is done for code optimization

        Return message data that is packaged in a wrapper (for http endpoint, it's request object)
        """
        try:
            notification_message = json.loads(request.body)

            if type(notification_message) == str:
                message = json.loads(notification_message)
            elif type(notification_message) == dict:
                message = notification_message
            else:
                print("Unable to interpret Message: ", notification_message)
                message = None

            return message
        except Exception as e:
            raise(e)

    def retrieve_message(self, event):
        """
        Look into message queue and pull out the next message to process.
        If payload is a FileManager Params dict
            - read actual message form file.
            - replace payload in message
        return Message and message Handle
        If no more messages Exist return None
            - NOTE important as this is the termination criteria for recursion
        """
        buffered_message_template = {
            "Service": {"type": "string", "required": True},  # TODO change to report_name
            "Filename": {"type": "string", "required": True}
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
                file_manager = LocalClient()
                file_manager.folder = '/tmp/'

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
        NOTE: Buffered data are not deleted. Just periodically delete files from /tmp
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
        Large messages are stored in in /tmp folder using File manager
            - FileManager returns a params dict with storage data
        The FileManager return value is packaged in the message payload.
        """
        payload = json.dumps(message.get("payload"))
        if sys.getsizeof(payload) > self.MIN_MESSAGE_SIZE_TO_BUFFER:
            file_manager = LocalClient()
            file_manager.folder = '/tmp/'

            message = file_manager.upload_file(
                    file_data=payload.encode(),
                    path=queue_url.split('/')[-1] + '/',
                    filename=str(uuid.uuid4()),
                    params_dict={
                        "Service": 'local'
                    })

            message["payload"] = payload

        return self.sqs_client.send_message( # NOTE watch out for deduplication crash, whatever that is...
            QueueUrl=queue_url,
            MessageBody=json.dumps(message),
            # MessageBody=message,
            MessageGroupId='FliegenPushFifo'
        )

    def get_queue_name_prefix(self):
        """
        Standardise prefix (helps with searching for queues)
        """
        app_name = self.app_name
        topic_name = self.topic.split(':')[-1]

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

