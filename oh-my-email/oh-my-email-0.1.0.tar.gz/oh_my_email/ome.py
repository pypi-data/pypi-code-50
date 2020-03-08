# coding:utf-8
"""
description:
author: jiangyx3915
date: 2020-03-04
"""
import smtplib
from typing import Union, List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from oh_my_email.vo import (
    OhMyEmailContact,
    OhMyEmailConfig,
    OhMyEmailBaseContent,
    BaseAttachment
)
from oh_my_email.utils import _serialize_contacts, _serialize_contacts2str
from oh_my_email.exception import ConnectHostException, EmailAuthException, SendMailException


class OhMyEmail:

    def __init__(self, conf: OhMyEmailConfig):
        self.conf = conf
        self.smtp_client = None

    def get_client(self):
        if self.smtp_client is not None:
            return self.smtp_client
        self.smtp_client = smtplib.SMTP()
        try:
            self.smtp_client.connect(
                host=self.conf.mail_host,
                port=self.conf.mail_port)
        except Exception as e:
            raise ConnectHostException(f"Can not connect email server, {str(e)}")
        try:
            self.smtp_client.login(
                user=self.conf.mail_user,
                password=self.conf.mail_pass)
        except Exception as e:
            raise EmailAuthException(f"Auth Email SMTP Error, {str(e)}")
        return self

    def close_client(self):
        if self.smtp_client is None:
            return
        self.smtp_client.quit()
        self.smtp_client = None

    def __enter__(self):
        return self.get_client()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_client()

    def send(self, *,
             subject: str,
             sender: OhMyEmailContact,
             receiver: List[OhMyEmailContact],
             content: OhMyEmailBaseContent,
             cc: List[OhMyEmailContact] = None,
             bcc: List[OhMyEmailContact] = None,
             attachment: List[BaseAttachment] = None) -> bool:
        """
        send email
        :param subject: email subject
        :param sender:      邮件发送人列表
        :param receiver:    邮件接收人列表
        :param cc:          抄送人列表
        :param bcc:         暗抄人列表
        :param content:
        :param attachment:
        :return:
        """
        real_from_email = sender.render()
        real_to_email = _serialize_contacts(receiver)

        message = MIMEMultipart()
        message.add_header('Subject', subject)
        message.add_header('From', real_from_email)
        message.add_header('To', ",".join(real_to_email))
        message.attach(MIMEText(content.dispatch_content(message), content.content_type, 'utf-8'))

        if cc:
            message.add_header('CC', _serialize_contacts2str(cc))

        if bcc:
            message.add_header('BCC', _serialize_contacts2str(bcc))

        if attachment:
            for item in attachment:
                message.attach(item.patch())

        try:
            self.smtp_client.sendmail(real_from_email, real_to_email, message.as_string())
        except Exception as e:
            raise SendMailException(f'Send Email Error，{str(e)}')
        return True
