import catch_turtle,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

#缺少模块turtle时引发异常,停止安装
try:import turtle
except ImportError:
    raise NotImplementedError("Module turtle required")

info="%s 作者: %s"%(catch_turtle.__doc__,catch_turtle.__author__)

setup(
  name='catch_turtle',
  version=catch_turtle.__version__,
  description=info.splitlines()[0]+\
    " A game that made by using the *turtle* module.",
  long_description=info.replace('\n',''),
  author=catch_turtle.__author__,#作者
  author_email=catch_turtle.__email__,
  platform="win32",
  packages=['catch_turtle'], #这里是所有代码所在的文件夹名称
)
