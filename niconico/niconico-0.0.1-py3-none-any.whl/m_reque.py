#coding=utf-8


import random
import time
import requests
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
from datetime import timedelta
from bilibili import info


rootPath=r'./'


class MyReque():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.cachePool={}
        self.stamp = self.utc2local(self.local2utc(datetime.now())).strftime('%Y%m%d')  # #北京时区时间戳转换为字符串
        self.cookie=requests.cookies.RequestsCookieJar()
        self.session = requests.session()

    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam
        self.cookie.set("cookie", info.loginCookie)
        self.session.cookies.update(self.cookie)

    def requests_url(self, url, data=None):
        url = url if data is None else url+parse.urlencode(data)
        url = url.replace('%2C', ',').replace('%3A', ':').replace('%2B', '+')
        return url
    # 发送Get请求
    def requests_get(self, url, data=None):
        try:
            # url = url if data is None else url+parse.urlencode(data)
            # # url = url.replace('%2C', ',').replace('%3A', ':').replace('%2B', '+')
            # if url in self.cachePool.keys():
            #     print('cache:')
            #     return self.cachePool[url]
            time.sleep(random.random() * 0 + 0.1)  # 0-1区间随机数
            #没有缓存就开始抓取
            # print(self.urls['proxies']['https'] + ' --> ' + url)
            response = self.session.get(url=url, headers=self.headers, timeout=3)
            # self.session.keep_alive = False
            # response = self.session.get(url, proxies=self.urls['proxies'], timeout=10)
            # response.encoding = 'utf-8'
            value = response if response.status_code == requests.codes.ok else None
        except:
            value = None
        finally:
            return value
    # 保存htmlPage
    def write_html_page(self, path, page):
        f=open(path, 'w')
        f.write(page.encode('utf-8').decode('utf-8'))
        f.close()
    # 读取htmlPage
    def read_html_page(self, path):
        f = open(path, 'r')
        page=f.read().encode('utf-8').decode('utf-8')
        f.close()
        return page
    # UTC转本地（北京）
    def utc2local(self, utc_st):
        offset = timedelta(hours=8)
        local_st = utc_st + offset
        return local_st
    # 本地转UTC
    def local2utc(self, local_st):
        time_struct = time.mktime(local_st.timetuple())
        utc_st = datetime.utcfromtimestamp(time_struct)
        return utc_st
    # 字符串转换成datetime
    def strptime(self, str):
        return datetime.strptime(str, '%Y-%m-%d')
    # datetime转换为字符串
    def strftime(self, time):
        return time.strftime('%Y%m%d')

    # 获取代理ip
    def get_iplist(self,url):
        headers={
            'User-Agent':info.loginHeaders['User-Agent']
        }
        page=requests.get(url, headers=headers)
        soup=BeautifulSoup(page.text,'lxml')
        trs=soup.find_all('tr')
        ip_list = []
        for tr in trs[1:]:
            tds=tr.find_all('td')
            ip_list.append(tds[1].text+':'+tds[2].text)
        return ip_list
    # 切换ip代理
    def switchProxy(self):
        proxy_ip=random.choice(self.get_iplist(self.urls['proxyWeb']))
        # self.urls['proxies']['http']='http://' + proxy_ip
        self.urls['proxies']['https'] = 'https://' + proxy_ip

    def getStamp(self):
        return self.utc2local(self.local2utc(datetime.now())).strftime('%Y%m%d')


# 主程序入口
if __name__ == '__main__':
    print('TS:' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


