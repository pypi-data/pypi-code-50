#!/usr/bin/env python

from __future__ import absolute_import
import os
import six.moves.http_client
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from robot.libraries.BuiltIn import BuiltIn
from applitools.core import logger
from applitools.geometry import Region
from applitools.eyes import Eyes, BatchInfo
from applitools.selenium.webelement import EyesWebElement
from .session import SessionKeywords
from applitools.selenium.positioning import StitchMode
from robot.api import logger as loggerRobot
from EyesLibrary.resources import variables, utils
import six


class CheckKeywords:
    def check_eyes_window(
        self,
        name,
        force_full_page_screenshot=None,
        enable_eyes_log=None,
        enable_http_debug_log=None,
        matchtimeout=-1,
        target=None,
        hidescrollbars=None,
        wait_before_screenshots=None,
        send_dom=None,
        matchlevel=None,
        isdisabled=None
    ):
        """
        Takes a snapshot from the browser using the webdriver and matches
        it with the expected output.

            | =Arguments=                       | =Description=                                                                                                                                                   |
            | Name (str)                        | *Mandatory* - Name that will be given to region in Eyes                                                                                                         |
            | Force Full Page Screenshot (bool) | Will force the browser to take a screenshot of whole page. Define "Stitch Mode" argument on `Open Eyes Session` if necessary                                    |
            | Enable Eyes Log (bool)            | Determines if the trace logs of Applitools Eyes SDK are activated for this test. Overrides the argument set on `Open Eyes Session`                              |
            | Enable HTTP Debug Log (bool)      | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                                                   |
            | Match Timeout (int)               | Determines how much time in milliseconds Eyes continue to retry the matching before declaring a mismatch on this checkpoint                                     |
            | Target (Target)                   | The intended Target. See `Defining Ignore and Floating Regions`                                                                                                 |
            | Hide Scrollbars (bool)            | Sets if the scrollbars are hidden in the checkpoint, by passing 'True' or 'False' in the variable                                                               |
            | Wait Before Screenshots (int)     | Determines the number of milliseconds that Eyes will wait before capturing the screenshot of this checkpoint. Overrides the argument set on `Open Eyes Session` |
            | Send DOM (bool)                   | Sets if DOM information should be sent for this checkpoint                                                                                                      |    
            | Match Level (str)                 | The match level for the comparison of this checkpoint - can be STRICT, LAYOUT, CONTENT or EXACT                                                                 |
            | Is Disabled (bool)                | Determines whether or not interactions with Eyes will be silently ignored for this checkpoint                                                                   |    

        *Example:*
            | Check Eyes Window | Google Homepage | ${true} | ${true} | ${true} | 5000 |

        *Note (Safari on mobile):*
        When checking a window, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.
        """

        original_properties = utils.save_current_properties()
        utils.update_properties(force_full_page_screenshot, enable_eyes_log, enable_http_debug_log, hidescrollbars, wait_before_screenshots, send_dom, matchlevel, None, isdisabled)
        
        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":
            size = variables.driver.get_window_size("current")

            variables.eyes.check_region(
                Region(0, 71, size.__getitem__("width"), size.__getitem__("height")),
                name,
                matchtimeout,
                target,
            )
        else:
            variables.eyes.check_window(name, int(matchtimeout), target)

        utils.update_properties(**original_properties)
      
    def check_eyes_region(
        self,
        left,
        top,
        width,
        height,
        name,
        enable_eyes_log=None,
        enable_http_debug_log=None,
        matchtimeout=-1,
        target=None,
        hidescrollbars=None,
        wait_before_screenshots=None,
        send_dom=None,
        matchlevel=None,
        isdisabled=None
    ):
        """
        Takes a snapshot of the given region from the browser using a Region
        object (identified by left, top, width, height) and matches it with the
        expected output.

        The width and the height cannot be greater than the width and the height specified on `Open Eyes Session`.

            | =Arguments=                   | =Description=                                                                                                                                                   |
            | Left (float)                  | *Mandatory* - The left coordinate of the region that is tested e.g. 100                                                                                         |
            | Top (float)                   | *Mandatory* - The top coordinate of the region that is tested e.g. 150                                                                                          |
            | Width (float)                 | *Mandatory* - The width of the region that is tested e.g. 500                                                                                                   |
            | Height (float)                | *Mandatory* - The height of the region that is tested e.g. 120                                                                                                  |
            | Name (str)                    | *Mandatory* - Name that will be given to region in Eyes                                                                                                         |
            | Enable Eyes Log (bool)        | Determines if the trace logs of Applitools Eyes SDK are activated for this checkpoint. Overrides the argument set on `Open Eyes Session`                        |
            | Enable HTTP Debug Log (bool)  | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                                                   |
            | Match Timeout (int)           | Determines how much time in milliseconds  Eyes continue to retry the matching before declaring a mismatch on this checkpoint                                    |
            | Target (Target)               | The intended Target. See `Defining Ignore and Floating Regions`                                                                                                 |
            | Hide Scrollbars (bool)        | Sets if the scrollbars are hidden in the checkpoint, by passing 'True' or 'False' in the variable                                                               |
            | Wait Before Screenshots (int) | Determines the number of milliseconds that Eyes will wait before capturing the screenshot of this checkpoint. Overrides the argument set on `Open Eyes Session` |
            | Send DOM (bool)               | Sets if DOM information should be sent for this checkpoint                                                                                                      |    
            | Match Level (str)             | The match level for the comparison of this checkpoint - can be STRICT, LAYOUT, CONTENT or EXACT                                                                 |
            | Is Disabled (bool)            | Determines whether or not interactions with Eyes will be silently ignored for this checkpoint                                                                   |    

        *Example:*
            | Check Eyes Region | 100 | 150 | 500 | 120 | Google Logo | ${true} | ${true} | 5000 |
        """
        original_properties = utils.save_current_properties()
        utils.update_properties(None, enable_eyes_log, enable_http_debug_log, hidescrollbars, wait_before_screenshots, send_dom, matchlevel, None, isdisabled)

        region = Region(float(left), float(top), float(width), float(height))
        variables.eyes.check_region(region, name, matchtimeout, target)

        utils.update_properties(**original_properties)

    def check_eyes_region_by_element(
        self,
        element,
        name,
        enable_eyes_log=None,
        enable_http_debug_log=False,
        matchtimeout=-1,
        target=None,
        hidescrollbars=None,
        wait_before_screenshots=None,
        send_dom=None,
        stitchcontent=None,
        matchlevel=None,
        isdisabled=None
    ):
        """
        Takes a snapshot of the region of the given element from the browser
        using the web driver. Not available to mobile native apps.

            | =Arguments=                   | =Description=                                                                                                                                                   |
            | Element (WebElement)          | *Mandatory* - The Web Element to be checked                                                                                                                     |
            | Name (str)                    | *Mandatory* - Name that will be given to region in Eyes                                                                                                         |
            | Enable Eyes Log (bool)        | Determines if the trace logs of Applitools Eyes SDK are activated for this checkpoint. Overrides the argument set on `Open Eyes Session`                        |
            | Enable HTTP Debug Log (bool)  | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                                                   |
            | Match Timeout (int)           | Determines how much time in milliseconds  Eyes continue to retry the matching before declaring a mismatch on this test                                          |
            | Target (Target)               | The intended Target. See `Defining Ignore and Floating Regions`                                                                                                 |
            | Hide Scrollbars (bool)        | Sets if the scrollbars are hidden in the checkpoint, by passing 'True' or 'False' in the variable                                                               |
            | Wait Before Screenshots (int) | Determines the number of milliseconds that Eyes will wait before capturing the screenshot of this checkpoint. Overrides the argument set on `Open Eyes Session` |
            | Send DOM (bool)               | Sets if DOM information should be sent for this checkpoint                                                                                                      |    
            | Stitch Content (bool)         | Determines if Eyes will scroll this element to take a full element screenshot, when the element is scrollable                                                   |    
            | Match Level (str)             | The match level for the comparison of this checkpoint - can be STRICT, LAYOUT, CONTENT or EXACT                                                                 |
            | Is Disabled (bool)            | Determines whether or not interactions with Eyes will be silently ignored for this checkpoint                                                                   |    

        *Example:*
            | ${element}=                  | Get Element | //*[@id="hplogo"] |
            | Check Eyes Region By Element | ${element}  | ElementName       | ${true} | ${true} | 5000 |

        *Note (Safari on mobile):*
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.
        """
        original_properties = utils.save_current_properties()
        utils.update_properties(None, enable_eyes_log, hidescrollbars, wait_before_screenshots, send_dom, matchlevel, stitchcontent, isdisabled)

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":
            location = element.location
            size = element.size

            variables.eyes.check_region(
                Region(
                    location.__getitem__("x"),
                    location.__getitem__("y") + 71,
                    size.__getitem__("width"),
                    size.__getitem__("height"),
                ),
                name,
                matchtimeout,
                target,
                variables.stitchcontent,
            )
        else:
            variables.eyes.check_region_by_element(
                element, name, matchtimeout, target, variables.stitchcontent
            )

        utils.update_properties(**original_properties)

    def check_eyes_region_by_selector(
        self,
        value,
        name,
        selector="id",
        enable_eyes_log=None,
        enable_http_debug_log=None,
        matchtimeout=-1,
        target=None,
        hidescrollbars=None,
        wait_before_screenshots=None,
        send_dom=None,
        stitchcontent=None,
        matchlevel=None,
        isdisabled=None
    ):
        """
        Takes a snapshot of the region of the element found by calling
        find_element(by, value) from the browser using the web driver and
        matches it with the expected output. With a choice from eight
        selectors, to check by on `Using Selectors` section.

        Not available to mobile native apps.

            | =Arguments=                   | =Description=                                                                                                                                             |
            | Value (str)                   | *Mandatory* - The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                      |
            | Name (str)                    | *Mandatory* - Name that will be given to region in Eyes                                                                                                   |
            | Selector (str)                | *Mandatory* - The strategy to locate the element. The supported selectors are specified in `Using Selectors`                                              |
            | Enable Eyes Log (bool)        | Determines if the trace logs of Applitools Eyes SDK are activated for this checkpoint. Overrides the argument set on `Open Eyes Session`                  |
            | Enable HTTP Debug Log (bool)  | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                                             |
            | Match Timeout (int)           | Determines how much time in milliseconds Eyes continue to retry the matching before declaring a mismatch on this checkpoint                               |
            | Target (Target)               | The intended Target. See `Defining Ignore and Floating Regions`                                                                                           |
            | Hide Scrollbars (bool)        | Sets if the scrollbars are hidden in the checkpoint, by passing 'True' or 'False' in the variable                                                         |
            | Wait Before Screenshots (int) | Determines the number of milliseconds that Eyes will wait before capturing the screenshot of this test. Overrides the argument set on `Open Eyes Session` |
            | Send DOM (bool)               | Sets if DOM information should be sent for this checkpoint                                                                                                |    
            | Stitch Content (bool)         | Determines if Eyes will scroll this element to take a full element screenshot, when the element is scrollable                                             |    
            | Match Level (str)             | The match level for the comparison of this checkpoint - can be STRICT, LAYOUT, CONTENT or EXACT                                                           |
            | Is Disabled (bool)            | Determines whether or not interactions with Eyes will be silently ignored for this checkpoint                                                             |    

        *Example:*
            | Check Eyes Region By Selector | .first.expanded.dropdown | Css Element | css selector | ${true} | ${true} | 5000 |

        *Note (Safari on mobile):*
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.
        """
        original_properties = utils.save_current_properties()
        utils.update_properties(None, enable_eyes_log, enable_http_debug_log, hidescrollbars, wait_before_screenshots, send_dom, matchlevel, stitchcontent, isdisabled)
        
        selector_strategy = utils.get_selector_strategy(selector)

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":
            element = variables.driver.find_element(selector_strategy, value)
            location = element.location
            size = element.size

            variables.eyes.check_region(
                Region(
                    location.__getitem__("x"),
                    location.__getitem__("y") + 71,
                    size.__getitem__("width"),
                    size.__getitem__("height"),
                ),
                name,
                matchtimeout,
                target,
                variables.stitchcontent,
            )
        else:
            variables.eyes.check_region_by_selector(
                selector_strategy,
                value,
                name,
                matchtimeout,
                target,
                variables.stitchcontent,
            )

        utils.update_properties(**original_properties)

    def check_eyes_region_in_frame_by_selector(
        self,
        framereference,
        value,
        name,
        selector="id",
        enable_eyes_log=None,
        enable_http_debug_log=None,
        matchtimeout=-1,
        target=None,
        hidescrollbars=None,
        wait_before_screenshots=None,
        send_dom=None,
        stitchcontent=None,
        matchlevel=None,
        isdisabled=None
    ):
        """
        Takes a snapshot of the region of the element found by calling
        find_element(by, value) inside a specific frame, 
        and matches it with the expected output. With a choice from eight
        selectors, to check by on `Using Selectors` section.

            | =Arguments=                              | =Description=                                                                                                                                                   |
            | Frame Reference (str, int or WebElement) | *Mandatory* - Defines the frame to be checked. See below what arguments must be used as frame reference                                                         |
            | Value (str)                              | *Mandatory* - The specific value of the selector. e.g. a CSS SELECTOR value .first.expanded.dropdown                                                            |
            | Name (str)                               | *Mandatory* - Name that will be given to region in Eyes                                                                                                         |
            | Selector (str)                           | *Mandatory* - The strategy to locate the element. The supported selectors are specified in `Using Selectors`                                                    |
            | Enable Eyes Log (bool)                   | Determines if the trace logs of Applitools Eyes SDK are activated for this checkpoint. Overrides the argument set on `Open Eyes Session`                        |
            | Enable HTTP Debug Log (bool)             | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                                                   |
            | Match Timeout (int)                      | Determines how much time in milliseconds Eyes continue to retry the matching before declaring a mismatch on this test                                           |
            | Target (Target)                          | The intended Target. See `Defining Ignore and Floating Regions`                                                                                                 |
            | Hide Scrollbars (bool)                   | Sets if the scrollbars are hidden in the checkpoint, by passing 'True' or 'False' in the variable                                                               |
            | Wait Before Screenshots (int)            | Determines the number of milliseconds that Eyes will wait before capturing the screenshot of this checkpoint. Overrides the argument set on `Open Eyes Session` |
            | Send DOM (bool)                          | Sets if DOM information should be sent for this checkpoint                                                                                                      |    
            | Stitch Content (bool)                    | Determines if Eyes will scroll this element to take a full element screenshot, when the element is scrollable                                                   |    
            | Match Level (str)                        | The match level for the comparison of this checkpoint - can be STRICT, LAYOUT, CONTENT or EXACT                                                                 |
            | Is Disabled (bool)                       | Determines whether or not interactions with Eyes will be silently ignored for this checkpoint                                                                   |    

        *Example:*
            | Check Eyes Region In Frame By Selector | FrameName | .first.expanded.dropdown | Css Element | css selector | ${true} | ${true} | 5000 |

        *Frame Reference*

        In order to locate the correct frame, you must use one of the following references:
         - Str: Name of the frame
         - Int: Index of frame, relative to the list of frames on the page
         - EyesWebElement or WebElement: The frame element

        *Note (Safari on mobile):*
        When checking an element, provide osname=iOS and browsername=Safari on `Open Eyes Session`.
        Due to an issue regarding the height of the address bar not being taken into account when the screenshot is taken, a temporary workaround is in place.
        In order to screenshot the correct element, it is added the value of 71 to the y coordinate of the element.

        """

        original_properties = utils.save_current_properties()
        utils.update_properties(None, enable_eyes_log, enable_http_debug_log, hidescrollbars, wait_before_screenshots, send_dom, matchlevel, stitchcontent, isdisabled)

        if type(framereference) is six.text_type:
            try:
                framereference = int(framereference)
            except:
                framereference = str(framereference)

        selector_strategy = utils.get_selector_strategy(selector)

        # Temporary workaround in order to capture the correct element on Safari
        # Element coordinate y doesn't take the address bar height into consideration, so it has to be added
        # Current address bar height: 71
        if variables.eyes.host_app == "Safari" and variables.eyes.host_os == "iOS":

            with variables.driver.switch_to.frame_and_back(framereference):

                element = variables.driver.find_element(selector_strategy, value)
                location = element.location
                size = element.size

                variables.eyes.check_region(
                    Region(
                        location.__getitem__("x"),
                        location.__getitem__("y") + 71,
                        size.__getitem__("width"),
                        size.__getitem__("height"),
                    ),
                    name,
                    matchtimeout,
                    target,
                    variables.stitchcontent,
                )
        else:
            variables.eyes.check_region_in_frame_by_selector(
                framereference,
                selector_strategy,
                value,
                name,
                matchtimeout,
                target,
                variables.stitchcontent,
            )

        utils.update_properties(**original_properties)

