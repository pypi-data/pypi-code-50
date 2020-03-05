from webframework.core.webdriver import WebDriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element(object):

    def __init__(self):
        self._driver = WebDriver().get_instance()
        self._wait = WebDriverWait(self._driver, 10)

    def _get(self, locator, with_wait=False, wait=None):
        tries = 3
        element = None
        while tries:
            try:
                if with_wait is False:
                    element = self._driver.find_element(*locator)
                else:
                    element = self._wait.until(EC.presence_of_element_located(locator))
            except StaleElementReferenceException as e:
                print(e)

            tries = tries-1

        return element

    def _exists(self, locator, wait=None):
        status = False
        try:
            if wait is None:
                status = self._get(locator) is not None
            else:
                status = wait.until(EC.visibility_of_element_located(locator)) is not False
        except NoSuchElementException as e:
            print(e)
        except WebDriverException as e:
            print(e)

        return status


class WebElement(Element):

    def __init__(self, locator, wait_driver=None):
        super().__init__()
        self._locator = locator
        if wait_driver is None:
            self._wait_driver = self._wait
        else:
            self._wait_driver = wait_driver

    def get_tag_name(self):
        return self._get(self._locator).tag_name

    def get_text(self):
        return self._get(self._locator).text

    def click(self):
        self._get(self._locator).click()

    def submit(self):
        self._get(self._locator).submit()

    def clear(self):
        self._get(self._locator).clear()

    def get_property(self, name):
        return self._get(self._locator).get_property(name)

    def get_attribute(self, name):
        return self._get(self._locator).get_attribute(name)

    def is_selected(self):
        return self._get(self._locator).is_selected()

    def is_enabled(self):
        return self._get(self._locator).is_enabled()

    def is_displayed(self):
        return self._exists(self._locator, self._wait_driver)

    def send_keys(self, *value):
        self._get(self._locator).send_keys(value)

    def get_size(self):
        return self._get(self._locator).size

    def get_css_value(self, property_name):
        return self._get(self._locator).value_of_css_property(property_name)

    def get_location(self):
        return self._get(self._locator).location

    def get_rect(self):
        return self._get(self._locator).rect
