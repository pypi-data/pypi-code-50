# -*- coding:utf-8 -*-
# @Author: MoonKnight
# @Time:2020-03-15

import random
import time

class luckynum:

    time = None
    num = None

    def __init__(self):
        self.time = time.time()
        self.num = random.randrange(int(self.time))%10

    def get_luckynum(self):
        return self.num

