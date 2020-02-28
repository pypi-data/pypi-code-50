#!/usr/bin/env python3
import datetime as dt

class Latency:
    def __init__(self):
        self.latency = ''

    def log(self, field, value=dt.datetime.now()):
        self.latency += '%s: %s__' % (field,value,)

    
