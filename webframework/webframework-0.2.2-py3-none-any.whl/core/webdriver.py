from selenium import webdriver
from webframework.core.capabilites import Capabilities
from webframework import setting


class WebDriver:
    driver = None
    CHROME = "chrome"
    FIREFOX = "firefox"

    @classmethod
    def get_instance(cls):
        if cls.driver is None:
            cls.create_driver()
        return cls.driver

    @classmethod
    def create_driver(cls):
        browser_name = setting.WEB_BROWSER
        if browser_name == cls.CHROME:
            cls.driver = webdriver.Chrome(executable_path=setting.DRIVER_PATH,
                                          desired_capabilities=Capabilities.get_standard_chrome_capabilities())
        elif browser_name == cls.FIREFOX:
            cls.driver = webdriver.Firefox(executable_path=setting.DRIVER_PATH,
                                           desired_capabilities=Capabilities.get_standard_firefox_capabilities())

        cls.driver.get(setting.URL)

    @classmethod
    def close_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
        cls.driver = None
