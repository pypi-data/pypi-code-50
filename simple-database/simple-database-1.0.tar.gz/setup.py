import database,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

desc=database.__doc__
long_desc=desc+"  注:由于上传问题,说明暂无法正常显示。详见模块内的文档字符串。See doc string in this module for more info."

setup(
  name='simple-database',
  version=database.__version__,
  description=desc,
  long_description=long_desc,
  author=database.__author__,
  author_email=database.__email__,
  py_modules=['database'], #这里是代码所在的文件名称
  keywords=["database","data"],
  classifiers=[
      'Programming Language :: Python',
      "Natural Language :: Chinese (Simplified)",
      "Topic :: Database"],
)
