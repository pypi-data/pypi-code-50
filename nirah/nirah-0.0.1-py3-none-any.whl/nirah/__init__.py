"""
This module provides interfaces for sending messages through a variety of APIs
for updating you on the status on long running processes.

Functions:

discord(msg, target, token=None) -- Sends a message using a discord bot.
twilo(msg, target, token=None)  -- Sends a message using a twilio sms.
"""

import json
import argparse
import discord as d
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from pathlib import Path

SETTINGS_FILE = str(Path.home()) + "/.config/hermes/settings.json"

def discord(msg, target, token=None):
    """Sends a message using a discord bot.

    :param msg: The message to be sent.
    :param target: The username and number.
    :param token: The discord token.
    :returns: None
    :rtype: NoneType

    """
    if not token:
        token = json.load(open(SETTINGS_FILE))["discord_key"]
    client = d.Client()
    @client.event
    async def on_ready():
        try:
            member = client.get_user(target)
            channel = await member.create_dm()
            await channel.send(msg)
            await client.close()
        except AttributeError:
            await client.close()
            raise ValueError("invalid discord token provided")
    client.run(token)


def twilio(msg, target, token=None):
    """Sends a message using twilio sms.

    :param msg: The message to be sent.
    :param target: The username and number.
    :param token: A token in this format: "number:account_sid:auth_token"
    :returns: None
    :rtype: NoneType

    """
    account_sid = None
    auth_token = None
    number = None
    if not token:
        twillio_obj = json.load(open(SETTINGS_FILE))["twillio"]
        account_sid = twillio_obj["account_sid"]
        auth_token = twillio_obj["auth_token"]
        number = twillio_obj["number"]
    else:
        number, account_sid, auth_token = token.split(':')

    try:
        client = Client(account_sid, auth_token)
        client.messages.create(body=msg, from_=number, to=target)
    except TwilioRestException:
        raise ValueError("invalid twilio sid, auth token, or number")


def main():
    parser = argparse.ArgumentParser(prog = "arke",
                                     description="Send a message on a platform.")
    parser.version = "0.0.1"

    parser.add_argument("-v",
                        "--version",
                        action="version",
                        help="displays version info")
    
    parser.add_argument("method",
                        metavar="method",
                        type=str,
                        help="the method used to send the message to the user")

    parser.add_argument("msg",
                        metavar="msg",
                        type=str,
                        help="the message being sent by the user")

    parser.add_argument("target",
                        metavar="target",
                        type=int,
                        help="the person that will receive the message")

    parser.add_argument("-t"
                        "--token",
                        action="store",
                        metavar="auth_token",
                        type=str,
                        help="the api token for the method")

    args = parser.parse_args()

    try:
        if args.method == "discord" or args.method == "d":
            discord(args.msg, args.target, token=args.t__token)
        if args.method == "twilio" or args.method == "t":
            twilio(args.msg, args.target, token=args.t__token)
    except ValueError as err:
        print("error: ", err)

if __name__== "__main__":
    main()
