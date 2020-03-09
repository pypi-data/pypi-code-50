#!/usr/bin/python

###################################
# Data Validator By R&D ICWR      #
# Copyright (c)2020 - Afrizal F.A #
###################################

import re

class validator():
    def __init__(self,key,data):
        self.key=key
        self.data=data

    def proc(self,key,data):
        valid_data=[]
        for x in key:
            array_data=re.findall(x.lower(),data.lower())
            if array_data:
                valid_data.append(array_data)
        return valid_data

    def matching(self):
        if type(self.data) == list:
            valid_data=[]
            i=0
            for x in self.data:
                i=i+1
                valid_data.append({i:self.proc(self.key,x)})
            return valid_data
        else:
            return self.proc(self.key,self.data)
