from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class MailService:
    @staticmethod
    def send_email(from_email, to_emails, subject, html_content, token):
        message = Mail(
            from_email=from_email,
            to_emails=to_emails,
            subject=subject,
            html_content=html_content
        )
        try:
            sg = SendGridAPIClient(token)
            response = sg.send(message)
        except Exception as e:
            raise Exception(str(e))
        return response

    @staticmethod
    def send_verify_email(from_email, to_email, host_name, user_token, sendgrid_token, subject=None):
        html_content = """
        Hello,
        <div>please verify your email address by clicking the link below:</div>
        <a href="https://{host_name}/verify-email?email={email}&token={token}">Verify Email</a>
        <div>If you didn’t request this, please ignore this email.</div>
        """.format(host_name=host_name,email=to_email, token=user_token)
        if not subject:
            subject = "Please verify your email"
        response = MailService.send_email(from_email=from_email, 
                                          to_emails=to_email, 
                                          subject=subject, 
                                          html_content=html_content, 
                                          token=sendgrid_token)
        return response

    @staticmethod
    def send_reset_password(from_email, to_email, host_name, user_token, sendgrid_token, subject=None):
        html_content = """
        <div>Hello,</div>
        <div>We has received a request to change your password. You can do this through the link below:</div>
        <a href="https://{host_name}/reset-password?email={email}&token={token}">Change my password</a>
        <div>If you didn’t request this, please ignore this email. Your password won’t change until you access the link above and create a new one.</div>
        """.format(host_name=host_name, email=to_email, token=user_token)
        if not subject: 
            subject = "Reset your password"
        response = MailService.send_email(from_email=from_email, 
                                          to_emails=to_email, 
                                          subject=subject, 
                                          html_content=html_content, 
                                          token=sendgrid_token)
        return response