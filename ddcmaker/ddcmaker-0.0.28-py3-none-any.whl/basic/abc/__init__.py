from ddcmaker.basic.abc.basic_maker import BasicMaker
import enum
import os


class Maker(enum.Enum):
    UNKNOWN = -1
    HUMAN = 0
    CAR = 1
    HUMAN_CODE = 2
    SPIDER = 3


MAKER_PATH_DICT = {
    "/home/pi/human": Maker.HUMAN,  # 黑色机器人，现已不再更新
    "/home/pi/Car": Maker.CAR,
    "/home/pi/human_code": Maker.HUMAN_CODE,  # 白色机器人
    "/home/pi/spider": Maker.SPIDER
}

MAKER_NAME_DICT = {
    Maker.UNKNOWN: "",
    Maker.HUMAN: "机器人",  # 黑色机器人
    Maker.CAR: "无人车",
    Maker.HUMAN_CODE: "机器人",  # 白色机器人
    Maker.SPIDER: "六足蜘蛛"}

MAKER_TYPE_INT = {
    "/home/pi/human": 0,
    "/home/pi/Car": 1,
    "/home/pi/human_code": 0,
    "/home/pi/spider": 2
}


def get_maker_type():
    for key in MAKER_PATH_DICT.keys():
        if os.path.exists(key):
            return MAKER_PATH_DICT[key]
    return -1


def get_maker_name():
    return MAKER_NAME_DICT[get_maker_type()]


def get_type_int():
    for key in MAKER_TYPE_INT.keys():
        if os.path.exists(key):
            return MAKER_TYPE_INT[key]
    return -1
