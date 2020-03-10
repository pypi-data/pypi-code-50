import music_score,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

long_desc="详见模块内的文档字符串。See doc string in this module for more info."

setup(
  name='music-score',
  version=music_score.__version__,
  description=music_score.__doc__,
  long_description=long_desc,
  author=music_score.__author__,
  author_email=music_score.__email__,
  py_modules=['music_score'], #这里是代码所在的文件名称
  keywords=["terminal","command-line","console"],
  classifiers=[
      'Environment :: Console',
      'Programming Language :: Python',
      "Topic :: Terminals"],
  install_requires=["console-tool"]
)
