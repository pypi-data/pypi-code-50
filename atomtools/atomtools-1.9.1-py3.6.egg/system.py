"""
get max cores and memory for linux

"""
import sys
import psutil


if sys.platform in ['linux', 'darwin']:
    devnull = open('/dev/null', 'w')
elif sys.platform in ['windows']:
    devnull = open('NUL', 'w')


def kmg_unit(unit):
    unit = unit.upper()
    ALL_UNITS = ['TB', "GB", "MB", "KB"]
    assert unit in ALL_UNITS
    num = 1
    flag = False
    for this_unit in ALL_UNITS:
        if this_unit == unit or flag:
            num *= 1024
            flag = True
    return num


def get_maxcore():
    return round(psutil.cpu_count()*(1-psutil.cpu_percent()/100))


def get_maxmem(unit=None):
    mem = psutil.virtual_memory().available * 0.9
    if unit:
        return mem / kmg_unit(unit)
    return mem
