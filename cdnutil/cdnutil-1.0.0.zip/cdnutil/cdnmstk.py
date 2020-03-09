# encoding: utf-8
import threading
import time
import requests
import json
import traceback
from cdnutil import config
from cdnutil.Log import Logger
from cdnutil import common
from cdnutil import basepy
logger = Logger(__name__).getLogger()
headers = {"content-type": "application/json"}

# class Token:
    # __lock = threading.RLock()
    # __token = None
    # __createTime = -1
    # __lastTouchTime = -1
    #
    #
    # def getToken(self):
    #     # python3.x可以使用timeout
    #     # Token.__lock.acquire(timeout=30)
    #     Token.__lock.acquire()
    #     logger.info("acquire thread: " + threading.currentThread().getName())
    #     # time.sleep(5)
    #     # logger.info("sleep haole")
    #     try:
    #         tk_expire = int(config.getPropertyValue("cdn_tk_expire"))
    #         # 如果不存在token，或者token已经过期，直接生成
    #         if Token.__token is None or (Token.__createTime != -1 and (time.time() - Token.__createTime >= tk_expire)):
    #             token = self.__refreshToken__()
    #             if token is not None:
    #                 Token.__token = token
    #                 Token.__createTime = time.time()
    #                 Token.__lastTouchTime = Token.__createTime
    #                 return Token.__token
    #
    #         # 直接返回token
    #         Token.__lastTouchTime = time.time()
    #         return Token.__token
    #     finally:
    #         Token.__lock.release()
    #         logger.info("release thread: " + threading.currentThread().getName())
    #
    # def __refreshToken__(self):
    #     # python3.x可以使用timeout
    #     # Token.__lock.acquire(timeout=30)
    #     Token.__lock.acquire()
    #     try:
    #         rsaKey = self.__getRsaInfo__()
    #         if rsaKey is None:
    #             logger.warning("rsa is None")
    #             return None
    #
    #         token = self.__loginBackstage__(rsaKey)
    #         if token is None:
    #             logger.warning("login failed")
    #             return None
    #         return token
    #     except Exception as e:
    #         logger.warning("refreshToken error")
    #         trace = traceback.format_exc()
    #         logger.error(trace)
    #     finally:
    #         Token.__lock.release()
    #
    # def __getRsaInfo__(self):
    #     """
    #     每次操作之前，去后台获取rsa key
    #     :return: 成功返回key， 失败返回None
    #     """
    #     url = config.getPropertyValue("cdnms_location") + "/" + config.getPropertyValue("rsa_servlet")
    #     logger.info(" url = {}".format(url))
    #     result = requests.get(url)
    #     logger.info(" url = {}, result = {}".format(url, result))
    #     if result is None or result.text is None:
    #         logger.warning("rsa is None")
    #         return None
    #
    #     logger.info(" url = {}, result = {}".format(url, result.text))
    #     if json.loads(result.text).get("code") == "0":
    #         return json.loads(result.text).get("data")
    #
    #     return None
    #
    # def __loginBackstage__(self, rsaInfo):
    #     """
    #     登陆后台，获取操作token
    #     :param rsaInfo: 在rsa获取接口返回
    #     :return: 登陆成功返回token，失败返回None
    #     """
    #     url = config.getPropertyValue("cdnms_location") + "/" + config.getPropertyValue("login_servlet")
    #     password = None
    #     if basepy.getPyVer().startswith("2"):
    #         password = str(common.base64str(config.getPropertyValue("cdn_pwd"), common.str2key(rsaInfo.get("key"))))
    #     else:
    #         # 指定encoding，只有python3.x才有，2.7环境不能指定
    #         password = str(common.base64str(config.getPropertyValue("cdn_pwd"), common.str2key(rsaInfo.get("key"))), encoding="utf-8")
    #
    #     data = json.dumps({
    #         "username": config.getPropertyValue("cdn_usr"),
    #         "password": password,
    #         "keyId": rsaInfo.get("id")
    #     })
    #     headers = {
    #         "X-Requested-With": "XMLHttpRequest",
    #         "content-type": "application/json"
    #     }
    #     logger.info(" url = {}, data = {}, headers = {}".format(url, data, headers))
    #     result = requests.post(url=url, data=data, headers=headers)
    #     logger.info(" url = {}, result = {}".format(url, result))
    #
    #     if result is None or result.text is None:
    #         logger.warning("login result is None")
    #         return -1
    #
    #     logger.info(" url = {}, result = {}".format(url, result.text))
    #     try:
    #         tmpO = json.loads(result.text)
    #         if tmpO.get("code") == "0" or tmpO.get("code") == 0:
    #             return tmpO.get("data").get("token")
    #
    #         logger.warning("get access token faild, reason: " + tmpO.get("msg"))
    #         return None
    #     except:
    #         logger.warning("parse login result info failed")
    #         return None

def loadTokenFromDisk(filename):
    with open(filename, "r") as file:
        return file.readline()

def writeTokenToDisk(filename, info):
    with open(filename, "w") as file:
        file.write(info)
