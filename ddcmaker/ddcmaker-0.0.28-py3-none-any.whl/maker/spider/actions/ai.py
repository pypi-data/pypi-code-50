_ACTION_FILES = {
    "identifying": "cv_color_stream.py",
    "tracking": "cv_track_stream.py",
    "follow": "cv_color_tracking.py",
    "line_follow": "cv_linefollow.py",
    "balance": "balance.py",
    "sonar": "sonar.py",

}

_CMD_PREFIX = "python3 /home/pi/hexapod/{cmd} no_display {info}"
_SUPPORT_COLOR = ["red", "green", "blue"]


def identifying(spider):
    spider.logger("颜色识别(红色点头，蓝绿摇头)")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('identifying'), info="")
    spider.host_run(cmd)


def tracking(spider, color):
    if color in _SUPPORT_COLOR:
        spider.logger("云台追踪")
        cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('tracking'),
                                 info=color)
        spider.host_run(cmd)
    else:
        raise Exception(f"传入参数{color}超出范围,请在{_SUPPORT_COLOR}中选择")


def follow(spider):
    spider.logger("机体跟随")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('follow'), info="")
    spider.host_run(cmd)


def line_follow(spider):
    spider.logger("自动巡线")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('line_follow'), info="")
    spider.host_run(cmd)


def balance(spider):
    spider.logger("自动平衡")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('balance'), info="")
    spider.host_run(cmd)


def sonar(spider):
    spider.logger("自动避障")
    cmd = _CMD_PREFIX.format(cmd=_ACTION_FILES.get('sonar'), info="")
    spider.host_run(cmd)


