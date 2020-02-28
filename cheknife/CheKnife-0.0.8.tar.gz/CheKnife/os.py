import os


def get_sys_id():
    uname = os.uname()
    return f'{uname[0]} {uname[4]}'
