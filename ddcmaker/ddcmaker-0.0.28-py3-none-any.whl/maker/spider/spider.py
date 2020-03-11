import time
from typing import List, Tuple

from ddcmaker.maker.spider.actions import ai, normal

from ddcmaker.basic.device.serial import SerialServoController
from ddcmaker.basic.abc.basic_maker import BasicMaker


class Spider(BasicMaker):
    def __init__(self):
        super().__init__("蜘蛛", sleep_time=1)
        self.serial_controller = SerialServoController("/home/pi/hexapod/ActionGroups/")

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
            self.logger(msg)

    def set_servo(self, servo_infos: List[Tuple], used_time: int):
        self.logger("暂不支持")

    """ai动作"""

    def identifying(self):
        ai.identifying(self)

    def tracking(self, color: str):
        ai.tracking(self, color)

    def follow(self):
        ai.follow(self)

    def line_follow(self):
        ai.line_follow(self)

    def balance(self):
        ai.balance(self)

    def sonar(self):
        ai.sonar(self)

    """基本动作"""

    def init_body(self):
        normal.init_body(self)

    def creeping(self):
        normal.creeping(self)

    def creeping_forward(self):
        normal.creeping_forward(self)

    def creeping_backward(self):
        normal.creeping_backward(self)

    def creeping_left(self):
        normal.creeping_left(self)

    def creeping_right(self):
        normal.creeping_right(self)

    def stand(self):
        normal.stand(self)

    def forward(self):
        normal.forward(self)

    def backward(self):
        normal.backward(self)

    def left(self):
        normal.left(self)

    def right(self):
        normal.right(self)

    def towering(self):
        normal.towering(self)

    def towering_forward(self):
        normal.towering_forward(self)

    def towering_backward(self):
        normal.towering_backward(self)

    def towering_left(self):
        normal.towering_left(self)

    def towering_right(self):
        normal.towering_right(self)

    def forward_flutter(self):
        normal.forward_flutter(self)

    def backward_flutter(self):
        normal.backward_flutter(self)

    def left_shift(self):
        normal.left_shift(self)

    def right_shift(self):
        normal.right_shift(self)

    def twisting(self):
        normal.twisting(self)
