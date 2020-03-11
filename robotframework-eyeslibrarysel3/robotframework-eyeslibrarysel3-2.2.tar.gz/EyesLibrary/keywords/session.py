#!/usr/bin/env python

from __future__ import absolute_import
import os
import six.moves.http_client
import base64
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from applitools import logger
from applitools.logger import StdoutLogger
from applitools.logger import FileLogger
from applitools.geometry import Region
from applitools.eyes import Eyes, BatchInfo
from applitools.selenium.webelement import EyesWebElement
from applitools.selenium.positioning import StitchMode
from robot.api import logger as loggerRobot
from datetime import datetime
from ..version import __version__
from EyesLibrary.resources import variables, utils
import six


class SessionKeywords(object):

    library_arguments = {}

    def open_eyes_session(
        self,
        apikey=None,
        appname=None,
        testname=None,
        library=None,
        width=None,
        height=None,
        osname=None,
        browsername=None,
        matchlevel=None,
        enable_eyes_log=None,
        enable_http_debug_log=None,
        baselinename=None,
        batch=None,
        branchname=None,
        parentbranch=None,
        serverurl=None,
        force_full_page_screenshot=None,
        stitchmode=None,
        matchtimeout=None,
        hidescrollbars=None,
        save_new_tests=None,
        wait_before_screenshots=None,
        send_dom=None,
        stitchcontent=False,
        isdisabled=None,
    ):
        """
        Starts a session (=test) with Applitools.

        Some of the following arguments may also be defined on library import.
        See `Before running tests` or `Importing`.

            | =Arguments=                       | =Description=                                                                                                                               |
            | API Key (str)                     | *Mandatory* - User's Applitools Eyes key                                                                                                    |
            | Application Name (str)            | *Mandatory* - The name of the application under test                                                                                        |
            | Test Name (str)                   | *Mandatory* - The test name                                                                                                                 |  
            | Library (str)                     | Library to test (Either SeleniumLibrary or AppiumLibrary)                                                                                   |
            | Width (int)                       | The width of the browser window e.g. 1280                                                                                                   |
            | Height (int)                      | The height of the browser window e.g. 1000                                                                                                  |
            | Operating System (str)            | The operating system of the test, can be used to override the OS name to allow cross OS verification                                        |
            | Browser Name (str)                | The browser name for the test, can be used to override the browser name to allow cross browser verification                                 |
            | Match Level (str)                 | The match level for the comparison of this test's checkpoints - can be STRICT, LAYOUT, CONTENT or EXACT                                     |
            | Enable Eyes Log (bool)            | Determines if the trace logs of Applitools Eyes SDK are activated for this session                                                          |
            | Enable HTTP Debug Log (bool)      | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                                               |
            | Baseline Name (str)               | Name of the branch where the baseline reference will be taken from and where new and accepted steps will be saved to                        |
            | Batch (str or BatchInfo)          | The desired batch. See `Group tests into batches`                                                                                           |
            | Branch Name (str)                 | The branch to use to check test                                                                                                             |
            | Parent Branch (str)               | Parent Branch to base the new Branch on                                                                                                     |
            | Server URL (str)                  | The URL of the Eyes server. If not provided then your test will run on the public cloud                                                     |
            | Force Full Page Screenshot (bool) | Will force the browser to take a screenshot of whole page                                                                                   |
            | Stitch Mode (str)                 | Type of stitching used for full page screenshots - can be CSS or SCROLL                                                                     |
            | Match Timeout (int)               | Determines how much time in milliseconds Eyes continues to retry the matching before declaring a mismatch on this test checkpoints          |
            | Hide Scrollbars (bool)            | Sets if the scrollbars are hidden this session's tests, by passing 'True' or 'False' in the variable                                        |
            | Save New Tests (bool)             | Sets if the new checkpoints on this session are automatically accepted, by passing 'True' or 'False' in the variable                        |
            | Wait Before Screenshots (int)     | Determines the number of milliseconds that Eyes will wait before capturing a screenshot on this test checkpoints                            |
            | Send DOM (bool)                   | Sets if DOM information should be sent for this session's checkpoints                                                                       |    
            | Stitch Content (bool)             | If this test checkpoint's elements/region are scrollable, determines if Eyes will scroll this them to take a full region/element screenshot |    
            | Is Disabled (bool)                | Determines whether or not interactions with Eyes will be silently ignored for this test                                                     |    

        *Mandatory Arguments:* They may be defined through this keyword, or when importing the library.
        In order to run a test, provide at least the API Key, Application Name and Test Name.
 
        When opening the session on a mobile browser or hybrid app, the context must be set to WEBVIEW in order to retrieve the correct viewport size. Geolocation of the device may have to be set after switching context.

        *Example:*                                                                                                                                                                                                                               
            | Open Eyes Session | YourApplitoolsKey | AppName | TestName | SeleniumLibrary | 1024 | 768 | OSOverrideName | BrowserOverrideName | layout | ${true} | batchname=BatchName | serverurl=https://myserver.com |
        """

        if appname is None:
            appname = self.library_arguments["appname"]
        if testname is None:
            testname = self.library_arguments["testname"]
        if apikey is None:
            apikey = self.library_arguments["apikey"]
        if library is None:
            library = self.library_arguments["library"]
        if osname is None:
            osname = self.library_arguments["osname"]
        if browsername is None:
            browsername = self.library_arguments["browsername"]
        if matchlevel is None:
            matchlevel = self.library_arguments["matchlevel"]
        if enable_eyes_log is None:
            enable_eyes_log = self.library_arguments["enable_eyes_log"]
        if serverurl is None:
            serverurl = self.library_arguments["serverurl"]
        if save_new_tests is None:
            save_new_tests = self.library_arguments["save_new_tests"]
        if matchtimeout is None:
            matchtimeout = self.library_arguments["matchtimeout"]

        if serverurl is None:
            variables.eyes = Eyes()
        else:
            variables.eyes = Eyes(serverurl)

        variables.eyes.api_key = apikey

        try:
            libraryInstance = BuiltIn().get_library_instance(library)

            if library == "AppiumLibrary":
                driver = libraryInstance._current_application()
            else:
                driver = libraryInstance.driver
        except RuntimeError:
            raise Exception("%s instance not found" % library)

        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        if osname is not None:
            variables.eyes.host_os = osname
        if browsername is not None:
            variables.eyes.host_app = browsername
        if baselinename is not None:
            variables.eyes.baseline_branch_name = baselinename
        if batch is not None:
            if type(batch) is six.text_type:
                batch = str(batch)
            batches_list = variables.batches

            # If batch argument is string
            if isinstance(batch, str):
                # Check for batch with same name
                for batch_element in batches_list:
                    if batch_element.name == batch:
                        variables.eyes.batch = batch_element
                        break
                # If a batch with this name is not yet on the list
                if variables.eyes.batch is None:
                    new_batch = BatchInfo(batch)
                    variables.eyes.batch = new_batch
                    variables.batches.append(new_batch)
            # If batch argument is BatchInfo
            else:
                # Check for batch with same name and date
                for batch_element in batches_list:
                    if (
                        batch_element.name == batch.name
                        and batch_element.started_at == batch.started_at
                    ):
                        variables.eyes.batch = batch_element
                        break
                # If the list doesn't contain a batch with the same name and date
                if variables.eyes.batch is None:
                    variables.eyes.batch = batch
                    variables.batches.append(batch)

        if matchlevel is not None:
            variables.eyes.match_level = utils.get_match_level(matchlevel)
        if parentbranch is not None:
            variables.eyes.parent_branch_name = parentbranch
        if branchname is not None:
            variables.eyes.branch_name = branchname
        if osname is not None:
            variables.eyes.host_os = osname
        if stitchmode is not None:
            variables.eyes.stitch_mode = utils.get_stitch_mode(stitchmode)
        if matchtimeout is not None:
            variables.eyes.match_timeout = int(matchtimeout)
        if force_full_page_screenshot is not None:
            variables.eyes.force_full_page_screenshot = force_full_page_screenshot
        if save_new_tests is not None:
            variables.eyes.save_new_tests = save_new_tests
        if wait_before_screenshots is not None:
            variables.eyes.wait_before_screenshots = int(wait_before_screenshots)
        if send_dom is not None:
            variables.eyes.send_dom = send_dom
        if stitchcontent is not False:
            variables.stitchcontent = stitchcontent

        if width is None and height is None:
            variables.driver = variables.eyes.open(driver, appname, testname)
        else:
            variables.driver = variables.eyes.open(
                driver, appname, testname, {"width": int(width), "height": int(height)}
            )

        # Workaround - This property has to be called after opening session
        # Otherwise, the checks will throw exceptions
        if isdisabled is not None:
            variables.eyes.is_disabled = isdisabled

    def close_eyes_session(
        self, enable_eyes_log=None, enable_http_debug_log=None, raise_exception=True, 
    ):
        """
        Closes a session and returns the results of the session.
        If a test is running, aborts it. Otherwise, does nothing.

            | =Arguments=                  | =Description=                                                                                                           |
            | Enable Eyes Log (bool)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable                                 |
            | Enable HTTP Debug Log (bool) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable                           |
            | Raise Exception (bool)       | If you don't want an exception to be thrown if there are new, missing or mismatched steps, pass 'False' in the variable |

        *Example:*
            | Close Eyes Session | ${false} |                                 
        """
        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        variables.eyes.close(raise_exception)
        variables.eyes.abort_if_not_closed()

        utils.manage_logging(False, False)

    def abort_eyes_session_if_not_closed(
        self, enable_eyes_log=None, enable_http_debug_log=None
    ):
        """
        Stops execution without calling close(). 
        This method does all the cleanup normally done by close.
        If this method is called, and close has not been called, then the test will have a status of Aborted in the Test Manager.

            | =Arguments=                  | =Description=                                                                                 |
            | Enable Eyes Log (bool)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable       |
            | Enable HTTP Debug Log (bool) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable |

        *Example:*
            | Abort Eyes Session If Not Closed |                             
        """
        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        variables.eyes.abort_if_not_closed()

        utils.manage_logging(False, False)

    def eyes_session_is_open(self):
        """
        Returns True if an Applitools Eyes session is currently running, otherwise it will return False.
          
        *Example:*
            | ${isOpen}= | Eyes Session Is Open |                    
        """

        return variables.eyes.is_open

    def add_eyes_property(self, name, value):
        """
        Adds a custom key name/value property that will be associated with the session.
        You can view these properties and filter and group by these properties in the [https://eyes.applitools.com/app/test-results/|Test Manager]
        Make sure to use this keyword right after `Open Eyes Session`.

            | =Arguments= | =Description=                      |
            | Name (str)  | The name of the property           |
            | Value (str) | The value associated with the name |

        *Example:*
            | Add Eyes Property | Language | PT |                         
        """

        variables.eyes.add_property(name, value)

    def get_viewport_size(self, enable_eyes_log=None, enable_http_debug_log=None):
        """
        Retrieves the value that was set for the viewport.

            | =Arguments=                  | =Description=                                                                                 |
            | Enable Eyes Log (bool)       | The Eyes logs will not be included by default. To activate, pass 'True' in the variable       |
            | Enable HTTP Debug Log (bool) | The HTTP Debug logs will not be included by default. To activate, pass 'True' in the variable |

        *Example:*
            | ${size}= | Get Viewport Size |                  
        """
        logging_properties = utils.save_current_logging_properties()
        utils.manage_logging(enable_eyes_log, enable_http_debug_log)

        viewport_size = variables.eyes.get_viewport_size()

        utils.manage_logging(**logging_properties)
        return viewport_size

    def create_eyes_batch(self, name=None, started_at=None, batch_id=None):
        """
        Returns a BatchInfo object that may be used as batch argument on `Open Eyes Session`. For more information, read `Group tests into batches`.

            | =Arguments=                  | =Description=                                                                              |
            | Name (str)                   | The name of the batch                                                                      |
            | Started At (str or datetime) | The date and time that will be displayed in the Test Manager as the batch start time *(*)* |
            | Batch ID (str)               | This argument groups together tests ran in different executions                            |

        The *Started At* argument may be passed as:
        - String: YYYY-mm-dd HH:MM:SS
        - Datetime variable: See [https://robotframework.org/robotframework/latest/libraries/DateTime.html|DateTime library]

        *(*)* Currently, due to a problem with Eyes, the Test Manager always shows the default batch start time, even when setting a custom one.

        *Example:*
            | ${batch}= | Create Eyes Batch |      
        """

        if started_at is not None:
            if type(started_at) is six.text_type:
                started_at = str(started_at)

            if isinstance(started_at, str):
                started_at = datetime.strptime(started_at, "%Y-%m-%d %H:%M:%S")

        if name is not None and started_at is not None:
            batch = BatchInfo(name, started_at)
        elif name is not None:
            batch = BatchInfo(name)
        elif started_at is not None:
            batch = BatchInfo(None, started_at)
        else:
            batch = BatchInfo()

        if batch_id is not None:
            batch.id = batch_id
        return batch

    def get_eyes_property(self, name):
        """
        Returns the value of a given variable of Eyes. For a list of Eyes properties, consult [https://applitools.com/docs/api/eyes-sdk/index-gen/class-eyes-selenium-python.html|Eyes Documentation]

            | =Arguments= | =Description=            |
            | Name (str)  | The name of the variable |
      
        *Example:*
            | ${value}= | Get Eyes Property | send_dom |      
        """
        return vars(variables.eyes)[name]

