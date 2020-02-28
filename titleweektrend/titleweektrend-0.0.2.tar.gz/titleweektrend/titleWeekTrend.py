#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:47:10 2020

@author: seangao
"""


from pytrends.request import TrendReq
from datetime import date
import datetime
import re
import contractions
import spacy 
import en_core_web_sm

#GET WEEK TREND FOR A SINGLE WORD
def getWeekTrend(word):
    kw_list = [word]
    
    today = date.today()
    tomorrow = today + datetime.timedelta(days=1)
    week_ago = today - datetime.timedelta(days=7)
    
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_df = pytrends.get_historical_interest(kw_list, 
                                         year_start=week_ago.year, 
                                         month_start=week_ago.month, 
                                         day_start=week_ago.day, 
                                         hour_start=0, 
                                         year_end=tomorrow.year, 
                                         month_end=tomorrow.month, 
                                         day_end=tomorrow.day, 
                                         hour_end=0,
                                         sleep=120)
    kwWT = kw_df[word].sum()
    return kwWT
 
#LOWERCASE FUNCTION
def lowerCase(input_str):
    input_str = input_str.lower()
    return input_str

#LEMMATIZATION FUNCTION
def lemma(input_str):
    sp = en_core_web_sm.load()
    s = sp(input_str)
    
    input_list = []
    for word in s:
        w = word.lemma_
        input_list.append(w)
        
    output = ' '.join(input_list)
    return output

#CONVERT THE TITLE
def titleConvert(title):
    t = contractions.fix(title)
    t = re.sub('[^a-zA-z0-9\s]','',t)
    t = lowerCase(t)
    t = lemma(t)
    t = t.replace('nowthis', '')
    t = t.strip()
    return t

#GET WEEK TREND FOR A TITLE
def titleWeekTrend(title):
    t = titleConvert(title)
    t_list = t.split()
    
    tr_list = []
    for word in t_list:
        tr = getWeekTrend(word)
        tr_list.append(tr)
        
    return sum(tr_list)