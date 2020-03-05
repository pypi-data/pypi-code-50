from selenium import webdriver


class Capabilities:
    @staticmethod
    def get_standard_chrome_capabilities():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--lang=es")
        options.add_argument("incognito")
        chrome_capabilities = options.to_capabilities()
        return chrome_capabilities

    @staticmethod
    def get_standard_firefox_capabilities():
        pass
