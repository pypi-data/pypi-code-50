"""A simple python timer module.
一个简单的Python计时器模块,其中包含Timer类。

示例1:
import timer
t=timer.Timer() #初始化Timer对象
do_something()
t.printtime() #输出执行do_something()所用时间

示例2:
import timer
with timer.Timer(): #在这里开始计时
    do_something()
#退出with语句时自动打印出所用时间。
"""
import time

__email__="3416445406@qq.com"
__author__="七分诚意 qq:3076711200 邮箱:%s"%__email__
__version__="1.1"

class Timer:
    "一个计时器类"
    def __init__(self):
        self.start()
    def start(self):
        "开始计时"
        self.time=time.perf_counter()
    __enter__=start
    def gettime(self):
        "获取从计时开始之后的时间"
        return time.perf_counter()-self.time
    def printtime(self,fmt_str="用时:{:.8f}秒"):
        "打印gettime获取的值"
        print(fmt_str.format(self.gettime()))
    def __exit__(self,*args):
        self.printtime()

def test():
    t=Timer()
    t.printtime(fmt_str="计时器启动用时:{:.8f}秒")

if __name__=="__main__":
    test()
