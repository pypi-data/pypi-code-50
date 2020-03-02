# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------
#
#  This file is part of the Chirp Python SDK.
#  For full information on usage and licensing, see https://chirp.io/
#
#  Copyright (c) 2011-2019, Asio Ltd.
#  All rights reserved.
#
# ------------------------------------------------------------------------


class ChirpSDKError(Exception):

    def __init__(self, message, code=None):
        """
        Raise a Chirp core related error.

        Args:
            message (str): Error message
            receive (int): Response code from the core

        """
        super(ChirpSDKError, self).__init__(self)
        self.message = message
        self.error_code = code

    def __str__(self):
        """Return the error message."""
        return self.message


class ChirpSDKAudioError(Exception):
    """ An error raised from the ChirpSDK audio handling. """

    pass  # noqa: WPS604


class ChirpSDKNetworkError(Exception):
    """ An error raised from the ChirpSDK network handling. """

    pass  # noqa: WPS604
