import time


def head_to_left(robot, step: int = 1):
    for i in range(step):
        robot.pwm_servo_controller.set_servo(robot.head_horizontal.servo_id,
                                             robot.head_to_left_value,
                                             robot.interval_time)
        time.sleep(robot.interval_time / 1000)
        # robot.logger("向左看")


def head_to_right(robot, step: int = 1):
    for i in range(step):
        robot.pwm_servo_controller.set_servo(robot.head_horizontal.servo_id,
                                             robot.head_to_right_value, robot.interval_time)
        time.sleep(robot.interval_time / 1000)
        # robot.logger("向右看")


def head_to_horizontal_middle(robot, step: int = 1):
    for i in range(step):
        robot.pwm_servo_controller.set_servo(robot.head_horizontal.servo_id,
                                             robot.head_horizontal_middle_value,
                                             int(robot.interval_time / 2))
        time.sleep(robot.interval_time / 1000)


def head_to_up(robot, step: int = 1):
    for i in range(step):
        robot.pwm_servo_controller.set_servo(robot.head_vertical.servo_id,
                                             robot.head_up_value,
                                             robot.interval_time)
        time.sleep(robot.interval_time / 1000)
        # robot.logger("向上看")


def head_to_down(robot, step: int = 1):
    for i in range(step):
        robot.pwm_servo_controller.set_servo(robot.head_vertical.servo_id,
                                             robot.head_down_value,
                                             robot.interval_time)
        time.sleep(robot.interval_time / 1000)
        # robot.logger("向下看")


def head_to_vertical_middle(robot, step: int = 1):
    for i in range(step):
        robot.pwm_servo_controller.set_servo(robot.head_vertical.servo_id,
                                             robot.head_vertical_middle_value,
                                             int(robot.interval_time / 2))
        time.sleep(robot.interval_time / 1000)


def shaking_head(robot, step: int = 1):
    for i in range(step):
        head_to_left(robot)
        time.sleep(robot.interval_time / 1000)
        head_to_right(robot)
        time.sleep(robot.interval_time / 1000)
        head_to_horizontal_middle(robot)
        time.sleep(robot.interval_time / 200)
        robot.logger("摇头")


def nod(robot, step: int = 1):
    for i in range(step):
        head_to_up(robot)
        time.sleep(robot.interval_time / 1000)
        head_to_down(robot)
        time.sleep(robot.interval_time / 1000)
        head_to_vertical_middle(robot)
        time.sleep(robot.interval_time / 1000)
        robot.logger("点头")


def init_head(robot, step: int = 1):
    for i in range(step):
        head_to_vertical_middle(robot)
        # time.sleep(robot.interval_time / 200)
        head_to_horizontal_middle(robot)
        # time.sleep(robot.interval_time / 1000)
        # robot.logger("正视前方")
