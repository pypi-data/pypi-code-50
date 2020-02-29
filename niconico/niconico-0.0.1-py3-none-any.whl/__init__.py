# -*- coding:utf-8 -*- 

import os
import codecs

__version__ = codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION.txt')).read()
__author__ = 'Iseuwei'

#有顺序
from .m_reque import MyReque
from .m_mysql import MySql
from .user_bilibili import User
from .video_bilibili import Video
from .m_test import BiliBili
