# -*- coding: utf-8 -*-
# @Time : 2020-03-03 16:50
# @Author : xzr
# @File : __init__.py.py
# @Software: PyCharm
# @Contact : xzregg@gmail.com
# @Desc :


import os

from supervisor.supervisord import main
from supervisor.loggers import RotatingFileHandler

def doRollover(self):
    """
    Do a rollover, as described in __init__().
    """

    if self.maxBytes <= 0:
        return
    if not (self.stream.tell() >= self.maxBytes):
        return
    self.stream.close()
    # patch multiprocess log segmentation
    if self.backupCount > 0 and  os.path.getsize(self.baseFilename) >= self.maxBytes:
        for i in range(self.backupCount - 1, 0, -1):
            sfn = "%s.%d" % (self.baseFilename, i)
            dfn = "%s.%d" % (self.baseFilename, i + 1)
            if os.path.exists(sfn):
                self.removeAndRename(sfn, dfn)
        dfn = self.baseFilename + ".1"
        self.removeAndRename(self.baseFilename, dfn)

    self.stream = open(self.baseFilename, 'ab')


RotatingFileHandler.doRollover = doRollover
main = main