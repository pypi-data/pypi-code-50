# fmt: off
# This file is automatically generated, DO NOT EDIT

from os.path import abspath, join, dirname
_root = abspath(dirname(__file__))

libinit_import = "wpilib._init_wpilib"
depends = ['wpiHal', 'wpiutil', 'ntcore', 'wpilibc', 'wpilibc_interfaces']
pypi_package = 'wpilib'

def get_include_dirs():
    return [join(_root, "include"), join(_root, "rpy-include"), join(_root, "src")]

def get_library_dirs():
    return []

def get_library_dirs_rel():
    return []

def get_library_names():
    return []

def get_library_full_names():
    return []