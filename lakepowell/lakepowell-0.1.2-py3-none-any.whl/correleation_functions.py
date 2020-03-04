# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:34:44 2020

@author: aquag
"""
from scipy.stats.stats import pearsonr
#import numpy as np

#need to pull the fish data
    #what are we looking at? catch erp unit effort? biomass?
#pull the water levels
#find corelation
def cor_min_height(fish_data, water_data):
    min_hight = water_data["MIN ELEVATION"]
    corelation = pearsonr(fish_data, water_data)
    return corelation

def cor_max_height(fish_data, water_data):
    max_height = water_data["MAX ELEVATION"]
    corelation = pearsonr(fish_data,max_height)
    return corelation

def cor_ave_depth(fish_data, water_data):
    corelation = []
    return corelation

def cor_change_height(fish_data, water_data):
    change_height = water_data["DIFFERENCE"]
    corelation = pearsonr(fish_data, change_height)
    return corelation

#additinal funciton that will find best match for a set range of years
#will call one of the smaller functions to do so