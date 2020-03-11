"""老版机器人，不再维护优化"""

from ddcmaker.maker.human import robot
from ddcmaker.public import showlib
from ddcmaker.maker.human.AI_human import cv_mode as cv

Rb = robot.robot()
Sh = showlib.showlib()


class Robot(object):
    @staticmethod
    def init_head():
        Rb.init_head()

    @staticmethod
    def left(step=1):
        Rb.left(step)

    @staticmethod
    def right(step=1):
        Rb.right(step)

    @staticmethod
    def left_slide(step=1):
        Rb.left_slide(step)

    @staticmethod
    def right_slide(step=1):
        Rb.right_slide(step)

    @staticmethod
    def forward(step=1):
        Rb.forward(step)

    @staticmethod
    def backward(step=1):
        Rb.backward(step)

    @staticmethod
    def up(step=1):
        Rb.up(step)

    @staticmethod
    def down(step=1):
        Rb.down(step)

    @staticmethod
    def check(step=1):
        Rb.check(step)

    @staticmethod
    def nod(step=1):
        Rb.nod(step)

    @staticmethod
    def shaking_head(step=1):
        Rb.shaking_head(step)

    '''虚不实真，苦切一除能，咒等等无是，咒上无是，咒明大是'''

    @staticmethod
    def hiphop():
        Sh.hiphop()

    @staticmethod
    def smallapple():
        Sh.smallapple()

    @staticmethod
    def jiangnanstyle():
        Sh.jiangnanstyle()

    @staticmethod
    def lasong():
        Sh.lasong()

    @staticmethod
    def feelgood():
        Sh.feelgood()

    @staticmethod
    def push_up():
        Rb.push_up()

    @staticmethod
    def abdominal_curl():
        Rb.abdominal_curl()

    @staticmethod
    def wave():
        Rb.wave()

    @staticmethod
    def bow():
        Rb.bow()

    @staticmethod
    def spread_wings():
        Rb.spread_wings()

    @staticmethod
    def haha():
        Rb.haha()

    @staticmethod
    def follow(color="green"):
        r = cv()
        r.follow(color)

    @staticmethod
    def find_color():
        r = cv()
        r.identifying()

    @staticmethod
    def find_hand():
        r = cv()
        r.find_hand()

    @staticmethod
    def check_distance(color="green"):
        r = cv()
        r.check_distance(color)

    @staticmethod
    def tracking(color="green"):
        r = cv()
        r.tracking(color)


def init():
    normal_robot = Robot()
    normal_robot.init_head()
