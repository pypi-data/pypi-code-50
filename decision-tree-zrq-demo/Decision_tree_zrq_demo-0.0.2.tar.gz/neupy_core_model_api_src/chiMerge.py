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
def split(Instances):
    ''''' Split the 4 attibutes, collect the data of the ith attributs, i=0,1,2,3
        Return a list like [['0.2', 'Iris-setosa'], ['0.2', 'Iris-setosa'],...]'''
    log=[]
    for i in range(len(Instances)):
        log.append([Instances.iloc[i][0], Instances.iloc[i][1]])
    return(log)

def count(log):
    '''''Count the number of the same record
      Return a list like [['4.3', 'Iris-setosa', 1], ['4.4', 'Iris-setosa', 3],...]'''
    log_cnt=[]
    log.sort(key=lambda log:log[0])
    i=0
    while(i<len(log)):
        cnt=log.count(log[i])#count the number of the same record
        record=log[i][:]
        record.append(cnt) # the return value of append is None
        log_cnt.append(record)
        i+=cnt#count the next diferent item
    return(log_cnt)

def build(log_cnt):
    '''''Build a structure (a list of truples) that ChiMerge algorithm works properly on it
         return a list like ([0:[6,0]],...) 含义：变量值为0是，非违规6人，违规0人 '''
    log_dic={}
    for record in log_cnt:
        if record[0] not in log_dic.keys():
            log_dic[record[0]]=[0,0]
        if record[1]==0:
            log_dic[record[0]][0]=record[2]
        elif record[1]==1:
            log_dic[record[0]][1]=record[2]
        else:
            raise TypeError("Data Exception")
    log_truple=sorted(log_dic.items())
    return(log_truple)

def collect(Instances):
    ''''' collect data for discretization '''
    log = split(Instances)
    log_cnt = count(log)
    log_tuple = build(log_cnt)
    return (log_tuple)

def combine(a,b):
    '''''  a=('4.4', [3, 1, 0]), b=('4.5', [1, 0, 2])
           combine(a,b)=('4.4', [4, 1, 2])  '''
    c=a[:] # c[0]=a[0]
    for i in range(len(a[1])):
        c[1][i]+=b[1][i]
    return(c)

def chi2(A):
    ''''' Compute the Chi-Square value '''
    '''计算两个区间的卡方值'''
    m=len(A);
    k=len(A[0])
    R=[]
    '''第i个区间的实例数'''
    for i in range(m):
        sum=0
        for j in range(k):
            sum+=A[i][j]
        R.append(sum)
    C=[]
    '''第j个类的实例数'''
    for j in range(k):
        sum=0
        for i in range(m):
            sum+=A[i][j]
        C.append(sum)
    N=0
    '''总的实例数'''
    for ele in C:
        N+=ele
    res=0
    for i in range(m):
        for j in range(k):
            Eij=R[i]*C[j]/N
            if Eij!=0:
                res=res+(A[i][j]-Eij)**2/Eij
    return res

def ChiMerge(log_tuple,max_interval):
    ''''' ChiMerge algorithm  '''
    ''''' Return split points '''
    num_interval=len(log_tuple)
    while(num_interval>max_interval):
        num_pair=num_interval-1
        chi_values=[]
        ''' 计算相邻区间的卡方值'''
        for i in range(num_pair):
            arr=[log_tuple[i][1],log_tuple[i+1][1]]
            chi_values.append(chi2(arr))
        min_chi=min(chi_values) # get the minimum chi value
        for i in range(num_pair-1,-1,-1): # treat from the last one
            if chi_values[i]==min_chi:
                log_tuple[i]=combine(log_tuple[i],log_tuple[i+1]) # combine the two adjacent intervals
                log_tuple[i+1]='Merged'
        while('Merged' in log_tuple): # remove the merged record
            log_tuple.remove('Merged')
        num_interval=len(log_tuple)
    split_points = [record[0] for record in log_tuple]
    return(split_points)

def chiMerge(df, max_group):
    # print('Strat:' + ctime())
    log_touple = collect(df)
    print(log_touple)
    split_point = ChiMerge(log_touple,max_group)
    # print('End:' + ctime())
    return split_point
