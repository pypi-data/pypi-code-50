# encoding: utf-8
import platform
import sys
if platform.python_version().startswith("2"):
    # python2.7 必须加入
    reload(sys)
    sys.setdefaultencoding('utf8')

def getPyVer():
    return platform.python_version()
