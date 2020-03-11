#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : mi.
# @File         : send_email
# @Time         : 2020-03-04 13:58
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(subject="邮件测试", msg="邮件测试信息", receivers='yuanjie@xiaomi.com', isstaging=1, _subtype='html'):
    token = {
        "mail.b2c.srv": "U92BzW2jqR@xiaomi.com",
        "mail.test.b2c.srv": "134a1ab8c0efbe14884b9956321818e0@xiaomi.com"
        # "9297367afe24f39009dae012d2fd0342@xiaomi.com"
    }
    smtp = smtplib.SMTP("mail.test.b2c.srv" if isstaging else "mail.b2c.srv", 25)
    sender = token[smtp._host]

    if isinstance(receivers, str) and receivers.__contains__("@"):
        receivers = [receivers]

    message = MIMEText(msg, _subtype, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = sender
    message['To'] = ",".join(receivers)

    try:
        smtp.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(f"{e}: 无法发送邮件")


if __name__ == '__main__':
    send_email(isstaging=1)