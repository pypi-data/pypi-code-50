from cautil.utils.email import EmailUtilInterface
from cautil import ConfigDataException

import boto3
import botocore


class SES(EmailUtilInterface):

    def __init__(self, config):
        self.config = config
        self.validate_configuration(self.config)

    def send_email(self, to_email, subject, message, **kwargs):
        try:
            from_email = self.config['smtpFromEmail']
            reply_to = from_email
            client = boto3.client('ses',
                                  region_name=self.config['smtpRegionName'],
                                  aws_access_key_id=self.config['smtpAccessKey'],
                                  aws_secret_access_key=self.config['smtpSecretKey'])
            if(isinstance(to_email, str)):
                to_email = [to_email]
            response = client.send_email(
                Source=from_email,
                Destination={
                    'ToAddresses': to_email
                },
                Message={
                    'Subject': {
                        'Data': subject,
                        'Charset': 'utf8'
                    },
                    'Body': {
                        'Text': {
                            'Data': message,
                            'Charset': 'utf8'
                        }
                    }
                },
                ReplyToAddresses=[
                    reply_to
                ])
            print(response)
            return {"statusCode": response['ResponseMetadata']['HTTPStatusCode'], "body": {"msg": "Mail sent successfully"}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg": str(e)}}

    def get_email_configuration(self, **kwargs):
        return self.config

    def set_email_configuration(self, config, **kwargs):
        self.config = config
        self.validate_configuration(self.config)

    def validate_configuration(self, config, **kwargs):
        config_req_param_list = [
            "smtpAccessKey",
            "smtpSecretKey",
            "smtpRegionName",
            "smtpFromEmail"
        ]
        for param in config_req_param_list:
            if(param not in self.config):
                raise ConfigDataException(
                    'Config param `{}` is missing'.format(param))
        return True
