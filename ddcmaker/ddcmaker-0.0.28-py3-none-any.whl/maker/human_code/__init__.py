from ddcmaker.maker.human_code.actions import normal
from ddcmaker.maker.human_code.actions import head
from ddcmaker.maker.human_code.robot import Robot


def init():
    normal_car = Robot()
    normal_car.run_action(normal.init_body)
    normal_car.run_action(head.init_head)
