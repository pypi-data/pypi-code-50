import pynotepad,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

long_desc="由于上传问题,说明暂无法正常显示。详见模块内的文档字符串。See doc string in this module for more info."

setup(
  name='pynotepad',
  version=pynotepad.__version__,
  description="A simple text editor made by tkinter.一款使用tkinter编写的文本编辑器程序。",
  long_description=pynotepad.__doc__.replace('\n','')+long_desc,
  author=pynotepad.__author__,
  author_email=pynotepad.__email__,
  py_modules=['pynotepad'], #这里是代码所在的文件名称
  keywords=["simple","text","editor","notepad","tkinter"],
  classifiers=[
      'Programming Language :: Python',
      "Topic :: Text Editors"],
)
