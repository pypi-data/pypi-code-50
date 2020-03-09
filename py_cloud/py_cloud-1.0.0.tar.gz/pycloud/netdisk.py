
"""
    百度云盘模块，提供以下特性
        * 登陆主页
        * 管理文件
        * 分享链接和密码，自动保存
        * 保存文件时，自动创建文件夹
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
import json
import random
import os

from tortoises.driver import start_chrome


DEFAULT_COOKIE_PATH = os.path.join(os.environ['HOME'], '.cookies/net_disk.cookie')


def sleep(level: int):
    if level == -1:
        pass
    elif level == 0:
        time.sleep(random.uniform(0, 0.5))
    elif level == 1:
        time.sleep(random.uniform(0.5, 1.5))
    elif level == 2:
        time.sleep(random.uniform(1.5, 2.5))
    elif level == 3:
        time.sleep(random.uniform(2.5, 3.5))
    elif level == 4:
        time.sleep(random.uniform(3.5, 4.5))
    elif level == 5:
        time.sleep(random.uniform(4.5, 5.5))
    else:
        assert level in [-1, 0, 1, 2, 3, 4, 5, ], "level must be range from -1 to 5"


class NetDisk(object):

    def __init__(self, user_name=None, password=None, maximize=True, mode='slow', *args, **kwargs):
        self.driver = start_chrome(*args, **kwargs)
        assert mode in ['slow', 'fast', ], "mode should be either 'slow' or 'fast'"
        self.mode = mode

        self.user_name = user_name
        self.password = password
        self.adjust(refresh=False, maximize=maximize)

    def add_username(self, user_name):
        self.user_name = user_name

    def add_password(self, password):
        self.password = password

    def fetch_home(self):
        print('connecting to < https://pan.baidu.com/ > ...')
        try:
            self.driver.get('https://pan.baidu.com/')
            WebDriverWait(driver=self.driver, timeout=60, poll_frequency=0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//div")))
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 2))
        except TimeoutException:
            print('fail to connect')
            raise TimeoutException
        print('success to connect')

    def login(self):
        assert self.user_name and self.password, 'user_name and password can\'t not be empty !'
        self.fetch_home()
        print('login ...')
        try:
            selector = self.driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn')
            self.driver.execute_script('arguments[0].click()', selector)
            WebDriverWait(driver=self.driver, timeout=60, poll_frequency=0.5).until(
                expected_conditions.presence_of_element_located((By.ID, "TANGRAM__PSP_4__userName", )))
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 2))
            self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys(self.user_name)
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 2))
            self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys(self.password)
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 2))
            selector = self.driver.find_element_by_id('TANGRAM__PSP_4__submit')
            self.driver.execute_script('arguments[0].click()', selector)
            WebDriverWait(driver=self.driver, timeout=60, poll_frequency=0.5).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, "user-name")))
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 2))
        except NoSuchElementException:
            print('fail to login')
            pass
        print('success to login\n')
        self.remove_advertise()
        self.display_account_info()
        self.dir_list()

    def manual_login(self):
        self.driver = start_chrome(headless=False, limit=False, delete_cookies=True, )
        self.fetch_home()

    def save_cookie(self, cookie_path=DEFAULT_COOKIE_PATH):
        # save cookie
        if not os.path.exists(os.path.dirname(cookie_path)):
            os.makedirs(cookie_path)
        print(f'saving cookies to path < {cookie_path} >')
        with open(cookie_path, 'a+') as f:
            f.write(json.dumps(self.driver.get_cookies()))

    def login_with_cookie(self, cookie_path=DEFAULT_COOKIE_PATH):
        assert cookie_path, 'cookie path can\'t not be empty !'
        self.fetch_home()
        # add cookie
        print(f'loading cookies from path < {cookie_path} >')
        with open(cookie_path, 'r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                if isinstance(cookie.get('expiry'), float):
                    cookie['expiry'] = int(cookie['expiry'])
                self.driver.add_cookie(cookie)
        self.adjust(refresh=True, maximize=False)
        self.remove_advertise()
        self.display_account_info()
        self.dir_list()

    def adjust(self, refresh: bool, maximize: bool):
        # refreshing browser
        if refresh:
            try:
                self.driver.refresh()
                WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5).until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME, "user-name")))
                time.sleep(random.uniform(1, 2))
                print('success to login')
            except TimeoutException:
                pass
        # maximizing browser window
        if maximize:
            self.driver.maximize_window()
            time.sleep(random.uniform(1, 2))

    def display_account_info(self):
        try:
            print(f"user_name: {self.driver.find_element_by_class_name('user-name').text}")
            print(f"space: {self.driver.find_element_by_class_name('remaining-space').text}")
        except NoSuchElementException:
            pass

    def save(self, url, pwd=None, save_path='.', verbose=True):

        try:
            if verbose:
                if pwd:
                    print(f'saving info: '
                          f'\n\tnet cloud disk link: {url}'
                          f'\n\tverification code: {pwd}'
                          f'\n\tsaving directory: \'{save_path}\'')
                else:
                    print(f'saving info: '
                          f'\n\tnet cloud disk link: {url}'
                          f'\n\tsaving directory: \'{save_path}\'')
            # get url
            self.driver.get(url)
            WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//input")))
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 2))

            if pwd:
                # input password
                self.driver.find_element_by_xpath('//input').send_keys(pwd)
                if self.mode == 'slow':
                    time.sleep(random.uniform(0.5, 1))

                # click
                selector = self.driver.find_element_by_class_name('g-button-right')
                self.driver.execute_script('arguments[0].click()', selector)
                WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5).until(
                    expected_conditions.presence_of_element_located((By.XPATH, "//div[@node-type='fydGNC']")))
                if self.mode == 'slow':
                    time.sleep(random.uniform(1, 3))

            # select all
            selector = self.driver.find_element_by_xpath("//div[@node-type='fydGNC']")
            self.driver.execute_script('arguments[0].click()', selector)
            if self.mode == 'slow':
                time.sleep(random.uniform(0.5, 1))

            # save
            selector = self.driver.find_element_by_class_name('g-button')
            self.driver.execute_script('arguments[0].click()', selector)
            WebDriverWait(driver=self.driver, timeout=100, poll_frequency=0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='file-tree-container']")))
            if self.mode == 'slow':
                time.sleep(random.uniform(1, 3))

            # choose path to save (new version)
            element = None
            elements = self.driver.find_element_by_xpath(
                "//*[@id='fileTreeDialog']/div[2]/div/ul/li"
            )

            for dir_name in save_path.split('/'):
                if dir_name:
                    flag = False
                    for element in elements.find_elements_by_xpath('ul/li'):
                        if element.text.split('\n')[0] == dir_name:
                            flag = True
                            break
                    if not flag:
                        selector = self.driver.find_element_by_xpath("//span/em[@title='新建文件夹']")
                        self.driver.execute_script('arguments[0].click()', selector)
                        if self.mode == 'slow':
                            time.sleep(random.uniform(3.5, 4.5))
                        self.driver.find_element_by_xpath("//input[@value='新建文件夹']").send_keys(dir_name)
                        if self.mode == 'slow':
                            time.sleep(random.uniform(0.5, 1.5))
                        self.driver.find_element_by_class_name('shareFolderConfirm').click()
                        if self.mode == 'slow':
                            time.sleep(random.uniform(2.5, 3.5))
                        for element in elements.find_elements_by_xpath('ul/li'):
                            if element.text.split('\n')[0] == dir_name:
                                break
                    if 'treeview-collapse' in element.find_element_by_xpath('ul').get_attribute('class'):
                        element.click()
                        time.sleep(random.uniform(1, 3))
                    elements = element

            """
            # choose path to save (old version)
            selector = self.driver.find_element_by_xpath(
                f"//div[@class='file-tree-container']/ul/li/ul/li//*[text()='{save_path}']"
            )
            self.driver.execute_script('arguments[0].click()', selector)
            time.sleep(random.uniform(1, 3))
            """

            selector = self.driver.find_element_by_xpath("//a[@title='确定']")
            self.driver.execute_script('arguments[0].click()', selector)

            if self.mode == 'slow':
                time.sleep(random.uniform(1, 3))

            if '已为您成功保存文件' in self.driver.page_source:
                if verbose:
                    print('success to save')
                    print('\n' + '-' * 50)
        except Exception as e:
            print(e)

    def close(self):
        self.driver.close()

    def dir_list(self):
        try:
            dir_names = [element.text for element in self.driver.find_elements_by_xpath(
                "//div[@class='vdAfKMb']/dd/div[@class='file-name']")]
            if dir_names:
                print('user directory: ', end='')
                for dir_name in dir_names:
                    if dir_name not in ['已购资源', '我的卡包', '我的应用数据'] and dir_name:
                        print(f'{dir_name}', end='\t')
                print('\n' + '-'*50)
        except NoSuchElementException:
            pass

    def _dir_exist(self, dir_name):
        selector = None
        try:
            selector = self.driver.find_element_by_xpath(
                f"//div[@class='vdAfKMb']/dd/div[@class='file-name']//div[@class='text']//*[text()='{dir_name}']"
            )
        except NoSuchElementException:
            pass
        return selector

    def _dir_select(self, dir_name):
        selector = self._dir_exist(dir_name)
        if selector:
            self.driver.execute_script('arguments[0].click()', selector)
            time.sleep(random.uniform(0.5, 1))

    def make_dir(self, dir_name):
        selector = self._dir_exist(dir_name)
        if not selector:
            selector = self.driver.find_element_by_xpath("//a[@title='新建文件夹']")
            self.driver.execute_script('arguments[0].click()', selector)
            time.sleep(random.uniform(0.5, 1.5))
            self.driver.find_element_by_class_name('GadHyA').send_keys(dir_name)
            time.sleep(random.uniform(0.5, 1.5))
            selector = self.driver.find_element_by_class_name('awrgLl')
            self.driver.execute_script('arguments[0].click()', selector)
            time.sleep(random.uniform(0.5, 1.5))

    def make_path(self, path):
        dirs = path.split('/')
        for step in range(len(dirs)):
            self.make_dir(dirs[step])
            if step < len(dirs):
                self._dir_select(dirs[step])

    def remove_advertise(self):
        try:
            selector = self.driver.find_element_by_class_name('know-button')
            self.driver.execute_script('arguments[0].click()', selector)
        except NoSuchElementException:
            pass


if __name__ == '__main__':

    # from pycloud.util import gnr_path
    # from tqdm import tqdm

    """
    # get cookie
    nd = NetDisk()
    nd.manual_login()
    # login manually and save
    nd.save_cookie(cookie_path='cookies/net_disk.cookie')
    """

    # nd = NetDisk(mode='slow')
    # nd.login_with_cookie()
    #
    # items = [
    #     ('https://pan.baidu.com/s/1NxtrD9QbONy0xRxqXut5Bw', '8irj'),
    #     ('https://pan.baidu.com/s/1YJw9auKFnKMSeJaYb1PJTg', 'mqxz'),
    #     ('https://pan.baidu.com/s/17YYdXFyHjVAvbka0J2BFug', 'f8aa'),
    #     ('https://pan.baidu.com/s/1010Vnz9YZq6ygcsawKqiPw', 'fw38'),
    #     ('https://pan.baidu.com/s/1T4Chc6h14NOWLPSQI7VVQw', '7tuk'),
    #     ('https://pan.baidu.com/s/1tvDg7beobRmmFgtLP0zgXQ', 'a9z2'),
    #     ('https://pan.baidu.com/s/11-cMUa52HGoP_B13yDKhCw', 'p7da'),
    # ]
    #
    # for url, pwd in tqdm(items):
    #     nd.save(url=url, pwd=pwd, save_path=gnr_path(), verbose=False)
    pass
