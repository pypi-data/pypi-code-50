#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

__all__ = ['Duration']

class Duration:
    def __init__(self):
        self.start = 0.0
        self.duree = 0.0
        self.top = True

    def __call__(self):
        if self.top:
            self.start = time.time()
            self.duree = 0.0
            self.top = False
        else :
            self.duree = time.time() - self.start
            self.start = time.time()
            self.top = True
        return self.duree
    
    def st(self):
        self.top = False
        self.start = time.time()

    def sp(self):
        self.top = True
        self.duree = time.time() - self.start

    def get(self):
        return self.duree

    def evaluate(self, func, *args, **kwargs):
        self.st()
        r = func(*args, **kwargs)
        self.sp()
        return (self.get(), r)
    