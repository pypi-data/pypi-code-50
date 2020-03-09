#!/usr/bin/python
# -*- coding:utf-8 -*-

from time import ctime
import pymysql
import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import threading
import multiprocessing
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
# from jilincode.chiMerge import chiMerge
#from zrq import chiMerge
from time import ctime
from pandas.core.frame import DataFrame

def read4oracle():
    print("从测试数据库中获得数据，AC01_PC_TRAIN_ALL")
    import cx_Oracle
    # conn = cx_Oracle.connect('jlbd_da/jlbd_da@172.27.125.10/dsj1')
    # conn = cx_Oracle.connect('xyscore/xyscore@10.16.23.107/orcl')
    # conn = cx_Oracle.connect('jhk_test/jhk_test@10.16.23.107/orcl')
    # conn = cx_Oracle.connect('hma_analyse/hma_analyse@127.0.0.1/orcl')
    try:
        host = "172.27.125.10"
        port = "1521"
        sid = "dsj1"
        dsn = cx_Oracle.makedsn(host,port,sid)
        conn = cx_Oracle.connect("jlbd_temp","Neusoft12#$", dsn)
        sql = "select * from AC01_PC_TRAIN_ALL"
        data = pd.read_sql(sql, conn)
    except:
        print("\n 读取数据报错...")
    else:
        print("\n 读取数据完成...")
    # print(data)
    return data

    db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8')

    print("从测试数据库中获得数据，AC01_PC_TRAIN_10000")
    # import cx_Oracle
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "admin", "how2java")
    curs = db.cursor()
    printHeader = True
    sql = "select * from AC01_PC_TRAIN_10000"
    curs.execute(sql)
    list_data = []
    colname = []
    i = 0
    if printHeader:
        for col in curs.description:
            colname.append(col[0])
    for row_data in curs:
        i = i + 1
        list_data.append(list(row_data))
    print("\n 读取数据完成，数据类型转换并写到文件中")
    data = DataFrame(list_data)
    data.columns = colname
    return data
