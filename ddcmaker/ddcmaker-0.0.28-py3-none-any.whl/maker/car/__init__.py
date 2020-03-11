from ddcmaker.maker.car.car import Car
from ddcmaker.maker.car.actions import normal


def init():
    normal_car = Car()
    normal_car.run_action(normal.stop)
