#!/usr/bin/env python3
# Copyright 2017-2020 Purism SPC
# SPDX-License-Identifier: AGPL-3.0-or-later

import ldh_client
import re

from getpass import getpass

# define strings that use defaults
ADDRESS_PROMPT = "Enter your " + str(ldh_client.DEFAULT["HOST_LABEL"]) + " address: "
PASSPHRASE_PROMPT = "Enter your passphrase: "


class LdhCredential(object):
    """User credentials for an LDH account."""

    def __init__(self, user, host, passphrase):
        self.user = user
        self.host = host
        self.passphrase = passphrase

    def __str__(self):
        return self.address + " : '" + self.passphrase + "'"

    @property
    def address(self):
        return self.user + "@" + self.host


class LdhError(Exception):
    """Base class for LDH-related errors."""

    def __init__(self, message):
        self.message = message


def prompt_for_credentials():
    """Prompts the user until they enter valid credentials. Returns a valid LdhCredential."""

    valid_address = False

    while not valid_address:
        address = input(ADDRESS_PROMPT)
        regex = r"^[A-Za-z][A-Za-z0-9]*@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+$"
        if not re.match(regex, address):
            print(address + " is not a valid email address.")
        else:
            valid_address = True

    (user, host) = address.split("@")
    passphrase = getpass(PASSPHRASE_PROMPT)

    return LdhCredential(user, host, passphrase)


def get_accounts_from_goa():

    try:
        import gi
        gi.require_version('Goa', '1.0')
    except ValueError:
        raise ImportError('GOA library not available')

    from gi.repository import Goa

    client = Goa.Client.new_sync()
    return client.get_accounts()


def count_goa_credentials():

    count = 0

    try:
        accounts = get_accounts_from_goa()
        for objprx in accounts:
            accprx = objprx.get_account()
            if accprx.props.provider_type == 'librem_one':
                count += 1
    except Exception:
        count = -1

    return count


def get_single_goa_credential():
    """Query GOA for valid credentials."""

    user = None
    host = None
    passphrase = None

    accounts = get_accounts_from_goa()
    count = 0
    for objprx in accounts:
        accprx = objprx.get_account()
        if accprx.props.provider_type == 'librem_one':
            count += 1
            address = accprx.props.identity
            (user, host) = address.split("@")
            pbobj = objprx.get_password_based()
            passphrase = pbobj.call_get_password_sync('password')

    if count == 0:
        raise ValueError("No GOA credentials found.")
    elif count > 1:
        raise ValueError("Too many GOA credentials found.")

    return LdhCredential(user, host, passphrase)


def get_rclone_version():
    """Extract version number from rclone, if it is available."""

    try:

        import sh
        from sh import rclone
        from io import StringIO

        buffer = StringIO()

        try:
            rclone("--version", _out=buffer)
        except sh.ErrorReturnCode_252:
            pass

        return buffer.getvalue()
    except Exception:
        return "None"


def get_yad_version():
    """Extract version number from yad, if it is available."""

    try:

        import sh
        from sh import yad
        from io import StringIO

        buffer = StringIO()

        try:
            yad("--version", _out=buffer)
        except sh.ErrorReturnCode_252:
            pass

        return buffer.getvalue()
    except Exception:
        return "None"
