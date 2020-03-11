_ACTION_FILES = {
    "automatic_shot": "cv_find_stream.py",
    "identifying": "cv_color_stream.py",
    "find_hand": "cv_find_hand.py",
    "line_follow": "cv_line_patrol.py",
    "tracking": "cv_track_stream.py",
}

_CMD_PREFIX = "python3 /home/pi/human_code/{cmd} no_display {info}"
_SUPPORT_COLOR = ["red", "green", "blue"]


def automatic_shot(robot):
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('automatic_shot'),
                             info="")
    robot.host_run(cmd)
    robot.logger("自动射门")


def identifying(robot):
    robot.logger("颜色识别(红色点头，蓝绿摇头)")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('identifying'), info="")
    robot.host_run(cmd)


def find_hand(robot):
    robot.logger("手势识别")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('find_hand'), info="")
    robot.host_run(cmd)


def line_follow(robot):
    robot.logger("自动巡线")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('line_follow'), info="")
    robot.host_run(cmd)


def tracking(robot, color):
    if color in _SUPPORT_COLOR:
        robot.logger("云台追踪")
        cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('tracking'),
                                 info=color)
        robot.host_run(cmd)
    else:
        raise Exception(f"传入参数{color}超出范围,请在{_SUPPORT_COLOR}中选择")

# AUTOMATIC_SHOT = CV.automatic_shot
# IDENTIFYING = CV.identifying
# FIND_HAND = CV.find_hand
# LINE_FOLLOW = CV.line_follow
# TRACKING = CV.tracking
