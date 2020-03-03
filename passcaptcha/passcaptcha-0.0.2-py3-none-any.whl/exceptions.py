#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exceptions used in library. """


class passcaptchaError(Exception):
    """ nonoCAPTCHA base exception. """


class SafePassage(passcaptchaError):
    """ Raised when all checks have passed. Such as being detected or try
    again.
    """
    pass


class TryAgain(passcaptchaError):
    """ Raised when audio deciphering is incorrect and we can try again. """
    pass


class ReloadError(passcaptchaError):
    """ Raised when audio file doesn't reload to a new one. """
    pass


class DownloadError(passcaptchaError):
    """ Raised when downloading the audio file errors. """
    pass


class ButtonError(passcaptchaError):
    """ Raised when a button doesn't appear. """
    pass


class IframeError(passcaptchaError):
    """ Raised when defacing page times out. """
    pass


class PageError(passcaptchaError):
    """ Raised when loading page times out. """
    pass
