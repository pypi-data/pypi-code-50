from distutils.core import setup

setup(
    name="syntt",# 对外我们的模块的名字
    version="1.0", # 版本号
    description="这是对外发布的模块，测试额", # 描述
    author='lslk', # 作者
    author_email= "1967958100@qq.com",
    py_modules=['syntt.demo1','syntt.demo2'] # 要发布的模块
)