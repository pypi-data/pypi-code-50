# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:42:58 2020

@author: jcnossen1
"""

# -*- coding: utf-8 -*-

import multiprocessing as mp

import time

def _procMain(q):
    for k in range(100):
        print('procMain\n')


class TiffWriter:
    
    def __init__(self):
        self.pipe = mp.Pipe()
        self.p = mp.Process(target=_procMain, args=(self.pipe,))
        
        self.p.start()
        self.p.join()
        
    def pushImage(self, img):
        

if __name__ == "__main__":
    w = TiffWriter()
    
    