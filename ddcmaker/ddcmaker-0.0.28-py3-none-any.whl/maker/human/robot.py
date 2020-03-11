"""老版机器人，不再维护优化"""
import time

from ddcmaker.public.lsc_client import LSC_Client

lsc = LSC_Client()


class robot(object):
    lsc.MoveServo(6, 1500, 1000)
    lsc.MoveServo(7, 1500, 1000)
    time.sleep(2.1)

    def __init__(self):
        self.nodid = 1
        self.shakingid = 2
        self.Interval_time = 200
        self.start_angle = 1200
        self.homing_angle = 1500
        self.end_angle = 1700

    def init_head(self):
        PWMServo.setServo(self.nodid, self.homing_angle, self.Interval_time / 2)
        time.sleep(self.Interval_time / 200)
        PWMServo.setServo(self.shakingid, self.homing_angle, self.Interval_time)
        time.sleep(self.Interval_time / 1000)

    def up(self, step=1):
        lsc.RunActionGroup(0, step)
        lsc.WaitForFinish(5000)
        print("机器人站立")

    def down(self, step=1):
        lsc.RunActionGroup(14, step)
        lsc.WaitForFinish(5000)
        print("机器人蹲下")

    def check(self, step=1):
        lsc.RunActionGroup(188, step)
        lsc.WaitForFinish(5000)
        print("机器人自检")

    def forward(self, step):
        for i in range(step):
            lsc.RunActionGroup(1, 1)
            lsc.WaitForFinish(5000)
            print("机器人前进")

    def backward(self, step):
        for i in range(step):
            lsc.RunActionGroup(2, 1)
            lsc.WaitForFinish(5000)
            print("机器人后退")

    def left(self, step):
        for i in range(step):
            lsc.RunActionGroup(3, 1)
            lsc.WaitForFinish(5000)
            print("机器人左转")

    def right(self, step):
        for i in range(step):
            lsc.RunActionGroup(4, 1)
            lsc.WaitForFinish(5000)
            print("机器人右转")

    def shaking_head(self, step):
        for i in range(step):
            lsc.RunActionGroup(50, 1)
            lsc.WaitForFinish(5000)
            print("机器人摇头")

    def nod(self, step):
        for i in range(step):
            lsc.RunActionGroup(51, 1)
            lsc.WaitForFinish(5000)
            print("机器人点头")

    def left_slide(self, step):
        for i in range(step):
            lsc.RunActionGroup(11, 1)
            lsc.WaitForFinish(5000)
            print("机器人左滑")

    def right_slide(self, step):
        for i in range(step):
            lsc.RunActionGroup(12, 1)
            lsc.WaitForFinish(5000)
            print("机器人右滑")

    def push_up(self, step=1):
        lsc.RunActionGroup(7, step)
        time.sleep(3)
        print("机器人俯卧撑")

    def abdominal_curl(self, step=1):
        lsc.RunActionGroup(8, step)
        time.sleep(3)
        print("机器人仰卧起坐")

    def wave(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(9, 1)
            time.sleep(2.1)
            print("机器人挥手┏(＾0＾)┛")

    def bow(self, step=1):
        lsc.RunActionGroup(10, step)
        time.sleep(2.1)
        print("机器人鞠躬╰(￣▽￣)╭")

    def spread_wings(self, step=1):
        lsc.RunActionGroup(13, step)
        time.sleep(3)
        print("机器人大鹏展翅")

    def haha(self, step=1):
        lsc.RunActionGroup(15, step)
        time.sleep(2.1)
        print("机器人哈哈大笑o(*￣▽￣*)o")


from ddcmaker.public import voice, PWMServo


def speak(viocenum):
    if viocenum >= 48 or viocenum <= 25:
        return "超出语音模块区域"
    else:
        lsc.RunActionGroup(viocenum, 1)
        vlist = voice.voicelist()
        lsc.WaitForFinish(int(20000))
        time.sleep(int(vlist.voicelist()[viocenum]))
