import os
import selenium
from selenium import webdriver
import webdrivermanager as wdm
from colorama import Fore as F
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class InvalidInput(Exception):
    pass


class NotFound(Exception):
    pass


def wait(driver, timeout=5):
    '''
    Instantiates an implicit wait object, given the WebDriver and timeout. 

    wait : (*driver:WebDriver, timeout:anyof int/float) => WebDriverWait

    Required args indicated by *

    Example:

    front_end_wait = wait(chrome_driver, timeout=7)

    try:
        login_field = front_end_wait.until(d.find_element_by_id('Login'))
    except:
        pprint('Login field not found', 'f', 1)
    '''
    return WebDriverWait(driver, timeout)


def p_print(s, n=0, toc=None):
    '''
    Pretty Print for the Command Line output. 
    Helps make the output visually appealing and easily understandable.

    p_print : (*s:str, n:int, toc:str) => stdout

    Required args indicated by *

    s -> String to print

    n -> Indent level

    toc -> Status token

    Use the tokens "s", "f" to denote 'Success' and 'Failure' respectively.
    The token 's' prints the variable s to stdout with indent level n, in green text. 
    The token 'f' does the same, except uptupts red text. 
    Token 'info' outputs yellow text to stdout.
    Other tokens can be used for improving code readability. 
    '''
    s = str(s)
    if toc == None:
        print(F.WHITE + "     "*n + "$ " + s + F.WHITE)
    elif toc == "s":
        print(F.GREEN + "     "*n + "$ " + s + F.WHITE)
    elif toc == "f":
        print(F.RED + "     "*n + "$ " + s + F.WHITE)
    elif toc == "info":
        print(F.YELLOW + "     "*n + "$ " + s + F.WHITE)


def browser_init(browser_name, ops=[], exp_ops=[], headless_download=False):
    '''
    browser_init : (browser_name:str, ops:list, exp_ops:list, headless_download:bool) => WebDriver

    browser_name -> One of the following strings: 
    "firefox", "chrome", "edge","gecko", "opera_chromium", "opera".
    If the browser_name is not valid, an InvalidInput error is raised.

    ops -> Optional arguments can be provided as strings in a list. (e.g. ['headless'])

    exp_ops -> Similar to ops, this is for experimental options.

    Returns a webdriver which can be controlled with Selenium.

    By default, all downloads are in the current directory.
    The download directory will be printed to the stdout upon browser initiation.

    USAGE:

    `driver = init_browser("chrome")`

    `driver = init_browser('chrome', ops=['headless', 'verbose'])`
    '''
    abs_path = os.path.abspath(os.path.curdir)
    print(f"Download Directory path: {abs_path}")
    browsers = ["firefox", "chrome", "edge",
                "gecko", "opera_chromium", "opera"]
    bn = browser_name.lower()
    if bn not in browsers:
        p_print('The browser you have requested may not be supported.', toc='f')
        raise InvalidInput("Unrecognized Browser.")
    if bn == 'chrome':
        chrome_ops = selenium.webdriver.chrome.options.Options()
        service_args = []
        chrome_ops.add_experimental_option(
            'prefs', {'download.default_directory': f'{abs_path}'})
        if ops != []:
            for arg in ops:
                chrome_ops.add_argument(f'--{arg}')
        if exp_ops != []:
            for arg in exp_ops:
                chrome_ops.add_experimental_option(arg[0], arg[1])
        cdm = wdm.ChromeDriverManager
        driver = webdriver.Chrome(
            executable_path=f'{cdm().download_and_install()[0]}', chrome_options=chrome_ops, service_args=service_args)
        if headless_download:
            _chrome_headless_download(driver, abs_path)
        return driver
    elif bn == 'edge':
        edm = wdm.EdgeDriverManager
        return webdriver.Edge(executable_path=f'{edm().download_and_install()[0]}')
    elif bn == 'gecko' or 'firefox':
        gdm = wdm.GeckoDriverManager
        return webdriver.Firefox(executable_path=f'{gdm().download_and_install()[0]}')
    ocdm = wdm.OperaChromiumDriverManager
    return webdriver.Opera(executable_path=f'{ocdm().download_and_install()[0]}')


def _chrome_headless_download(driver, download_dir):
    '''
    Allows the browser to download in headless mode.    
    Requires chrome version 62.0.3196.0 or above.
    '''
    driver.command_executor._commands['send_command'] = (
        'POST', '/session/$sessionId/chromium/send_command')
    driver.execute('send_command',
                   {'cmd': 'Page.setDownloadBehavior',
                    'params': {
                        'behavior': 'allow',
                        'downloadPath': download_dir
                    }
                    })


def user_exit(driver):
    '''
    user_exit prompts the user to exit the test.  
    Note that this will close the driver (if 'y' is chosen).
    If 'n' is selected, the driver is left open, but the test is ended. 

    USAGE:
    U_exit(driver)
    '''
    stat = False
    while not stat:
        print('\n\n')
        p_print('Exit? (y/n/h)')
        p_print('If not, you will have to quit the driver manually.')
        uIN = input('>  ').strip()
        if uIN == 'y':
            driver.close()
            stat = True
        elif uIN == 'n':
            stat = True
            break
