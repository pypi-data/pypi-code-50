# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:27:35 2020

@author: aquag
"""

def calc_biomass_average(data):
    #We take in the data frame
    #pull weights
    weights = data["Weight"]
        #add together
    total_weight = sum(weights)
    #divide by total number of enteries
    size = len(weights)
    biomass = total_weight/size
    #return aveerage biomass
    return biomass

#def biomass function that takes in the whoel table and pulls out values
#runs the calcualtions for all of these and gives now column
    
def calc_biomass_total(data):
     #We take in the data frame
    #pull weights
    weights = data["Weight"]
        #add together
    total_weight = sum(weights)
   
    return total_weight