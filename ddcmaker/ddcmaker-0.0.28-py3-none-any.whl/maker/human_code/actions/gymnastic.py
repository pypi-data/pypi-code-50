import time

from ddcmaker.maker.human_code.actions import head


def keep_down(robot, step: int = 1):
    robot.run_action_file("gymnastics_keep_down", step, "蹲下")


def stand_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_stand_up", step, "立正")


def akimbo(robot, step: int = 1):
    robot.run_action_file("gymnastics_akimbo", step, "叉腰")


def left_hand_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_left_hand_up", step, "举左手")


def right_hand_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_right_hand_up", step, "举右手")


def left_leg_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_up_left_leg", step, "抬左腿")


def right_leg_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_up_right_leg", step, "抬右腿")


def head_left(robot, step: int = 1):
    for i in range(step):
        head.head_to_left(robot)
        time.sleep(robot.interval_time / 1000)
        robot.logger("左偏头")


def head_right(robot, step: int = 1):
    for i in range(step):
        head.head_to_right(robot)
        time.sleep(robot.interval_time / 1000)
        robot.logger("右偏头")


def head_down(robot, step: int = 1):
    for i in range(step):
        head.head_to_down(robot)
        time.sleep(robot.interval_time / 1000)
        robot.logger("低头")


def head_up(robot, step: int = 1):
    for i in range(step):
        head.head_to_up(robot)
        time.sleep(robot.interval_time / 1000)
        robot.logger("抬头")


def init_head(robot, step: int = 1):
    for i in range(step):
        robot.interval_time = 200
        head.init_head(robot)
        robot.logger("正视前方")


def hand_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_hand_up", step, "双手高举")


def hand_forward(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_flat_forward", step, "双手前举")


def hand_left(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_to_left", step, "双手向左")


def hand_right(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_to_right", step, "双手向右")


def applaud_left_leg(robot, step: int = 1):
    robot.run_action_file("gymnastics_applaud_left_leg", step, "鼓掌左腿向前")


def applaud_right_leg(robot, step: int = 1):
    robot.run_action_file("gymnastics_applaud_right_leg", step, "鼓掌右腿向后")


def hand_up_left_leg_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_curve_hands_left_leg", step, "双手高举迈左腿")


def hand_up_right_leg_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_curve_hands_right_leg", step, "双手高举迈右腿")


def akimbo_right_hand_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_right_hand_up_akimbo", step, "举右手左手叉腰")


def akimbo_left_hand_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_left_hand_up_akimbo", step, "举左手右手叉腰")


def hand_flat_left_leg_forward(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_flat_left_leg_forward", step, "双手平举左腿向前")


def hand_flat_left_leg_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_flat_left_leg_up", step, "双手平举向左踢腿")


def hand_flat_right_leg_forward(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_flat_right_leg_forward", step, "双手平举右腿向前")


def hand_flat_right_leg_up(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_flat_right_leg_up", step, "双手平举向右踢腿")


def hand_up_left_leg_backward(robot, step: int = 1):
    robot.run_action_file("gymnastics_hand_up_left_leg_backward", step, "双手高举左腿向后")


def hand_up_right_leg_backward(robot, step: int = 1):
    robot.run_action_file("gymnastics_hand_up_right_leg_backward", step, "双手高举右腿向后")


def hand_flat_down(robot, step: int = 1):
    robot.run_action_file("gymnastics_hands_flat_down", step, "双手平举脚同肩宽")
