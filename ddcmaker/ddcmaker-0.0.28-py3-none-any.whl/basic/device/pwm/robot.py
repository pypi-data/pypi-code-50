#!/usr/bin/python3
# encoding: utf-8
"""
适配pwm总线舵机
"""
import time
import threading
from pigpio import pi

USED_TIME_MIN = 20
USED_TIME_MAX = 30000
DEVIATION_MIN = -300
DEVIATION_MAX = 300


class PWMServo(object):
    """控制pwm总线舵机"""

    def __init__(self, pi: pi, pin: int, freq: int = 50, min_width: int = 500,
                 max_width: int = 2500, deviation: int = 0,
                 init_position: int = 1450):
        """
        初始化pwm总线舵机
        :param pi:gpio对象
        :param pin:引脚号
        :param freq:控制频率
        :param min_width:舵机最小范围
        :param max_width:舵机最大范围
        :param deviation:偏差
        """
        self.pi = pi
        self.pin = pin
        self.target_position = init_position  # 舵机预期移动到的位置
        self.position = self.pi.get_servo_pulsewidth(self.pin)  # 舵机当前位置
        self._freq = freq
        self._min = min_width
        self._max = max_width

        self._deviation = deviation

        self.interval = 20  # 连续转动舵机时的间隔时间，单位为毫秒
        self.used_time = 0
        self.init_servo()

    def init_servo(self):
        if abs(self.position - self.target_position) != self._deviation:
            self.set_position(self.target_position, used_time=200)

    def set_position(self, pos, used_time=0):
        """
        转动舵机
        :param pos:目标舵机位置
        :param used_time:耗时
        :return:
        """
        if pos < self._min or pos > self._max:
            print(pos)
            return

        if used_time == 0:
            # 立即响应
            self.target_position = pos
            self.position = self.target_position
            self.pi.set_PWM_dutycycle(self.pin,
                                      self.position + self.deviation)
        else:
            self.used_time = min(max(USED_TIME_MIN, used_time), USED_TIME_MAX)
            self.target_position = pos
            thread = threading.Thread(target=self.update_position)
            thread.start()

    @property
    def deviation(self):
        """
        获取当前偏差
        :return:
        """
        return self._deviation

    @deviation.setter
    def deviation(self, deviation: int = 0):
        """
        设置偏差，当deviation大于DEVIATION_MAX或小于DEVIATION_MIN时，设置失败
        :param deviation:偏差
        :raise:
        :return:
        """
        if deviation > DEVIATION_MAX or deviation < DEVIATION_MIN:
            print(f"deviation的允许范围为{DEVIATION_MIN}-{DEVIATION_MAX}")
            return
        self._deviation = deviation

    def update_position(self):
        """
        用于动态执行servo的动作
        :param self:pwm总线舵机
        :return:
        """
        if self.target_position == self.position:
            return
        # 舵机转动次数
        times = int(self.used_time / self.interval)

        # 计算每次转动的幅度
        position_inc = int(
            (self.target_position - self.position) / (times - 1))

        steps = [position_inc for _ in range(times - 1)]
        steps.append(
            self.target_position - self.position - position_inc * (times - 1))

        # 执行更新
        for step in steps:
            try:
                self.pi.set_servo_pulsewidth(self.pin, int(
                    self.position + step + self.deviation))
            except Exception as err:
                print(err)
            self.position += step
            time.sleep(self.interval / 1000)

# def update_position(serial: PWMServo):
#     """
#     用于动态执行servo的动作
#     :param serial:pwm总线舵机
#     :return:
#     """
#     while True:
#         steps = []
#         if serial.pos_changed is True:
#             # 舵机转动次数
#             times = int(serial.used_time / serial.interval)
#             # 每次转动的幅度
#
#             position_inc = int(abs(
#                 serial.position - serial.target_position) / (times - 1))
#
#             steps = [position_inc for _ in range(times - 1)]
#             steps.append(
#                 abs(serial.position - serial.target_position) - position_inc * (
#                         times - 1))
#
#             serial.servo_running = True
#
#             serial.pos_changed = False
#
#         if serial.servo_running is True:
#             for step in steps:
#                 try:
#                     serial.pi.set_servo_pulsewidth(serial.pin, int(
#                         serial.position + step + serial.deviation))
#                 except:
#                     pass
#                 serial.position += step
#                 time.sleep(serial.interval)
#             serial.servo_running = False
