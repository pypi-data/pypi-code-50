#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pa

class prova:
    def __init__(self, d1=1, d2=2, op='sum'):
        self.d1 = d1
        self.d2 = d2
        self.op = op
    def do_it(self):
        if self.op == 'sum':
            d3 = self.sum_()
        elif self.op == 'mult':
            d3 = self.multip()
        elif self.op == 'div':
            d3 = self.div()
        elif self.op == 'subtr':
            d3 = self.subtr()
        return d3
    def sum_(self):
        d3 = self.d2+self.d1
        return d3
    def multip(self):
        d3 = self.d2*self.d1
        return d3
    def div(self):
        d3 = self.d2/self.d1
        return d3
    def subtr(self):
        d3 = self.d2-self.d1
        return d3
    

