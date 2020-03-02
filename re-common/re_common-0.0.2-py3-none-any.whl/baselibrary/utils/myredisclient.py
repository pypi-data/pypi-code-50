import configparser
import os
import sys
import time
import traceback
import warnings

import redis

from re_common.baselibrary import IniConfig


def RedisConnect(configpath, sesc="proxy", encoding="utf-8"):
    """
    连接数据库 通过读取配置文件连接,如果读取配置文件 失败  返回None
    :return:
    """
    dictsall = IniConfig(configpath).get_conf_dict(encoding=encoding)
    dicts = dictsall[sesc]
    RedisHost = dicts['RedisHost']
    RedisPort = dicts['RedisPort']
    RedisDB = dicts['RedisDB']
    RedisKey = dicts['RedisKey']
    try:
        rconn = redis.StrictRedis(host=RedisHost, port=RedisPort, db=RedisDB, decode_responses=True)
    except:
        # 有可能因为网络波动无法连接 这里休眠10秒重连一次  如果还是失败就放弃
        time.sleep(10)
        rconn = redis.StrictRedis(host=RedisHost, port=RedisPort, db=RedisDB, decode_responses=True)
    if rconn:
        return rconn, RedisKey
    return None


def getDataFromRedis(configpath, sesc="proxy"):
    rconn, RedisKey = RedisConnect(configpath, sesc=sesc)
    if rconn:
        rows = rconn.smembers(RedisKey)
        return rows
    else:
        print("redis出现连接错误")
        sys.exit(-1)
