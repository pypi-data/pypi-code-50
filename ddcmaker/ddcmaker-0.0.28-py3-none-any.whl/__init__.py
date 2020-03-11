
import platform

__version__ = '0.0.28'
__metaclass__ = type
__all__ = [
    '__init__', "Robot", "Spider", "Car"
]
NAME = 'ddcmaker'

if platform.system() == "Linux":
    from ddcmaker.maker import *
    from ddcmaker.server import *
    from ddcmaker.basic.abc import *
# elif platform.system() == "Windows":
#     from ddcmaker.server import *
#     from ddcmaker.basic.abc import *
else:
    print("当前系统暂不支持！")
