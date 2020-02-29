#coding=utf-8

from bilibili import User
from bilibili import Video
from bilibili import MySql

import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 300)
pd.set_option('display.max_colwidth', 30)

rootPath=r'./'


class BiliBili():
    def __init__(self):
        self.user=User()
        self.video = Video()
        self.mysql=MySql()
    # 下载更新用户数据表
    def user_update(self):
        self.user.Imatate()
    # 下载更新视频数据表
    def video_update(self):
        self.video.Imatate()
    # 导出用户数据表
    def user_export(self):
        df=self.mysql.getdbmysql('user_bilibili')
        return df

# 主程序入口
if __name__ == '__main__':
    mt=BiliBili()
    mt.user_export()




