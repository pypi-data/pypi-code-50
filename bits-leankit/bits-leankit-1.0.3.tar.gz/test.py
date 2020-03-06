#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script which demos module functionality."""

import os
import sys

from bits.auth import Auth
from bits.settings import Settings

# add bitsapiclient to the path
MYPATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(MYPATH, "bits"))

from bits.leankit import Leankit  # noqa


def main():
    """Execute the main function."""
    settings = Settings().get()
    auth = Auth(settings)
    leankit = Leankit(
        host=settings['leankit']['host'],
        username=settings['leankit']['username'],
        password=settings['leankit']['password'],
        verbose=True,
    )

    # list users
    leankit.client(auth).users_list()

    # update users
    # leankit.client(auth).users_update()


if __name__ == '__main__':
    main()
