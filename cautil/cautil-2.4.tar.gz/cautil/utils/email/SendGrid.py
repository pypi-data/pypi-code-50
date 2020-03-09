import os
from cautil.utils.email import EmailUtilInterface
from cautil import ConfigDataException
from python_http_client import HTTPError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SendGrid(EmailUtilInterface):

    def __init__(self, config):
        self.config = config
        self.validate_configuration(self.config)

    def send_email(self, to_email, subject, message, **kwargs):
        try:
            mail = Mail(from_email=self.config['from_email_address'],to_emails=to_email,subject=subject,plain_text_content=message)

            sg = SendGridAPIClient(self.config['send_grid_api_key'])
            response = sg.send(mail)
            if response.status_code != 202:
                print(f"Sending mail to {to_email} failed")
                return {"statusCode": response.status_code, "body": {"msg": f"failed to publish_notification: {response.body}"}}

            print(f"Sending mail to {to_email} success")
            return {"statusCode": response.status_code, "body": {"msg": "Mail sent successfully"}}
        except Exception as e:
            print(f"error: {e}")
            return {"statusCode": 500, "body": {"msg": str(e)}}
        except HTTPError as e:
            print(f"HTTP error: {e}")
            return {"statusCode": 500, "body": {"msg": f"error: publish_notification: {e}"}}

    def get_email_configuration(self, **kwargs):
        return self.config

    def set_email_configuration(self, config, **kwargs):
        self.config = config
        self.validate_configuration(self.config)

    def validate_configuration(self, config, **kwargs):
        config_req_param_list = [
            "from_email_address",
            "send_grid_api_key"
        ]
        for param in config_req_param_list:
            if(param not in self.config):
                raise ConfigDataException(
                    'Config param `{}` is missing'.format(param))
        return True

