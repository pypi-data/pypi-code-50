# Copyright (C) 2019 Spiralworks Technologies Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import warnings

from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.utils import LibraryListener, timestr_to_secs, is_truthy
from SeleniumLibrary.base import DynamicCore, keyword
from SeleniumLibrary.locators import ElementFinder
from SeleniumLibrary.keywords import (
    AlertKeywords,
    BrowserManagementKeywords,
    CookieKeywords,
    ElementKeywords,
    FormElementKeywords,
    FrameKeywords,
    JavaScriptKeywords,
    RunOnFailureKeywords,
    ScreenshotKeywords,
    SelectElementKeywords,
    TableElementKeywords,
    WaitingKeywords,
    WebDriverCache,
    WindowKeywords
)
from PIL import Image


# force override warn method
# ignore the warning for capture page keyword
# since we are re-writing the png file to jpg
# this will suppress the warning message
def _new_warn(message, category=None, stacklevel=1, source=None):
    if str(message) == "name used for saved screenshot does not \
            match file type. It should end with a `.png` extension":
        return

    old_warn(message, category, stacklevel, source)


old_warn = warnings.warn
setattr(warnings, "warn", _new_warn)


class ScreenshotExtensionKeywords(ScreenshotKeywords):

    @keyword
    def element_capture_screenshot(self, locator, *options):
        """
        Takes a screenshot of an element and embeds it into the log.

        *Example:*
        | Element Capture Screenshot | css=#element |
        | Element Capture Screenshot | css=#element | style=grayscale |
        """
        self.capture_element_screenshot(locator)

    @keyword
    def capture_page(self, filename='selenium-screenshot-{index}.jpg'):
        """
        Takes a screenshot of the current page and embeds it into a log file.

        ``filename`` argument specifies the name of the file to write the
        screenshot into. The directory where screenshots are saved can be
        set when `importing` the library or by using the `Set Screenshot
        Directory` keyword. If the directory is not configured, screenshots
        are saved to the same directory where Robot Framework's log file is
        written.

        Starting from SeleniumLibrary 1.8, if ``filename`` contains marker
        ``{index}``, it will be automatically replaced with an unique running
        index, preventing files to be overwritten. Indices start from 1,
        and how they are represented can be customized using Python's
        [https://docs.python.org/3/library/string.html#format-string-syntax|
        format string syntax].

        An absolute path to the created screenshot file is returned.

        Examples:
        | `Capture Page`            |                                        |
        | `File Should Exist`       | ${OUTPUTDIR}/selenium-screenshot-1.jpg |
        | ${path} =                 | `Capture Page`              |
        | `File Should Exist`       | ${OUTPUTDIR}/selenium-screenshot-2.jpg |
        | `File Should Exist`       | ${path}                                |
        | `Capture Page`            | custom_name.jpg                        |
        | `File Should Exist`       | ${OUTPUTDIR}/custom_name.jpg           |
        | `Capture Page`            | custom_with_index_{index}.jpg          |
        | `File Should Exist`       | ${OUTPUTDIR}/custom_with_index_1.jpg   |
        | `Capture Page`            | formatted_index_{index:03}.jpg         |
        | `File Should Exist`       | ${OUTPUTDIR}/formatted_index_001.jpg   |
        """

        # this will save png file content in a jpg file name
        # this is needed in order for robot report to reflect proper filename
        return_path = self.capture_page_screenshot(filename)

        # converts file content from png to jpg
        im = Image.open(return_path)
        rgb_im = im.convert('RGB')
        rgb_im.save(return_path)

        return return_path


class WaitingExtensionKeywords(WaitingKeywords):

    @keyword
    def wait_until_location_is(self, expected, timeout=None, case_sensitive=True, message=None):
        """Waits until the current URL is ``expected``.

        Ignores case when ```case_sensitive``` is False (default is True).

        The ``expected`` argument is the expected value in url.

        Fails if ``timeout`` expires before the location is. See
        the `Timeouts` section for more information about using timeouts
        and their default value.

        The ``message`` argument can be used to override the default error
        message.

        New in SeleniumLibrary 4.0
        """

        current_url = self.driver.current_url().lower() if not case_sensitive \
            else self.driver.current_url
        expected_url = str(expected).lower() if not case_sensitive else str(expected)
        self._wait_until(lambda: expected_url == current_url,
                         "Location did not is '%s' in <TIMEOUT>." % expected,
                         timeout, message)


class SeleniumExtensionLibrary(SeleniumLibrary):
    # use the same doc as SeleniumLibrary
    __doc__ = "SeleniumExtensionLibrary is SeleniumLibrary extension.\n" + SeleniumLibrary.__doc__

    def __init__(self, timeout=5.0, implicit_wait=0.0, run_on_failure='Capture Page',
                 screenshot_root_directory=None, plugins=None, event_firing_webdriver=None):
        self.timeout = timestr_to_secs(timeout)
        self.implicit_wait = timestr_to_secs(implicit_wait)
        self.speed = 0.0
        self.run_on_failure_keyword \
            = RunOnFailureKeywords.resolve_keyword(run_on_failure)
        self._running_on_failure_keyword = False
        self.screenshot_root_directory = screenshot_root_directory
        self._element_finder = ElementFinder(self)
        self._plugin_keywords = []
        libraries = [
            AlertKeywords(self),
            BrowserManagementKeywords(self),
            CookieKeywords(self),
            ElementKeywords(self),
            FormElementKeywords(self),
            FrameKeywords(self),
            JavaScriptKeywords(self),
            RunOnFailureKeywords(self),
            ScreenshotExtensionKeywords(self),
            SelectElementKeywords(self),
            TableElementKeywords(self),
            WaitingExtensionKeywords(self),
            WindowKeywords(self)
        ]
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()
        self._running_keyword = None
        self.event_firing_webdriver = None
        if is_truthy(event_firing_webdriver):
            self.event_firing_webdriver = self._parse_listener(event_firing_webdriver)
        self._plugins = []
        if is_truthy(plugins):
            plugin_libs = self._parse_plugins(plugins)
            self._plugins = plugin_libs
            libraries = libraries + plugin_libs
        self._drivers = WebDriverCache()
        DynamicCore.__init__(self, libraries)


# use the same documentation as SeleniumLibrary
SeleniumExtensionLibrary.__init__.__doc__ = SeleniumLibrary.__init__.__doc__
