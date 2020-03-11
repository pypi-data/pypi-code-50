import timer,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

desc=''.join(timer.__doc__.splitlines()[:2]) #取文档字符串的前两行
long_desc=desc+"  注:由于上传问题,说明暂无法正常显示。详见模块内的文档字符串。See doc string in this module for more info."

setup(
  name='py-timer',
  version=timer.__version__,
  description=desc,
  long_description=long_desc,
  author=timer.__author__,
  author_email=timer.__email__,
  py_modules=['timer'], #这里是代码所在的文件名称
  keywords=["timer","performance analysis"],
  classifiers=[
      'Programming Language :: Python',
      "Natural Language :: Chinese (Simplified)"],
)
