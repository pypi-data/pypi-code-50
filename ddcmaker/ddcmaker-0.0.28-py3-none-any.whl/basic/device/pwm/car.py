"""
电机控制
"""
import pigpio


class Motor(object):
    def __init__(self, forward_pin: int, backward_pin: int,
                 freq: int = 10000, max_value: int = 100,
                 ):
        """
        :param forward_pin: 控制前进的引脚
        :param backward_pin: 控制后退的引脚
        :param freq:设置频率，默认值为10khz
        """
        # 引脚号,采用BCM编码
        self.pi = pigpio.pi()
        self._forward_pin = forward_pin
        self._backward_pin = backward_pin
        self.max_value = max_value

        # 设置pwm舵机范围
        self.pi.set_PWM_range(self._forward_pin, self.max_value)
        self.pi.set_PWM_range(self._backward_pin, self.max_value)

        # 设置频率
        self.pi.set_PWM_frequency(self._forward_pin, freq)
        self.pi.set_PWM_frequency(self._backward_pin, freq)

        # 初始化pin控制
        self.pi.set_PWM_dutycycle(self._forward_pin, 0)
        self.pi.set_PWM_dutycycle(self._backward_pin, 0)

    def forward(self, speed):
        """前进"""
        speed = min(max(0, speed), self.max_value)
        self.pi.set_PWM_dutycycle(self._forward_pin, speed)
        self.pi.set_PWM_dutycycle(self._backward_pin, 0)

    def backward(self, speed):
        """后退"""
        speed = min(max(0, speed), self.max_value)
        self.pi.set_PWM_dutycycle(self._forward_pin, 0)
        self.pi.set_PWM_dutycycle(self._backward_pin, speed)

    def stop(self):
        self.pi.set_PWM_dutycycle(self._forward_pin, 0)
        self.pi.set_PWM_dutycycle(self._backward_pin, 0)
