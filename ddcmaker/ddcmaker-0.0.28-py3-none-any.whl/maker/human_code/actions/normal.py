def init_body(robot, step: int = 1):
    robot.run_action_file("0", step=step)


def up(robot, step: int = 1):
    robot.run_action_file("0", step=step, msg="站立")


def down(robot, step: int = 1):
    robot.run_action_file("14", step=step, msg="蹲下")


def check(robot, step: int = 1):
    robot.run_action_file("188", step=step, msg="自检")


def forward(robot, step: int = 1):
    robot.run_action_file("1", step=step, msg="前进")


def backward(robot, step: int = 1):
    robot.run_action_file("2", step=step, msg="后退")


def left(robot, step: int = 1):
    robot.run_action_file("3", step=step, msg="左转")


def right(robot, step: int = 1):
    robot.run_action_file("4", step=step, msg="右转")


def left_slide(robot, step: int = 1):
    robot.run_action_file("11", step=step, msg="左滑")


def right_slide(robot, step: int = 1):
    robot.run_action_file("12", step=step, msg="右滑")


def push_up(robot, step: int = 1):
    robot.run_action_file("7", step=step, msg="俯卧撑")


def abdominal_curl(robot, step: int = 1):
    robot.run_action_file("8", step=step, msg="仰卧起坐")


def wave(robot, step: int = 1):
    robot.run_action_file("9", step=step, msg="挥手┏(＾0＾)┛")


def bow(robot, step: int = 1):
    robot.run_action_file("10", step=step,
                          msg="鞠躬╰(￣▽￣)╭")


def spread_wings(robot, step: int = 1):
    robot.run_action_file("13", step=step, msg="大鹏展翅")


def laugh(robot, step: int = 1):
    robot.run_action_file("15", step=step,
                          msg="哈哈大笑o(*￣▽￣*)o")


def straight_boxing(robot, step: int = 1):
    robot.run_action_file("30", step=step, msg="直拳")


def lower_hook_combo(robot, step: int = 1):
    robot.run_action_file("31", step=step, msg="下勾拳")


def left_hook(robot, step: int = 1):
    robot.run_action_file("32", step=step, msg="左勾拳")


def right_hook(robot, step: int = 1):
    robot.run_action_file("33", step=step, msg="右勾拳")


def punching(robot, step: int = 1):
    robot.run_action_file("34", step=step, msg="攻步冲拳")


def crouching(robot, step: int = 1):
    robot.run_action_file("35", step=step, msg="八字蹲拳")


def yongchun(robot, step: int = 1):
    robot.run_action_file("36", step=step, msg="咏春拳")


def beat_chest(robot, step: int = 1):
    robot.run_action_file("37", step=step, msg="捶胸")


def left_side_kick(robot, step: int = 1):
    robot.run_action_file("50", step=step, msg="左侧踢")


def right_side_kick(robot, step: int = 1):
    robot.run_action_file("51", step=step, msg="右侧踢")


def left_foot_shot(robot, step: int = 1):
    robot.run_action_file("52", step=step, msg="左脚射门")


def right_foot_shot(robot, step: int = 1):
    robot.run_action_file("53", step=step, msg="右脚射门")


def show_poss(robot, step: int = 1):
    robot.run_action_file("60", step=step, msg="摆拍poss")


def inverted_standing(robot, step: int = 1):
    robot.run_action_file("101", step=step, msg="前倒站立")


def rear_stand_up(robot, step: int = 1):
    robot.run_action_file("102", step=step, msg="后倒站立")
