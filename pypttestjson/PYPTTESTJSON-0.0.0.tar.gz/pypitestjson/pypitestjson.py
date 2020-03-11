#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import os
import sys
import json

def load_dict(self,filename):
    with open(filename, "r") as json_file:
        dic = json.load(json_file)
    return dic

    
def save_dict(self,filename,dic):
    with open(filename, 'w') as json_file:
        json.dump(dic, json_file)