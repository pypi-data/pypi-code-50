import time

one_second_return = 'abcde'
fifty_return = [1, 2, 3, 4, 5]


def one_second():
    time.sleep(1)
    return one_second_return


def fifty_ms():
    time.sleep(0.05)
    return fifty_return


def user_time(dur, **kwargs):
    time.sleep(dur)
    return kwargs


def five_second():
    time.sleep(5.)
    return fifty_return


def erronious():
    raise ValueError('you did something horrific and it broke the code')


def passthrough(*args, **kwargs):
    return args, kwargs
