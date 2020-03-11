from typing import List, Tuple

from ddcmaker.basic.device.pwm.car import Motor
from ddcmaker.basic.abc import BasicMaker
from ddcmaker.maker.car.actions import normal


class Car(BasicMaker):
    def __init__(self):
        super().__init__('小车')
        # 引脚采用BCM编码
        self.left_motor = Motor(forward_pin=26, backward_pin=18)
        self.right_motor = Motor(forward_pin=7, backward_pin=8)

    def run_action_file(self, action_file_name, step=1, msg=None):
        self.logger("暂不支持")

    def set_servo(self, servo_infos: List[Tuple], used_time: int):
        self.logger("暂不支持")

    def left(self, angle: 10):
        """
        0.1秒大约10°
        """
        if angle < 0:
            self.logger(f"非法角度：{angle}")

        if 0 < angle < 10:
            _angle = 10
        else:
            _angle = angle
        for _ in range(round(_angle / 10)):
            normal.left(self, 0.1, 50)
        self.logger(f"左转 {angle}角度")

    def right(self, angle: 10):
        """
        0.1秒大约10°
        """
        if angle < 0:
            self.logger(f"非法角度：{angle}")

        if 0 < angle < 10:
            _angle = 10
        else:
            _angle = angle
        for _ in range(round(_angle / 10)):
            normal.right(self, 0.1, 50)
        self.logger(f"右转 {angle}角度")

    def forward(self, length: int = 1):
        """
        前进,单位为厘米
        """
        if length < 0:
            self.logger(f"非法长度：{length}")
        for _ in range(round(length / 1)):
            normal.forward(self, 0.1, 50)  # 大约1cm
        self.logger(f"前进 {length}厘米")

    def backward(self, length):
        """
        后退,单位为厘米
        """
        if length < 0:
            self.logger(f"非法长度：{length}")
        for _ in range(round(length / 1)):
            normal.backward(self, 0.1, 50)  # 大约1cm

        self.logger(f"后退 {length}厘米")

    def stop(self):
        normal.stop(self)
