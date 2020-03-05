import allure
from webframework.core.webdriver import WebDriver


def take_screenshot():
    screenshot = WebDriver.get_instance().get_screenshot_as_png()
    allure.attach(screenshot, "Screenshot", allure.attachment_type.PNG, ".png")


def save_page_source():
    page_source = WebDriver.get_instance().page_source
    allure.attach(page_source, "Page source", allure.attachment_type.TEXT)
