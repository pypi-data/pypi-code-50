import os
import requests
import json


class ProxyDownloaderMiddleware(object):

    def __init__(self, proxy_server_addr):
        self.proxy_server_addr = proxy_server_addr

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        proxy_server_addr = crawler.spider.settings.get('PROXY_SERVER_ADDR') if crawler.spider.settings.get(
            'PROXY_SERVER_ADDR') else os.environ.get('PROXY_SERVER_ADDR')
        s = cls(proxy_server_addr)
        return s

    def process_request(self, request, spider):

        proxy = self.get_proxy(spider.name, request.url)
        if proxy is not None:
            proxy_server = f"http://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}"
            if 'splash' in request.meta:
                request.meta['splash']['args']['proxy'] = proxy_server
            else:
                request.meta['proxy'] = proxy_server
                request.headers["Proxy-Authorization"] = proxy['basic_auth_header']

        # spider.logger.info(f'request.meta->{request.meta}')
        # spider.logger.info(f'request.headers->{request.headers}')`

        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def get_proxy(self, name, url):

        try:
            response = requests.get(self.proxy_server_addr + f"/get?name={name}&url={url}", timeout=10)
        except Exception as err:
            print(f'error occurred: {err}, spider name: {name}, request url: {url}')
            return None

        resp = response.json()

        return {
            'host': resp['host'],
            'user': resp['user'],
            'pass': resp['pass'],
            'port': resp['port'],
            'type': resp['type'],
            'basic_auth_header': resp['basic_auth_header'],
        }
