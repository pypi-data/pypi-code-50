#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import json
import requests

@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    help=(
        "Post slack message masquerading as a fictitious user"
    ),
)
@click.argument(
    "channel", type=str, metavar="SLACK_CHANNEL_URL", nargs=1
)
@click.argument("username", type=str, metavar="USER", nargs=1)
@click.argument("message", type=str, metavar="MESSAGE", nargs=1)
@click.argument("emoji", type=str, metavar="EMOJI", nargs=1)
@click.version_option(__VERSION__)
def slackerade_cli(channel, username, message, emoji):
    payload = {"urls": (channel, ),
        "username": username,
        "text": message,
        "icon_emoji": emoji
    requests.post(channel, {"payload": json.dumps(payload)}, verify=False)

if __name__ == "__main__":
    slackerade_cli()
