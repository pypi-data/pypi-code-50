#!/usr/bin/env python

"""
Utilities to log time.
"""

import time


class Timer(object):
    # class property specifying whether the created instances are active
    active = True

    def __init__(self, fmt='timer {:.3e} sec: {:<s}'):
        self.__t = time.time()
        self.__fm = fmt

    def lap(self, message=''):
        if self.active:
            t = time.time()
            if message:
                print(self.__fm.format(t - self.__t, message))
            self.__t = t


if __name__ == '__main__':
    # usage example
    t0 = Timer()

    from sys import argv
    if argv[1] == 'True':
        Timer.active = True
    else:
        Timer.active = False

    t1 = Timer()
    for n in map(int, argv[2:]):
        s = 0
        for i in range(n + 1):
            s += i
        t1.lap(message='completed for n={}. s={}'.format(n, s))

    Timer.active = True
    t0.lap(message='Whole script')
