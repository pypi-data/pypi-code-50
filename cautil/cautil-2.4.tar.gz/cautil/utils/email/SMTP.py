from cautil.utils.email import EmailUtilInterface
from cautil import ConfigDataException

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SMTP(EmailUtilInterface):

    def __init__(self, config):
        self.config = config
        self.validate_configuration(self.config)

    def send_email(self, to_email, subject, message, **kwargs):
        try:
            from_email = self.config['smtpFromEmail']
            if(isinstance(to_email, list)):
                to_email = ",".join(to_email)
            smtp_server = self.__login_smtp_server()
            multipart_msg = MIMEMultipart()
            multipart_msg["From"] = from_email
            multipart_msg["To"] = to_email
            multipart_msg["Subject"] = subject
            multipart_msg.attach(MIMEText(message, "html"))
            smtp_server.send_message(multipart_msg)
            del multipart_msg
            smtp_server.quit()
            return {"statusCode": 200, "body": {"msg": "Mail sent successfully"}}
        except smtplib.SMTPAuthenticationError as e:
            return {"statusCode": e.smtp_code, "body": {"msg":  e.smtp_error.decode('utf-8')}}
        except Exception as e:
            return {"statusCode": 500, "body": {"msg":  str(e)}}

    def get_email_configuration(self, **kwargs):
        return self.config

    def set_email_configuration(self, config, **kwargs):
        self.config = config
        self.validate_configuration(self.config)

    def validate_configuration(self, config, **kwargs):
        config_req_param_list = [
            "smtpUserName",
            "smtpPassword",
            "smtpHost",
            "smtpPort",
            "smtpFromEmail"
        ]
        for param in config_req_param_list:
            if(param not in self.config):
                raise ConfigDataException(
                    'Config param `{}` is missing'.format(param))
        return True

    def __login_smtp_server(self):
        user_name = self.config['smtpUserName']
        password = self.config['smtpPassword']
        host_address = self.config['smtpHost']
        smtp_server = smtplib.SMTP(
            host=host_address, port=self.config['smtpPort'])
        smtp_server.starttls()
        smtp_server.login(user_name, password)
        return smtp_server
