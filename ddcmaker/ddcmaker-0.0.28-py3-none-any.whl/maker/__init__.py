from ddcmaker.basic.abc import get_maker_type, Maker

maker_type = get_maker_type()
if maker_type == Maker.CAR:
    from ddcmaker.maker.car import Car
    from ddcmaker.maker.car import init
    from ddcmaker.maker.car.actions import normal

    init()
elif maker_type == Maker.HUMAN_CODE:
    from ddcmaker.maker.human_code import Robot
    from ddcmaker.maker.human_code import init
    from ddcmaker.maker.human_code.actions import ai
    from ddcmaker.maker.human_code.actions import normal
    from ddcmaker.maker.human_code.actions import head
    from ddcmaker.maker.human_code.actions import gymnastic
    init()
elif maker_type == Maker.HUMAN:
    from ddcmaker.maker.human import Robot
    from ddcmaker.maker.human import init

    init()
elif maker_type == Maker.SPIDER:
    from ddcmaker.maker.spider import Spider
    from ddcmaker.maker.spider import init
    from ddcmaker.maker.spider.actions import normal
    from ddcmaker.maker.spider.actions import ai

    init()
elif maker_type == Maker.UNKNOWN:
    print("该创客设备暂不支持")
