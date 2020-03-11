import time
from typing import List, Tuple

from ddcmaker.maker.human_code.actions import ai
from ddcmaker.maker.human_code.actions import normal
from ddcmaker.maker.human_code.actions import head
from ddcmaker.maker.human_code.actions import gymnastic
from ddcmaker.maker.human_code.actions import dance
from ddcmaker.maker.human_code.controller import PWMServoController
from ddcmaker.basic.abc.basic_maker import BasicMaker
from ddcmaker.basic.device.servo import Servo
from ddcmaker.basic.device.serial import SerialServoController


class Robot(BasicMaker):
    def __init__(self):
        super().__init__("机器人", sleep_time=1, )
        self.serial_controller = SerialServoController("/home/pi/human_code/ActionGroups/")

        self.pwm_servo_controller = PWMServoController()
        # 头部舵机编号
        # 控制头部上下的舵机
        self.head_vertical = Servo(servo_id=1, init_value=1450, min_value=1090, max_value=1810,
                                   per_angle_to_value=8)
        # 控制头部左右的舵机
        self.head_horizontal = Servo(servo_id=2, init_value=1450, min_value=1090, max_value=1810,
                                     per_angle_to_value=8)
        self.head_joints = [self.head_horizontal, self.head_vertical]
        self.interval_time = 200  # 单位为ms
        self.min_used_time = 0.5
        self.max_used_time = 15

        self.head_to_left_value = 1800  # 向左摆头角度
        self.head_to_right_value = 1200  # 向右摆头角度
        self.head_horizontal_middle_value = 1500  # 水平舵机中间角度

        self.head_up_value = 1800  # 抬头角度
        self.head_down_value = 1200  # 低头角度
        self.head_vertical_middle_value = 1500  # 垂直舵机中间角度

        # 左部关节
        self.left_sole = Servo(servo_id=1, init_value=500, min_value=420, max_value=740, reverse=True)
        self.left_ankle = Servo(servo_id=2, init_value=500, reverse=True)
        self.left_knee = Servo(servo_id=3, init_value=303, min_value=63, max_value=943, reverse=True)
        self.left_vertical_hip = Servo(servo_id=4, init_value=500)
        self.left_horizontal_hip = Servo(servo_id=5, init_value=500)
        self.left_wrist = Servo(servo_id=6, init_value=500, reverse=True)
        self.left_elbow = Servo(servo_id=7, init_value=500, reverse=True)
        self.left_shoulder = Servo(servo_id=8, init_value=725, min_value=85, max_value=985, reverse=True)
        self._left_joints = [
            self.left_sole, self.left_ankle, self.left_knee, self.left_vertical_hip,
            self.left_horizontal_hip, self.left_wrist, self.left_elbow, self.left_shoulder
        ]

        # 右部关节
        self.right_sole = Servo(servo_id=9, init_value=500, min_value=260, max_value=580)
        self.right_ankle = Servo(servo_id=10, init_value=500)
        self.right_knee = Servo(servo_id=11, init_value=697, min_value=57, max_value=937)
        self.right_vertical_hip = Servo(servo_id=12, init_value=500, reverse=True)
        self.right_horizontal_hip = Servo(servo_id=13, init_value=500, reverse=True)
        self.right_wrist = Servo(servo_id=14, init_value=500)
        self.right_elbow = Servo(servo_id=15, init_value=500)
        self.right_shoulder = Servo(servo_id=16, init_value=275, min_value=15, max_value=915)
        self._right_joints = [
            self.right_sole, self.right_ankle, self.right_knee, self.right_vertical_hip,
            self.right_horizontal_hip, self.right_wrist, self.right_elbow, self.right_shoulder
        ]

    def run_action_file(self, action_file_name, step=1, msg=None):
        """
        执行动作组文件
        :param action_file_name:
        :param step:
        :param msg:
        :return:
        """
        for i in range(step):
            self.serial_controller.run_action_file(action_file_name)
            time.sleep(self.sleep_time)
            if msg is not None:
                self.logger(msg)

    def set_servo(self, servo_infos: List[Tuple], used_time: int, msg=None):
        """
        执行动作
        :param servo_infos:舵机信息,[(servo_id,angle)]
        :param used_time:耗时，单位为s
        :param msg: 提示信息
        :return:
        """
        if used_time < self.min_used_time or used_time > self.max_used_time:
            self.logger(f"used_time参数范围非法,有效值{self.min_used_time}-{self.max_used_time}")
            return
        for servo, angle in servo_infos:
            # 舵机执行命令
            if servo in self.head_joints:
                self.pwm_servo_controller.set_servo(
                    servo.servo_id, servo.get_value(angle), int(used_time * 1000))
            elif servo in self._left_joints:
                self.serial_controller.set_servo(
                    servo.servo_id, servo.get_value(angle), int(used_time * 1000))
            elif servo in self._right_joints:
                self.serial_controller.set_servo(
                    servo.servo_id, servo.get_value(angle), int(used_time * 1000))
            else:
                print("非法舵机号")
                return
        time.sleep(used_time)

        if msg is not None:
            self.logger(msg)

    """舞蹈动作"""
    def hip_hop(self):
        """
        舞蹈组——街舞
        """
        dance.hiphop(self)

    def jiang_nan_style(self):
        """
        舞蹈组——江南style
        """
        dance.jiangnanstyle(self)

    def small_apple(self):
        """
        舞蹈组——小苹果
        """
        dance.smallapple(self)

    def la_song(self):
        """
        舞蹈组——LASONG
        """
        dance.lasong(self)

    def feelgood(self):
        """
        舞蹈组——倍儿爽
        """
        dance.feelgood(self)

    def fantastic_baby(self):
        """
        舞蹈组——fantastic baby
        """
        dance.fantastic_baby(self)

    def super_champion(self):
        """
        舞蹈组——super champion
        """
        dance.super_champion(self)

    def youth_cultivation(self):
        """
        舞蹈组——青春修炼手册
        """
        dance.youth_cultivation(self)

    def love_starts(self):
        """
        舞蹈组——爱出发
        """
        dance.Love_starts(self)

    """AI功能"""
    def automatic_shot(self):
        """
        AI组——自动射门
        """
        ai.automatic_shot(self)

    def identifying(self):
        """
        AI组——颜色识别
        """
        ai.identifying(self)

    def find_hand(self):
        """
        AI组——手势识别
        """
        ai.find_hand(self)

    def line_follow(self):
        """
        AI组——自动寻迹
        """
        ai.line_follow(self)

    def tracking(self, color: str):
        """
        AI组——云台跟踪
        """
        ai.tracking(self, color)

    """基本功能"""

    def init_body(self):
        """
        通用组——初始化机器人
        """
        normal.init_body(self)

    def up(self):
        """
        通用组——机器人站立
        """
        normal.up(self)

    def down(self):
        """
        通用组——机器人蹲下
        """
        normal.down(self)

    def check(self):
        """
        通用组——机器人自检
        """
        normal.check(self)

    def forward(self, step):
        """
        通用组——机器人前进
        """
        normal.forward(self, step)

    def backward(self, step):
        """
        通用组——机器人后退
        """
        normal.backward(self, step)

    def left(self, step):
        """
        通用组——机器人左转
        """
        normal.left(self, step)

    def right(self, step):
        """
        通用组——机器人右转
        """
        normal.right(self, step)

    def left_slide(self, step):
        """
        通用组——机器人左滑
        """
        normal.left_slide(self, step)

    def right_slide(self, step):
        """
        通用组——机器人右滑
        """
        normal.right_slide(self, step)

    def push_up(self, step):
        """
        通用组——机器人俯卧撑
        """
        normal.push_up(self, step)

    def abdominal_curl(self, step):
        """
        通用组——机器人仰卧起坐
        """
        normal.abdominal_curl(self, step)

    def wave(self, step):
        """
        通用组——机器人挥手┏(＾0＾)┛
        """
        normal.wave(self, step)

    def bow(self, step):
        """
        通用组——机器人鞠躬╰(￣▽￣)╭
        """
        normal.bow(self, step)

    def spread_wings(self, step):
        """
        通用组——机器人大鹏展翅
        """
        normal.spread_wings(self, step)

    def laugh(self, step):
        """
        通用组——机器人哈哈大笑o(*￣▽￣*)o
        """
        normal.laugh(self, step)

    def straight_boxing(self, step):
        """
        通用组——机器人直拳
        """
        normal.straight_boxing(self, step)

    def lower_hook_combo(self, step):
        """
        通用组——机器人下勾拳
        """
        normal.lower_hook_combo(self, step)

    def left_hook(self, step):
        """
        通用组——机器人左勾拳
        """
        normal.left_hook(self, step)

    def right_hook(self, step):
        """
        通用组——机器人右勾拳
        """
        normal.right_hook(self, step)

    def punching(self, step):
        """
        通用组——机器人攻步冲拳
        """
        normal.punching(self, step)

    def crouching(self, step):
        """
        通用组——机器人八字蹲拳
        """
        normal.crouching(self, step)

    def yongchun(self, step):
        """
        通用组——机器人咏春拳
        """
        normal.yongchun(self, step)

    def beat_chest(self, step):
        """
        通用组——机器人捶胸
        """
        normal.beat_chest(self, step)

    def left_side_kick(self, step):
        """
        通用组——机器人左侧踢
        """
        normal.left_side_kick(self, step)

    def right_side_kick(self, step):
        """
        通用组——机器人右侧踢
        """
        normal.right_side_kick(self, step)

    def left_foot_shot(self, step):
        """
        通用组——机器人左脚射门
        """
        normal.left_foot_shot(self, step)

    def right_foot_shot(self, step):
        """
        通用组——机器人右脚射门
        """
        normal.right_foot_shot(self, step)

    def show_poss(self, step):
        """
        通用组——机器人摆拍poss
        """
        normal.show_poss(self, step)

    def inverted_standing(self, step):
        """
        通用组——机器人前倒站立
        """
        normal.inverted_standing(self, step)

    def rear_stand_up(self, step):
        """
        通用组——机器人后倒站立
        """
        normal.rear_stand_up(self, step)

    """头部"""

    # def head_to_right(self,step):
    #     """
    #     头部——机器人向右看
    #     """
    #     head.head_to_right(self,step)

    # def head_to_left(self,step):
    #     """
    #     头部——机器人向左看
    #     """
    #     head.head_to_left(self,step)

    # def head_to_horizontal_middle(self,step):
    #     head.head_to_horizontal_middle(self,step)
    #
    # def head_to_up(self,step):
    #     """
    #     头部——机器人向上看
    #     """
    #     head.head_to_up(self,step)

    # def head_to_down(self,step):
    #     """
    #     头部——机器人向下看
    #     """
    #     head.head_to_down(self,step)

    # def head_to_vertical_middle(self,step):
    #     head.head_to_vertical_middle(self,step)

    def shaking_head(self, step):
        """
        头部——机器人摇头
        """
        head.shaking_head(self, step)

    def nod(self, step):
        """
        头部——机器人点头
        """
        head.nod(self, step)

    def init_head(self, step):
        """
        头部——机器人正视前方
        """
        head.init_head(self, step)

    """______体操动作______"""

    def gy_keep_down(self, step: int = 1):
        """
        体操——机器人蹲下
        """
        gymnastic.keep_down(self, step)

    def gy_stand_up(self, step: int = 1):
        """
        体操——机器人立正
        """
        gymnastic.stand_up(self, step)

    def gy_akimbo(self, step: int = 1):
        """
        体操——机器人叉腰
        """
        gymnastic.akimbo(self, step)

    def gy_left_hand_up(self, step: int = 1):
        """
        体操——机器人举左手
        """
        gymnastic.left_hand_up(self, step)

    def gy_right_hand_up(self, step: int = 1):
        """
        体操——机器人举右手
        """
        gymnastic.right_hand_up(self, step)

    def gy_left_leg_up(self, step: int = 1):
        """
        体操——机器人迈左腿
        """
        gymnastic.left_leg_up(self, step)

    def gy_right_leg_up(self, step: int = 1):
        """
        体操——机器人迈右腿
        """
        gymnastic.right_leg_up(self, step)

    def gy_head_left(self, step: int = 1):
        """
        体操——机器人向左看
        """
        gymnastic.head_left(self, step)

    def gy_head_right(self, step: int = 1):
        """
        体操——机器人向右看
        """
        gymnastic.head_right(self, step)

    def gy_head_down(self, step: int = 1):
        """
        体操——机器人向下看
        """
        gymnastic.head_down(self, step)

    def gy_head_up(self, step: int = 1):
        """
        体操——机器人向上看
        """
        gymnastic.head_up(self, step)

    def gy_init_head(self, step: int = 1):
        """
        体操——机器人正视前方
        """
        gymnastic.init_head(self, step)

    def gy_hand_up(self, step: int = 1):
        """
        体操——机器人双手高举
        """
        gymnastic.hand_up(self, step)

    def gy_hand_forward(self, step: int = 1):
        """
        体操——机器人双手前举
        """
        gymnastic.hand_forward(self, step)

    def gy_hand_left(self, step: int = 1):
        """
        体操——机器人双手向左
        """
        gymnastic.hand_left(self, step)

    def gy_hand_right(self, step: int = 1):
        """
        体操——机器人双手向右
        """
        gymnastic.hand_right(self, step)

    def gy_applaud_left_leg(self, step: int = 1):
        """
        体操——机器人鼓掌迈左腿
        """
        gymnastic.applaud_left_leg(self, step)

    def gy_applaud_right_leg(self, step: int = 1):
        """
        体操——机器人鼓掌迈右腿
        """
        gymnastic.applaud_right_leg(self, step)

    def gy_hand_up_left_leg_up(self, step: int = 1):
        """
        体操——机器人双手高举迈左腿
        """
        gymnastic.hand_up_left_leg_up(self, step)

    def gy_hand_up_right_leg_up(self, step: int = 1):
        """
        体操——机器人双手高举迈右腿
        """
        gymnastic.hand_up_right_leg_up(self, step)

    def gy_akimbo_right_hand_up(self, step: int = 1):
        """
        体操——机器人举右手左手叉腰
        """
        gymnastic.akimbo_right_hand_up(self, step)

    def gy_akimbo_left_hand_up(self, step: int = 1):
        """
        体操——机器人举左手右手叉腰
        """
        gymnastic.akimbo_left_hand_up(self, step)

    def gy_hand_flat_left_leg_forward(self, step: int = 1):
        """
        体操——机器人双手平举左腿向前
        """
        gymnastic.hand_flat_left_leg_forward(self, step)

    def gy_hand_flat_left_leg_up(self, step: int = 1):
        """
        体操——机器人双手平举向左踢腿
        """
        gymnastic.hand_flat_left_leg_up(self, step)

    def gy_hand_flat_right_leg_forward(self, step: int = 1):
        """
        体操——机器人双手平举右腿向前
        """
        gymnastic.hand_flat_right_leg_forward(self, step)

    def gy_hand_flat_right_leg_up(self, step: int = 1):
        """
        体操——机器人双手平举向右踢腿
        """
        gymnastic.hand_flat_right_leg_up(self, step)

    def gy_hand_up_left_leg_backward(self, step: int = 1):
        """
        体操——机器人双手高举左腿向后
        """
        gymnastic.hand_up_left_leg_backward(self, step)

    def gy_hand_up_right_leg_backward(self, step: int = 1):
        """
        体操——机器人双手高举右腿向后
        """
        gymnastic.hand_up_right_leg_backward(self, step)

    def gy_hand_flat_down(self, step: int = 1):
        """
        体操——机器人双手平举手心向下
        """
        gymnastic.hand_flat_down(self, step)
