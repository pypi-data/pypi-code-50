from __future__ import absolute_import
import six.moves.http_client
import os
import logging
from applitools.core import logger, StdoutLogger
from applitools.eyes import MatchLevel
from applitools.core import EyesIllegalArgument
from applitools.selenium.positioning import StitchMode
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from . import variables


def get_match_level(matchlevel):

    selected_match_level = None

    if matchlevel.upper() == "STRICT":
        selected_match_level = MatchLevel.STRICT
    elif matchlevel.upper() == "CONTENT":
        selected_match_level = MatchLevel.CONTENT
    elif matchlevel.upper() == "LAYOUT":
        selected_match_level = MatchLevel.LAYOUT
    elif matchlevel.upper() == "EXACT":
        selected_match_level = MatchLevel.EXACT
    else:
        raise EyesIllegalArgument(
            "Please select a valid match level: Strict, Content, Layout, Exact"
        )

    return selected_match_level


def get_stitch_mode(stitchmode):

    selected_stitch_mode = None

    if stitchmode.upper() == "CSS":
        selected_stitch_mode = StitchMode.CSS
    elif stitchmode.upper() == "SCROLL":
        selected_stitch_mode = StitchMode.Scroll
    else:
        raise EyesIllegalArgument(
            "Please select a valid match stitch mode: Css, Scroll"
        )

    return selected_stitch_mode


def get_selector_strategy(selector):

    selected_strategy = None

    if selector.upper() == "CSS SELECTOR":
        selected_strategy = By.CSS_SELECTOR
    elif selector.upper() == "XPATH":
        selected_strategy = By.XPATH
    elif selector.upper() == "ID":
        selected_strategy = By.ID
    elif selector.upper() == "LINK TEXT":
        selected_strategy = By.LINK_TEXT
    elif selector.upper() == "PARTIAL LINK TEXT":
        selected_strategy = By.PARTIAL_LINK_TEXT
    elif selector.upper() == "NAME":
        selected_strategy = By.NAME
    elif selector.upper() == "TAG NAME":
        selected_strategy = By.TAG_NAME
    elif selector.upper() == "CLASS NAME":
        selected_strategy = By.CLASS_NAME
    else:
        raise InvalidElementStateException(
            "Please select a valid selector: CSS SELECTOR, XPATH, ID, LINK TEXT, PARTIAL LINK TEXT, NAME, TAG NAME, CLASS NAME"
        )

    return selected_strategy


def manage_logging(enable_eyes_log=None, enable_http_debug_log=None):
    
    if enable_eyes_log is True:
        logger.set_logger(StdoutLogger())
        logger.open_()
    elif enable_eyes_log is False:
        logger.close()
        logger.set_logger(None)

    if enable_http_debug_log is True:
        six.moves.http_client.HTTPConnection.debuglevel = 1
    elif enable_http_debug_log is False:
        six.moves.http_client.HTTPConnection.debuglevel = 0


def save_current_properties():
    return {
        "force_full_page_screenshot": variables.eyes.force_full_page_screenshot,
        "enable_eyes_log": logger._logger_to_use is not None,
        "enable_http_debug_log": six.moves.http_client.HTTPConnection.debuglevel > 0,
        "hidescrollbars": variables.eyes.hide_scrollbars,
        "wait_before_screenshots": variables.eyes.wait_before_screenshots,
        "send_dom": variables.eyes.send_dom,
        "matchlevel": variables.eyes.match_level,
        "stitchcontent": variables.stitchcontent,
        "isdisabled": variables.eyes.is_disabled
    }

def save_current_logging_properties():
    return {
        "enable_eyes_log": logger._logger_to_use is not None,
        "enable_http_debug_log": six.moves.http_client.HTTPConnection.debuglevel > 0,
    }

def update_properties(
    force_full_page_screenshot=None,
    enable_eyes_log=None,
    enable_http_debug_log=None,
    hidescrollbars=None,
    wait_before_screenshots=None,
    send_dom=None,
    matchlevel=None,
    stitchcontent=None,
    isdisabled=None
):

    if force_full_page_screenshot is not None:
        variables.eyes.force_full_page_screenshot = force_full_page_screenshot

    if enable_eyes_log is not None or enable_http_debug_log is not None:
        manage_logging(enable_eyes_log, enable_http_debug_log)

    if hidescrollbars is not None:
        variables.eyes.hide_scrollbars = hidescrollbars

    if wait_before_screenshots is not None:
        variables.eyes.wait_before_screenshots = int(wait_before_screenshots)

    if send_dom is not None:
        variables.eyes.send_dom = send_dom

    if matchlevel is not None:
        try:
            variables.eyes.match_level = get_match_level(matchlevel)
        except:
            variables.eyes.match_level = matchlevel

    if stitchcontent is not None:
        variables.stitchcontent = stitchcontent

    if isdisabled is not None:
        variables.eyes.is_disabled = isdisabled
