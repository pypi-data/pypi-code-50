from cautil.utils.notification import NotificationUtilInterface
from cautil import ConfigDataException

import boto3


class SNS(NotificationUtilInterface):

    def __init__(self, config):
        self.client = None
        self.config = config
        self.__validate_configuration(self.config)

    def send_notification(self, device_id, message, **kwargs):
        return { "statusCode": 500, "body": {"msg": 'Functionality not implemented'}}

    def send_group_notification(self, device_ids, message, **kwargs):
        return { "statusCode": 500, "body": {"msg": 'Functionality not implemented'}}

    def create_topic(self, topic_name, **kwargs):
        try:
            sns_client = self.__get_boto3_client()
            sns_response = sns_client.create_topic(Name=topic_name)
            return { "statusCode": 200, "body": {"msg": "Topic created successfully", "topicId": sns_response['TopicArn']}}
        except Exception as e:
            return { "statusCode": 500, "body": {"msg": str(e)}}

    def create_platform_endpoint(self, platform_id, device_id, data, **kwargs):
        try:
            sns_client = self.__get_boto3_client()
            sns_response = sns_client.create_platform_endpoint(PlatformApplicationArn=platform_id,
                                                               Token=device_id, CustomUserData=data)
            return { "statusCode": 200, "body": {"msg": "Endpoint created successfully", "endpointId":sns_response['EndpointArn']}}
        except Exception as e:
            return { "statusCode": 500, "body": {"msg": str(e)}}

    def subscribe(self, topic_id, protocol, endpoint_id, return_subscription_id=True, **kwargs):
        try:
            sns_client = self.__get_boto3_client()
            sns_response = sns_client.subscribe(
                TopicArn=topic_id, Protocol=protocol, Endpoint=endpoint_id, ReturnSubscriptionArn=return_subscription_id)
            return { "statusCode": 200, "body": {"msg": "Subscription created successfully", "subscriptionId": sns_response['SubscriptionArn']}}
        except Exception as e:
            return { "statusCode": 500, "body": {"msg": str(e)}}

    def publish(self, message, topic_id, subject, phone_number=None, message_structure=None, **kwargs):
        try:
            sns_client = self.__get_boto3_client()
            sns_response = sns_client.publish(
                Message=message, TopicArn=topic_id, Subject=subject, PhoneNumber=phone_number, MessageStructure=message_structure)
            return { "statusCode": 200, "body": {"msg": "Message published successfully", "messageId":sns_response['MessageId']}}
        except Exception as e:
            return { "statusCode": 500, "body": {"msg": str(e)}}

    def unsubscribe(self, subscription_id, **kwargs):
        try:
            sns_client = self.__get_boto3_client()
            sns_response = sns_client.unsubscribe(
                SubscriptionArn=subscription_id)
            return { "statusCode": 200, "body": {"msg": "Subscription deleted successfully"}}
        except Exception as e:
            return { "statusCode": 500, "body": {"msg": str(e)}}

    def __get_boto3_client(self):
        if self.client is None:
            self.client = boto3.client('sns', region_name=self.config['snsRegionName'], aws_access_key_id=self.config['snsAccessKey'],
                                       aws_secret_access_key=self.config['snsSecretKey'])
        return self.client
    
    def __validate_configuration(self, config):
        config_req_param_list = [
            "snsAccessKey",
            "snsSecretKey",
            "snsRegionName"
        ]
        for param in config_req_param_list:
            if(param not in self.config):
                raise ConfigDataException(
                    'Config param `{}` is missing'.format(param))
        return True
