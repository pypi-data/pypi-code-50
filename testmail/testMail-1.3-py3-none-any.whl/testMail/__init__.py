from email.mime.text import MIMEText
import smtplib
import re


class Mail(object):
    def __init__(self, user, passwd):
        self.pattern = re.compile(
            '^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        self.USER = user
        self.PASSWD = passwd

        if self.valid(user):
            self.SERVER = "smtp.{}".format(self.USER.split('@')[1])
            self.PORT = 465

        self.smtp = self.login(self.USER, self.PASSWD)

    def login(self, user, passwd):
        """execute user login
        # Arguments
            user: user email for login and sender
            passwd: user app password for login
        """
        smtp = smtplib.SMTP_SSL(self.SERVER, self.PORT)
        smtp.login(user, passwd)

        return smtp

    def valid(self, addr):
        """check email validation
        # Arguments
            addr: string you want to check
        """
        if self.pattern.match(addr):
            return True
        return False

    def send(self, addrs, title, content):
        """mail send to address
        # Arguments
            addrs: receiver's mail (one string or list)
            title: email's title
            content: email's content
        """
        msg = MIMEText(content)
        msg['Subject'] = title

        self.smtp.sendmail(self.USER, addrs, msg.as_string())

    def close(self):
        """disconnect smtp server (logout)
        """
        self.smtp.close()
