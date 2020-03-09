# encoding: utf-8
from cdnutil import basepy
headers = {"content-type": "application/json"}

def loadTokenFromDisk(filename):
    try:
        with open(filename, "r") as file:
            return file.readline()
    except:
        # 解决不配置登录情况token获取
        return "test_tk"

def writeTokenToDisk(filename, info):
    try:
        with open(filename, "w") as file:
            file.write(info)
    except:
        pass
