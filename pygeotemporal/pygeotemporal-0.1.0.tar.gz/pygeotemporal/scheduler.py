# coding: utf-8

"""
    Parser scheduler.
"""

from builtins import range
import schedule
import subprocess
import smtplib
import time
from email.mime.text import MIMEText


def jobexecute(execution, title, toaddress, sendemail):
    try:
        # for test
        # print "I'm working..."
        subprocess.check_output(execution, shell=True, stderr=subprocess.STDOUT)
        return 1
    except subprocess.CalledProcessError as e: 
        if sendemail:
            now = time.strftime("%c")
            fromaddress = "devnull@ncsa.illinois.edu"
            message = MIMEText("Failed at %s \n-----------------------------------\n %s \n" % (now, e.output))
            message['Subject'] = title
            message['From'] = fromaddress
            message['To'] = toaddress

            server = smtplib.SMTP('smtp.ncsa.illinois.edu', 25)
            server.sendmail(fromaddress, toaddress.split(", "), message.as_string())
            server.quit()

        return 0


# re-execute the job for executionnumber times, and send email the last time. sleep for 10 mins between each execution.
def job(execution, title, toaddress, executionnumber):
    for i in range(0, executionnumber - 1):
        execute_status = jobexecute(execution, title, toaddress, False)
        if execute_status == 1:
            return 
        else:
            time.sleep(10*60)
    jobexecute(execution, title, toaddress, True)
    return 


def scheduler(execution, title, toaddress, executionnumber): 
    # https://github.com/dbader/schedule
    # for test
    # scheduler = schedule.every(1).minutes
    scheduler = schedule.every().monday
    kwargs = {"execution": execution, "title": title, "toaddress": toaddress, "executionnumber": executionnumber}
    scheduler.do(job, **kwargs)

    while True:
        schedule.run_pending()
        time.sleep(1)
