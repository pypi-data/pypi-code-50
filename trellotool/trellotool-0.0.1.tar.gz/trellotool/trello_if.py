#!/usr/bin/env python
#
# trello_if.py - Interface to Trello
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#

import sys
import os

from trello import TrelloClient

from trellotool import config


member_store = {}
client = None


def check_credentials():

    global client

    api_key = os.environ.get("TRELLO_API_KEY")
    api_secret = os.environ.get("TRELLO_API_SECRET")
    err = False

    cmd = os.path.basename(sys.argv[0])

    if api_key is None:
        print("{}: You need to have the env variable TRELLO_API_KEY set"
              .format(cmd))
        print("You can get this from visiting https://trello.com/app-key and "
              "copying the key")
        print("into your shell, like this, 'export TRELLO_API_KEY=sjkfhksdhf"
              "jksdhfkjsdhfk'")
        print()
        err = True

    if api_secret is None:
        print("{}: You need to have the env variable TRELLO_API_SECRET set"
              .format(cmd))
        print("You can get this from visiting https://trello.com/app-key, "
              "generating a Token")
        print("and copy that into your shell, like this,"
              "'export TRELLO_API_SECRET=dkfjg9045jgl'")
        print()
        err = True

    if err:
        print("Exiting...")
        sys.exit(1)

    client = TrelloClient(
        api_key=api_key,
        api_secret=api_secret
    )


def get_boards():
    boards = client.list_boards()
    return boards


def get_board(board_id):
    return client.get_board(board_id)


def get_cards(list_id):
    tlist = client.get_list(list_id)
    return tlist.list_cards()


def get_member_info(member_id):
    try:
        return member_store[member_id]
    except KeyError:
        member_obj = client.get_member(member_id)
        member_store[member_id] = member_obj
        return member_obj


def add_card(tlist_name, card_title, card_description):
    tlist_id = config.get_list_id_by_name(tlist_name)

    if tlist_id is None:
        print("Error: Couldn't not find list, so can't add card")
        sys.exit(2)

    tlist = client.get_list(tlist_id)
    tlist.add_card(name=card_title,
                   desc=card_description)
