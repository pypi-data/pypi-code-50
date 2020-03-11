import time


def left(car, used_time: [int, float] = 1, speed: int = 50):
    if used_time > 30 or used_time < 0:
        raise Exception("单次运行时间参数")
    elif speed < 0:
        raise Exception("速度参数必须大于0")
    else:
        car.left_motor.forward(speed)
        car.right_motor.backward(speed)
        time.sleep(used_time)
        stop(car)


def right(car, used_time: [int, float] = 1, speed: int = 50):
    if used_time > 30 or used_time < 0:
        raise Exception("单次运行时间参数")
    elif speed < 0:
        raise Exception("速度参数必须大于0")
    else:
        car.right_motor.forward(speed)
        car.left_motor.backward(speed)
        time.sleep(used_time)
        stop(car)


def forward(car, used_time: [int, float] = 1, speed: int = 50):
    if used_time > 30 or used_time < 0:
        raise Exception("单次运行时间参数")
    elif speed < 0:
        raise Exception("速度参数必须大于0")
    else:
        car.left_motor.forward(speed)
        car.right_motor.forward(speed)
        time.sleep(used_time)
        stop(car)


def backward(car, used_time: [int, float] = 1, speed: int = 50):
    if used_time > 30 or used_time < 0:
        raise Exception("单次运行时间参数")
    elif speed < 0:
        raise Exception("速度参数必须大于0")
    else:
        car.left_motor.backward(speed)
        car.right_motor.backward(speed)
        time.sleep(used_time)
        stop(car)


def stop(car, used_time: int = 1, speed: int = 50):
    _, _ = used_time, speed
    car.right_motor.stop()
    car.left_motor.stop()
