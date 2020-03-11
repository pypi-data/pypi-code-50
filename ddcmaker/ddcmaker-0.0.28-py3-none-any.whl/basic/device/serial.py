#!/usr/bin/python3
# encoding: utf-8
"""
控制串联舵机
串口设置可以参考https://www.mouser.com/datasheet/2/348/u92747-e-1021105.pdf 第12页
"""
import pathlib
import sqlite3 as sql
import serial
import pigpio
import time
import ctypes
from ddcmaker.basic.constant import lobot_servo_constant as Constant


class Serial(object):
    def __init__(self, dev: str = "/dev/ttyAMA0",
                 freq: int = 115200, rx_con_pin: int = 17,
                 tx_con_pin: int = 27):
        """
        :param dev:设备文件路径，默认/dev/ttyAMA0
        :param freq:波特率，默认115200
        :param rx_con_pin:控制寄存器 rx_con对应的gpio
        :param tx_con_pin:控制寄存器 x_con对应的gpio
        """
        self.pi = pigpio.pi()
        self.serialHandle = serial.Serial(dev, freq)
        self.rx_con_pin = rx_con_pin
        self.tx_con_pin = tx_con_pin
        self.port_init()

    def port_init(self):
        self.pi.set_mode(self.rx_con_pin, pigpio.OUTPUT)
        self.pi.write(self.rx_con_pin, 0)
        self.pi.set_mode(self.tx_con_pin, pigpio.OUTPUT)
        self.pi.write(self.tx_con_pin, 1)

    def port_write(self):
        """配置串行接口模式为写模式，即tx_con为1，rx_con为0"""
        self.pi.write(self.tx_con_pin, 1)
        self.pi.write(self.rx_con_pin, 0)

    def port_read(self):
        """配置串行接口模式为读模式，即tx_con为0，rx_con为1"""
        self.pi.write(self.rx_con_pin, 1)
        self.pi.write(self.tx_con_pin, 0)

    def port_reset(self):
        """重置串行接口模式，即tx_con为1，rx_con为1"""
        time.sleep(0.1)
        self.serialHandle.close()
        self.pi.write(self.rx_con_pin, 1)
        self.pi.write(self.tx_con_pin, 1)
        self.serialHandle.open()
        time.sleep(0.1)

    def write(self, servo_id: int = None, w_cmd: int = None,
              dat1: int = None, dat2: int = None):
        """
        下发写指令
        指令格式：帧头 舵机号 指令长度 读指令 |读指令 dat1低八位|
        读指令 dat1低八位 dat1高八位 dat2低八位 dat2高八位
        数据长度=指令除帧头后剩余部分个数
        :param servo_id:舵机号
        :param w_cmd:写指令
        :param dat1:
        :param dat2:
        :return:
        """
        self.port_write()
        buf = bytearray()

        # 帧头
        buf.append(Constant.LOBOT_SERVO_FRAME_HEADER)
        buf.append(Constant.LOBOT_SERVO_FRAME_HEADER)

        data_buf = bytearray()
        # 舵机号
        data_buf.append(servo_id)
        # 读指令,数据长度稍后计算
        data_buf.append(w_cmd)

        if dat1 is not None and dat2 is None:
            # 当dat2为None，只取dat1的低八位
            data_buf.append(dat1 & 0xff)
        elif dat1 is not None and dat2 is not None:
            # 当dat1和dat2都不为None，依次取dat1和data2低八位,高八位
            data_buf.extend([(0xff & dat1), (0xff & (dat1 >> 8))])
            data_buf.extend([(0xff & dat2), (0xff & (dat2 >> 8))])
        data_length = len(data_buf) + 1

        # 数据长度
        data_buf.insert(1, data_length)
        buf.extend(data_buf)
        # 计算数据的校验和
        buf.append(get_checksum(buf))

        self.serialHandle.write(buf)

    def read(self, servo_id: int = None, r_cmd: int = None):
        """
        下发读指令
        指令格式：帧头 舵机号 指令长度 写指令
        :param servo_id:舵机号
        :param r_cmd:写指令
        :return:
        """
        self.port_write()
        buf = bytearray()
        # 帧头
        buf.append(Constant.LOBOT_SERVO_FRAME_HEADER)
        buf.append(Constant.LOBOT_SERVO_FRAME_HEADER)
        # 舵机号
        buf.append(servo_id)
        # 数据长度
        buf.append(3)
        # 读指令
        buf.append(r_cmd)
        # 生成校验和
        buf.append(get_checksum(buf))
        self.serialHandle.write(buf)
        time.sleep(0.00034)

    def get_cmd_msg(self, cmd: int):
        """
        获取指令回显
        :param cmd:指令类型
        :return:
        """
        self.serialHandle.flushInput()
        self.port_read()
        time.sleep(0.005)
        # 指令返回的数据格式：帧头 舵机号 数据长度 指令 数据
        count = self.serialHandle.inWaiting()  # 获取缓存中的字节数

        # 判断返回的数据是否合法
        if count >= 5:
            recv = self.serialHandle.read(count)
            if recv[0] != 0x55 or recv[1] != 0x55 or recv[4] != cmd:
                self.serialHandle.flushInput()
                return None
        else:
            self.serialHandle.flushInput()
            return None

        # 根据数据长度，返回相应的数据
        dat_len = recv[3]
        self.serialHandle.flushInput()
        if dat_len == 3:
            return None
        elif dat_len == 4:
            return recv[5]
        elif dat_len == 5:
            pos = 0xffff & (recv[5] | (0xff00 & ((recv[6]) << 8)))
            return ctypes.c_int16(pos).value
        elif dat_len == 7:
            pos1 = 0xffff & (recv[5] | (0xff00 & ((recv[6]) << 8)))
            pos2 = 0xffff & (recv[7] | (0xff00 & ((recv[8]) << 8)))
            return ctypes.c_int16(pos1).value, ctypes.c_int16(pos2).value

    def set_new_servo_id(self, old_servo_id, new_servo_id):
        """
        将旧舵机号：old_servo_id设置为新舵机号：new_servo_id
        :param old_servo_id:旧舵机号
        :param new_servo_id:新舵机号
        :return:
        """
        self.write(old_servo_id, Constant.LOBOT_SERVO_ID_WRITE, new_servo_id)

    def get_id(self, servo_id: int = None):
        """
        获取舵机id，如果servo_id为None，则读取读缓存中的舵机id
        :param servo_id:
        :return:
        """
        while True:
            if servo_id is None:
                self.read(0xfe, Constant.LOBOT_SERVO_ID_READ)
            else:
                self.read(servo_id, Constant.LOBOT_SERVO_ID_READ)

            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_ID_READ)
            if msg is not None:
                return msg

    def stop_servo(self, servo_id: int = None):
        """
        指定舵机停止工作
        :param servo_id:舵机号
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_MOVE_STOP)

    def set_deviation(self, servo_id: int, deviation: int = 0):
        """
        设置舵机偏差
        :param servo_id:舵机号
        :param deviation:偏差
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_ANGLE_OFFSET_ADJUST,
                   deviation)
        self.write(servo_id, Constant.LOBOT_SERVO_ANGLE_OFFSET_WRITE)

    def get_deviation(self, servo_id: int):
        """
        读取指定舵机的偏差
        :param servo_id: 舵机号
        :return:
        """
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_ANGLE_OFFSET_READ)

            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_ANGLE_OFFSET_READ)
            if msg is not None:
                return msg

    def set_angle_limit(self, servo_id: int, low: int, high: int):
        """
        设置舵机角度的最小值和最大值
        :param servo_id:舵机号
        :param low:最小值
        :param high:最大值
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_ANGLE_LIMIT_WRITE, low, high)

    def get_angle_limit(self, servo_id: int):
        """获取舵机角度的最小值和最大值"""
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_ANGLE_LIMIT_READ)
            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_ANGLE_LIMIT_READ)
            if msg is not None:
                return msg

    def set_vin_limit(self, servo_id: int, low: int, high: int):
        """
        设置舵机电压的最小值和最大值
        :param servo_id: 舵机号
        :param low: 最小值，单位为mv
        :param high: 最大值，单位为mv
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_VIN_LIMIT_WRITE, low, high)

    def get_vin_limit(self, servo_id: int):
        """
        读取舵机电压的最小值和最大值，mv
        :param servo_id:舵机号
        :return:
        """
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_VIN_LIMIT_READ)
            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_VIN_LIMIT_READ)
            if msg is not None:
                return msg

    def get_vin(self, servo_id: int):
        """
        读取舵机电压，单位为mv
        :param servo_id: 舵机号
        :return:
        """
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_VIN_READ)
            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_VIN_READ)
            if msg is not None:
                return msg

    def set_max_temp(self, servo_id: int, m_temp: int):
        """
        设置舵机最大温度
        :param servo_id:舵机号
        :param m_temp: 最大温度
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_TEMP_MAX_LIMIT_WRITE, m_temp)

    def get_temp_limit(self, servo_id: int):
        """
        获取舵机温度范围
        :param servo_id:舵机号
        :return:
        """
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_TEMP_MAX_LIMIT_READ)
            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_TEMP_MAX_LIMIT_READ)
            if msg is not None:
                return msg

    def get_temp(self, servo_id: int):
        """
        获取舵机温度
        :param servo_id:舵机号
        :return:
        """
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_TEMP_READ)
            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_TEMP_READ)
            if msg is not None:
                return msg

    def set_position(self, servo_id: int, pos: int, used_time: int):
        """
        设置舵机的位置
        :param servo_id:舵机号
        :param pos: 位置
        :param used_time:耗时
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_MOVE_TIME_WRITE, pos,
                   used_time)

    def get_position(self, servo_id: int):
        """
        获取舵机的位置
        :param servo_id:舵机号
        :return:
        """
        while True:
            self.read(servo_id, Constant.LOBOT_SERVO_POS_READ)
            msg = self.get_cmd_msg(Constant.LOBOT_SERVO_POS_READ)
            if msg is not None:
                return msg

    def reset_position(self, servo_id: int):
        """
        重置舵机到初始化位置
        :param servo_id:舵机号
        :return:
        """
        self.set_deviation(servo_id, 0)
        time.sleep(0.1)
        self.write(servo_id, Constant.LOBOT_SERVO_MOVE_TIME_WRITE, 500, 100)

    def set_speed(self, servo_id: int, speed: int):
        """
        设置舵机运行速度
        :param servo_id: 舵机号
        :param speed: 运行速度
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_OR_MOTOR_MODE_WRITE,
                   1, speed)

    def set_servo_mode(self, servo_id: int, mode: int):
        """
        设置舵机的模式
        :param servo_id: 舵机号
        :param mode: 模式
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_OR_MOTOR_MODE_WRITE, mode, 0)

    def set_servo_load(self, servo_id: int, mode: int):
        """
        舵机加载模式
        :param servo_id:舵机号
        :param mode:
        :return:
        """
        self.write(servo_id, Constant.LOBOT_SERVO_LOAD_OR_UNLOAD_WRITE, mode)

    def show_servo_state(self):
        """
        展示舵机状态
        :return:
        """
        servo_id = self.get_id()
        self.port_reset()
        if servo_id is not None:
            print(f'当前的舵机ID是：{servo_id}')
            pos = self.get_position(servo_id)
            print(f'当前的舵机角度：{pos}')
            self.port_reset()

            now_temp = self.get_temp(servo_id)
            print(f'当前的舵机温度：{now_temp}')
            self.port_reset()

            now_vin = self.get_vin(servo_id)
            print(f'当前的舵机电压：{now_vin}mv')
            self.port_reset()

            d = self.get_deviation(servo_id)
            print(f'当前的舵机偏差：{ctypes.c_int8(d).value}')
            self.port_reset()

            limit = self.get_angle_limit(servo_id)
            print(f'当前的舵机可控角度为{limit[0]}-{limit[1]}')
            self.port_reset()

            vin = self.get_vin_limit(servo_id)
            print(f'当前的舵机报警电压为{vin[0]}mv-{vin[1]}mv')
            self.port_reset()

            temp = self.get_temp_limit(servo_id)
            print(f'当前的舵机报警温度为50°-{temp}°')
            self.port_reset()
        return servo_id


class SerialServoController(object):
    """串行舵机控制器"""

    def __init__(self, file_path: str, min_pos: int = 0, max_pos: int = 1000,
                 min_used_time: int = 10, max_used_time: int = 30000,
                 min_servo_id: int = 0, max_servo_id: int = 18,
                 min_deviation: int = -200, max_deviation: int = 200):
        """
        :param file_path:执行文件目录，如/home/pi/human_code/ActionGroups
        :param min_pos:最小位置
        :param max_pos:最大位置
        :param min_used_time:最小耗时
        :param max_used_time:最大耗时
        :param min_servo_id:舵机号最小值
        :param max_servo_id:舵机号最大值
        :param min_deviation:最小误差
        :param max_deviation:最大误差
        """
        self.file_path = pathlib.Path(file_path).absolute()
        self.serial = Serial()
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.min_used_time = min_used_time
        self.max_used_time = max_used_time
        self.min_servo_id = min_servo_id
        self.max_servo_id = max_servo_id
        self.min_deviation = min_deviation
        self.max_deviation = max_deviation
        self.action_status = False
        self.stop_action = False

    def set_servo(self, servo_id: int, pos: int, used_time: int):
        """
        设置舵机
        :param servo_id:舵机号
        :param pos:舵机转动值
        :param used_time:耗时
        :return:
        """
        pos = min(max(pos, self.min_pos), self.max_pos)
        used_time = min(max(used_time, self.min_used_time), self.max_used_time)
        self.serial.write(servo_id, Constant.LOBOT_SERVO_MOVE_TIME_WRITE, pos,
                          used_time)

    def set_deviation(self, servo_id: int, deviation: int):
        """
        设置舵机偏差
        :param servo_id:舵机号
        :param deviation:偏差
        :return:
        """
        if servo_id < self.min_servo_id or servo_id > self.max_servo_id:
            return
        if deviation < self.min_deviation or deviation > self.max_deviation:
            return

        if self.action_status is False:
            self.serial.set_deviation(servo_id, deviation)

    def stop_servo(self):
        """
        :return:
        """
        for servo_id in range(self.min_servo_id, self.max_servo_id):
            self.serial.write(servo_id, Constant.LOBOT_SERVO_MOVE_STOP)

    def stop_action(self):
        self.stop_action = True
        time.sleep(0.1)

    def run_action_file(self, action_name: str, step: int = 1):
        """
        执行动作组
        :param action_name:动作名
        :param step: 运行次数
        :return:
        """
        from ddcmaker.basic.hwax import HWAX
        if action_name is None:
            return
        if self.action_status:
            print("上一个动作还未完成")
            return
        hwax_file = self.file_path.joinpath(f'{action_name}.hwax')
        d6a_file = self.file_path.joinpath(f'{action_name}.d6a')
        if hwax_file.exists():
            self.action_status = True
            self.serial.port_write()
            hwax = HWAX(hwax_file.as_posix(), self.serial.serialHandle)
            hwax.reset()
            for i in range(step):
                while True:
                    if self.stop_action:
                        print('stop')
                        self.stop_action = False
                        break

                    ret = hwax.next()
                    if ret is None:
                        break
            hwax.reset()
            hwax.close()
            self.action_status = False
        elif d6a_file.exists():
            connect = sql.connect(d6a_file.as_posix())
            cursor = connect.cursor()
            cursor.execute("select * from ActionGroup")
            for i in range(step):
                while True:
                    action = cursor.fetchone()
                    if self.stop_action:
                        print('stop')
                        self.stop_action = False
                        break

                    if action is None:
                        break

                    for j in range(0, len(action) - 2, 1):
                        self.set_servo(j + 1, action[2 + j], action[1])
                    # 睡眠的原因时，指令下发是异步的，如果直接下发下一条指令，会覆盖上一条指令
                    time.sleep(action[1] / 1000)
            cursor.close()
            connect.close()
        else:
            print("未能找到动作组文件")


def get_checksum(buf: bytearray) -> int:
    """
    生成校验和
    :param buf:数据buffer
    :return:校验和
    """
    checksum = 0x00
    for b in buf:
        checksum += b
    checksum = checksum - Constant.LOBOT_SERVO_FRAME_HEADER * 2
    checksum = ~checksum
    return checksum & 0xff


if __name__ == '__main__':
    test_serial = Serial()
    test_serial.show_servo_state()
