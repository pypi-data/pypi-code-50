"""
用于将角度转换为舵机运行值，并实现最大角度和最小角度控制
"""


class Servo(object):
    def __init__(self, servo_id: int, min_value: int = 140,
                 max_value: int = 860, init_value: int = 500,
                 per_angle_to_value: int = 4, reverse=False):
        self._min_value = min_value
        self._max_value = max_value
        self._init_value = init_value
        self._per_angle_to_value = per_angle_to_value
        self.servo_id = servo_id
        if reverse is True:
            self._max_angle = (init_value - min_value) / per_angle_to_value
            self._min_angle = (init_value - max_value) / per_angle_to_value
        else:
            self._max_angle = (max_value - init_value) / per_angle_to_value
            self._min_angle = (min_value - init_value) / per_angle_to_value

        self._reverse = reverse

    def get_value(self, angle: int):
        """
        将角度转换为舵机运行值
        """
        if angle > self._max_angle or angle < self._min_angle:
            print(f"angle参数，非法{angle},合法值{self._min_angle}-{self._max_angle}")
            return
        if self._reverse:
            value = self._init_value - angle * self._per_angle_to_value
        else:
            value = self._init_value + angle * self._per_angle_to_value
        value = int(min(max(self._min_value, value), self._max_value))
        return int(min(max(self._min_value, value), self._max_value))
