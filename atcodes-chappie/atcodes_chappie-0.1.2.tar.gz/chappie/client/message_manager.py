from chappie.client.aws import SNSClient
from chappie.client.local import LocalstackSNSClient


class MessageManager():

    def __init__(self, params):
        """ params is a dictionary with 'Service' and other relevant details needed for the service
        For example for aws-sns,
        params = {
            "Service": "aws-sns",
            "Topic": "topic_arn",
            "Endpoint_Url": message listener endpoint,
            "Message_Filter": one of '__all__' or '__none__' or ["list", "of", "strings"]
        }
        For localstack messaging platform,
        params = {
            "Service": "localstack-sns",
            "Topic": "topic_arn",
            "Endpoint_Url": message listener endpoint,
            "Message_Filter": one of '__all__' or '__none__' or ["list", "of", "strings"]
        }
        For rabbitMQ,
        params = {
            "Service": "rabbitmq",
            "NEED": "TO FIND THE PARAMS"
        }
        """
        self.params = params
        self.service = self.params.get("Service")

        if self.service == "localstack-sns":
            self.client = LocalstackSNSClient()
            self.client.app_name = self.params.get('App_Name', '')
            self.client.topic = self.params.get('Topic', '')
            self.client.protocol = self.params.get('Protocol', '')
            self.client.endpoint_url = self.params.get('Endpoint_Url', '')
            self.client.message_filter = self.params.get('Message_Filter', '')
        elif self.service == "aws-sns":
            self.client = SNSClient()
            self.client.app_name = self.params.get('App_Name', '')
            self.client.topic = self.params.get('Topic', '')
            self.client.protocol = self.params.get('Protocol', '')
            self.client.endpoint_url = self.params.get('Endpoint_Url', '')
            self.client.message_filter = self.params.get('Message_Filter', '')
        else:
            self.client = None
            raise ValueError("Messaging Service (%s) is not supported"%(self.service))

    def initialize(self):
        """
        Initialize The messaging platform.
        For AWS, create Queues, Subscriptions, S3 Buffer bucket, and Filter policies
        For LocalStack, create Queues, Subscriptions, Local File storage, and Filter policies
        """
        return self.client.initialize()

    def publish_message(self, *,  message, fliegen_workflow_event='default'):
        """
        Publishes a message on the platform.
        Message will be published with the fliegen_workflow_event
            - For SQS it's added to Attributes, subscribers filter for the appropriate filter policy
        """
        return self.client.publish_message(message, fliegen_workflow_event)

    # TODO change to _from_request
    def extract_message(self, *, wrapper):
        """
        This is used by the message listener (subscriber) to interpret the message recieved at the endpoint.
        - NOTE Buffered messages are not retrieved here (to minimize S3 calls)
        """
        return self.client.extract_message(wrapper)

    # def update_filter_policy(self):
    #     return self.client.update_filter_policy()

    def get_event_queue(self, *, event):
        """
        Returns the Queue endpoint given an event dictionary
        """
        # Cerberus for event format
        return self.client.get_event_queue(event)

    def add_process(self, *, event):
        """
        Check if number of active process is < concurrency limit
        if yes:
            - increment process counter.
            - return process token
        if No:
            - return None
        """
        return self.client.add_process(event)

    def remove_process(self, *, event):
        """
        delete token and decrement the active process count
        return None
        """
        return self.client.remove_process(event)

    def push_message(self, *, message, queue_url):
        """
        Push a message into a queue.
        This is used to ensure fifo queues are handled in sequence
        """
        return self.client.push_message(message, queue_url)

    def retrieve_message(self, *, event):
        """
        Look into message queue and pull out the next message to process.
        return Message and message ID
        If no more messages Exist return None
            - NOTE important as this is the termination criteria for recursion
        """
        return self.client.retrieve_message(event)

    def delete_message(self, *, event, message_handle):
        """
        delete message from queue
        return None
        """
        return self.client.delete_message(event, message_handle)

    def process_event(self, *, event, message):
        """
        Handle any special requirements to process event specific to the client used.
        - For SQS fifo queue, push message to queue
        """
        return self.client.process_event(event, message)
