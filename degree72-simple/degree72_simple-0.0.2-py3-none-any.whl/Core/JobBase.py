import datetime
import os
from .Log import Log
from .HttpManager import HttpManager
from .Proxy import Proxy


class JobBase:

    def __init__(self, *args, **kwargs):
        self.run_date = datetime.datetime.now()
        self.init_folder()
        self.log = Log(self.__class__.__name__)
        self.maxHourlyPageView = 600
        self.proxy = None
        self.job_id = 1001
        self.run_id = 1001
        self._proxy_instance = Proxy()

    def init_folder(self):
        if not os.path.exists('Log/'):
            os.mkdir('Log/')

        if not os.path.exists('Data/'):
            os.mkdir('Data/')

    def init_http_manager(self, timeout=30, default_header=False):

        manager = HttpManager(proxy=self._proxy_instance
                              , default_header=default_header
                              , log=self.log
                              , timeout=timeout
                              , max_hourly_page_view=self.maxHourlyPageView
        )

        return manager

    def download_page(self
                      , url
                      , manager
                      , max_retry=10
                      , post_data=None
                      , validate_str_list=None
                      ):

        for _ in range(max_retry):
            resp = self.get_response(url, manager
                                     , max_retry=1
                                     , post_data=post_data)

            if validate_str_list:
                for each in validate_str_list:
                    if resp.text and each in resp.text:
                        return resp.text
                    if resp.content and each in resp.content:
                        return resp.content

    def debug(self):
        return os.getenv('DEBUG', True)

    def get_response(self, url
                     , manager
                     , max_retry=10
                     , post_data=None
                     ):
        retry = 0
        while retry <= max_retry:
            retry += 1
            # When retry big then 1, need be write log
            if retry > 3: manager.retry_log(url)

            resp = manager.download_page(url, post_data=post_data)
            if resp:
                return resp

        self.log.error("Retried all failed", "url => %s post_data => %s" % (url, post_data))
        return resp

    @property
    def LOCALHOST(self):
        # proxy_str = '127.0.0.1:8888'
        proxy_str = '192.168.0.109:8888'
        self._proxy_instance = Proxy(proxy_str)
        return proxy_str

    @property
    def NONE_PROXY(self):
        proxy_str = ''
        self._proxy_instance = Proxy(proxy_str)
        return proxy_str

    @property
    def PROXY_SQUID_US_3(self):
        proxy_str = ''
        self._proxy_instance = Proxy(proxy_str)
        return proxy_str

    @property
    def LOCAL_PROXY_P4(self):
        proxy_str = ''
        self._proxy_instance = Proxy(proxy_str)
        return proxy_str

    @property
    def LOCAL_PROXY_P5(self):
        proxy_str = ''
        self._proxy_instance = Proxy(proxy_str)
        return proxy_str