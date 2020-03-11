#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
白色机器人PWMServo控制，主要控制头部
"""
import pigpio
from ddcmaker.basic.device.pwm.robot import PWMServo


class PWMServoController(object):
    def __init__(self, pins: tuple = (5, 6), deviations: tuple = (0, 0),
                 min_pos: int = 500, max_pos: int = 2500,
                 min_used_time: int = 20, max_used_time: int = 30000,
                 min_deviation: int = -300, max_deviation: int = 300):
        """
        :param pins:引脚信息，默认的(5,6)对应扩展板上的(7,8)
        :param deviations:每个引脚的偏差，与pins一一对应
        :param min_pos:最小的角度
        :param max_pos:最大角度
        :param min_used_time:最小耗时
        :param max_used_time:最大耗时
        :param min_deviation:最小偏差
        :param max_deviation:最大偏差
        """
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.min_used_time = min_used_time
        self.max_used_time = max_used_time
        self.min_deviation = min_deviation
        self.max_deviation = max_deviation

        self.pi = pigpio.pi()

        self.servos = []
        for pin, deviation in zip(pins, deviations):
            self.servos.append(PWMServo(self.pi, pin, deviation=deviation))

        self.nod_id = 1
        self.shaking_id = 2
        self.interval_time = 200
        self.start_angle = 1200
        self.homing_angle = 1500
        self.end_angle = 1700

    def set_servo(self, servo_id: int, pos: int, used_time: int):
        """
        控制相应的舵机
        :param servo_id:舵机号
        :param pos:舵机运转角度
        :param used_time:耗时
        :return:
        """
        if servo_id <= 0 or servo_id > len(self.servos):
            return
        pos = min(max(pos, self.min_pos), self.max_pos)
        used_time = min(max(used_time, self.min_used_time), self.max_used_time)
        self.servos[servo_id - 1].set_position(pos, used_time)

    def set_deviation(self, servo_id, deviation):
        """
        设置舵机的误差
        :param servo_id:舵机号
        :param deviation: 误差
        :return:
        """
        if servo_id <= 0 or servo_id > len(self.servos):
            return
        if deviation < self.min_deviation or deviation > self.max_used_time:
            return
        self.servos[servo_id - 1].deviation = deviation
