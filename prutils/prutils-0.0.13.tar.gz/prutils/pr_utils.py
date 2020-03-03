import logging
import sys

def init_log(level=logging.DEBUG, filename=None, filemode="w"):
    """

    :param level:
    :param filename: 日志文件路径，默认为None不写文件，
    :param filemode: 可选w覆盖模式,或a添加模式
    """
    logging.basicConfig(level=level,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                        filename=filename,
                        filemode=filemode
                        )
def hello():
    print("hello args[%s]" % (sys.argv, ))


def world():
    print("world args[%s]" % (sys.argv, ))
