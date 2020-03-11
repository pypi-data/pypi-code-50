import console_tool,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

long_desc="由于上传问题,说明暂无法正常显示。详见模块内的文档字符串。See doc string in this module for more info."

setup(
  name='console-tool',
  version=console_tool.__version__,
  description=console_tool.__doc__.replace('n',''),
  long_description=long_desc,
  author=console_tool.__author__,
  author_email=console_tool.__email__,
  py_modules=['console_tool'], #这里是代码所在的文件名称
  keywords=["terminal","command-line","console"],
  classifiers=[
      'Environment :: Console',
      'Programming Language :: Python',
      "Topic :: Terminals"],
  install_requires=["colorama","termcolor"]
)