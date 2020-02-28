import datetime
import slack
import os


def convertTimestampToUnixEpoch(timeStamp: datetime.datetime):
    if timeStamp == None:
        return None
    result = timeStamp.timestamp()
    return result


def convertUnixEpochToTimestamp(unixEpoch: int):
    if unixEpoch == None:
        return None
    timestamp = datetime.datetime.fromtimestamp(unixEpoch)
    result = timestamp.strftime("%Y/%m/%d %H:%M:%S.%f")
    return result


def notifySlack(message, channel='#console'):
    client = slack.WebClient(token=os.environ.get("KOVA_SLACK_TOKEN"))
    response = client.chat_postMessage(channel=channel, text=message)
