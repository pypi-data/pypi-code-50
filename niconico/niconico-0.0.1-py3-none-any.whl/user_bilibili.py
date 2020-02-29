#coding=utf-8

import requests
import pandas as pd
from datetime import datetime
from bilibili import info
from bilibili import MyReque
from bilibili import MySql


rootPath=r'./'


class User():
    def __init__(self):
        self.urls = {}                      # 目标网页
        self.headers = {}                   # Get/Post请求头
        self.param = {}
        self.cookie=requests.cookies.RequestsCookieJar()
        self.session = requests.session()

        self.mysql=MySql()
        self.reque=MyReque()
        self.reque.update_info()

    # 从配置文件中更新登录链接信息
    def update_info(self):
        self.urls = info.loginUrls                                                  #http地址
        self.headers = info.loginHeaders
        self.param = info.loginParam
        self.cookie.set("cookie", info.loginCookie)
        self.session.cookies.update(self.cookie)


    def parse_accinfo(self, jsonp):
        try:
            mk = jsonp['data']
            # mid, 名字，性别，头像，签名，排名，级别，生日，硬币，粉丝勋章，描述，是否vip,是否关注
            line = ( mk['mid'], mk['name'], mk['sex'], mk['face'], mk['sign'], mk['rank'], mk['level'], mk['birthday'], mk['coins'], mk['fans_badge'], mk['official']['title'], mk['vip']['status'], mk['is_followed'])
            return line
        except Exception as e:
            print(e)
            return ['' for x in range(0, 13)]
    def parse_upstat(self, jsonp):
        try:
            mk = jsonp['data']
            # 播放量，阅读数，获赞量
            line = ( mk['archive']['view'], mk['article']['view'], mk['likes'])
            return line
        except Exception as e:
            print(e)
            return ['' for x in range(0, 3)]
    def parse_stat(self, jsonp):
        try:
            mk = jsonp['data']
            # 关注人数，粉丝数
            line = ( mk['following'], mk['follower'])
            return line
        except Exception as e:
            print(e)
            return ['' for x in range(0, 2)]
    def parse_navnum(self, jsonp):
        try:
            mk = jsonp['data']
            # 视频数量，专栏数量，相册数量
            line = ( mk['video'], mk['article'], mk['album'])
            return line
        except Exception as e:
            print(e)
            return ['' for x in range(0, 3)]
    def parse_toparc(self, jsonp):
        try:
            mk = jsonp['data']
            # tid, tname, title, desc, view, darmaku, reply, favorite, coin, share, like, dynamic, reason
            line = ( mk['aid'], mk['tname'],mk['title'], mk['desc'], mk['stat']['view'], mk['stat']['danmaku'], mk['stat']['reply'], mk['stat']['favorite'], mk['stat']['coin'], mk['stat']['share'], mk['stat']['like'], mk['dynamic'], mk['reason'])
            return line
        except Exception as e:
            print(e)
            return ['' for x in range(0, 13)]
    def parse_rank(self, jsonp):
        try:
            mk = jsonp['data']
            # 投币人数，总数
            line = ( mk['count'], mk['total_count'])
            return line
        except Exception as e:
            print(e)
            return ['' for x in range(0,2)]


    def crawl_up(self, left, right):
        self.reque.update_info()
        up_cache=self.mysql.getMidfromDB('user_bilibili', left, right)
        # up_cache=[]
        up_pool=range(left, right)
        result=[]
        i=0
        for mid in list(set(up_pool)-set(up_cache)):
            i+=1
            if (i % 100)==0:
                # 播放量，阅读数，获赞量 # 关注人数，粉丝数# 视频数量，专栏数量，相册数量# 视频地址# 专栏地址# 相册地址# 投币人数，总数
                df = pd.DataFrame(data=result,
                                  columns=['mid', '名字','性别','头像','签名','排名','级别','生日','硬币','粉丝勋章','描述','是否vip','是否关注','url_accinfo',
                                           '播放量','阅读数','获赞量','url_upstat','关注人数','粉丝数','url_stat','视频数量','专栏数量','相册数量','url_navnum',
                                           '视频地址','专栏地址','相册地址'])
                self.mysql.save2mysqldb('user_bilibili',df)
                result = []
                print(df)
            try:
                self.param['com']['mid'] = mid
                self.param['vcom']['vmid'] = mid
                self.param['search']['mid'] = mid
                self.param['article']['mid'] = mid
                self.param['album']['mid'] = mid

                upline = self.bilibili_up()
                result.append(upline)
            except:
                continue


    def bilibili_up(self):
        result=[]

        url=self.reque.requests_url(self.urls['accinfo'],self.param['com'])
        # mid, 名字，性别，头像，签名，排名，级别，生日，硬币，粉丝勋章，描述，是否vip,是否关注
        response = self.reque.requests_get(url=url)
        line=self.parse_accinfo(response.json())
        result.extend(line)
        result.append(url)

        url=self.reque.requests_url(self.urls['upstat'],self.param['com'])
        # 播放量，阅读数，获赞量
        response = self.reque.requests_get(url=url)
        line=self.parse_upstat(response.json())
        result.extend(line)
        result.append(url)

        url=self.reque.requests_url(self.urls['stat'],self.param['vcom'])
        # 关注人数，粉丝数
        response = self.reque.requests_get(url=url)
        line=self.parse_stat(response.json())
        result.extend(line)
        result.append(url)

        url=self.reque.requests_url(self.urls['navnum'],self.param['com'])
        # 视频数量，专栏数量，相册数量
        response = self.reque.requests_get(url=url)
        line=self.parse_navnum(response.json())
        result.extend(line)
        result.append(url)

        # 视频地址
        url=self.reque.requests_url(self.urls['search'],self.param['search'])
        result.append(url)
        # 专栏地址
        url=self.reque.requests_url(self.urls['article'],self.param['article'])
        result.append(url)
        # 相册地址
        url=self.reque.requests_url(self.urls['album'],self.param['album'])
        result.append(url)

        '''
        url=self.requests_url(self.urls['rank'],self.param['com'])
        # 投币人数，总数
        response = requests.get(url=url)
        line=self.parse_rank(response.json())
        result.extend(line)
        result.append(url)

        url=self.requests_url(self.urls['toparc'],self.param['vcom'])
        # tid, tname, title, desc, view, darmaku, reply, favorite, coin, share, like, dynamic, reason
        response = self.requests_get(url=url)
        line=self.parse_toparc(response.json())
        result.extend(line)
        result.append(url)
        '''

        return result


    def Imatate(self):
        self.update_info()
        self.crawl_up(400,100000)

# 主程序入口
if __name__ == '__main__':
    spider = User()
    spider.Imatate()


    print('TS:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


