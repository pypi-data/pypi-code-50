# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/11 11:25                      *
# @Author  : Bob He                                |
# @FileName: AI_human.py                           *
# @Software: PyCharm                               |
# @Project : ddcmaker                              *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
import sys

from ddcmaker.maker.human.ad_mode import ad_mode

human = ["cv_find_stream.py", "cv_color_stream.py", "cv_find_hand.py", "cv_distance_stream.py", "cv_track_stream.py"]


class cv_mode(ad_mode):
    def __init__(self):
        super().__init__()
        self.Xpath = "python3 /home/pi/human/"
        self.list = human
        self.cap = " no_display "
        self.color = ["red", "green", "blue"]

    def follow(self, color):
        if color in self.color:
            print("机体跟随")
            self.name = self.list[0] + self.cap + color
            super().run()
        else:
            raise Exception(
                "函数 %s" % sys._getframe().f_code.co_name + "参数的颜色超出范围，请在" + str(self.color) + "中选择，不传参默认" + color)

    def identifying(self):
        print("颜色识别(红色点头，蓝绿摇头)")
        self.name = self.list[1] + self.cap
        super().run()

    def find_hand(self):
        print("手势识别")
        self.name = self.list[2] + self.cap
        super().run()

    def check_distance(self, color):
        if color in self.color:
            print("检测颜色距离")
            self.name = self.list[3] + self.cap + color
            super().run()
        else:
            raise Exception(
                "函数 %s" % sys._getframe().f_code.co_name + "传入参数的颜色超出范围，请在" + str(self.color) + "中选择，默认参数为" + color)

    def tracking(self, color):
        if color in self.color:
            print("云台追踪")
            self.name = self.list[4] + self.cap + color
            super().run()
        else:
            raise Exception(
                "函数 %s" % sys._getframe().f_code.co_name + "传入参数的颜色超出范围，请在" + str(self.color) + "中选择，默认参数为" + color)
