from distutils.core import setup

setup(
    name='baizhansupermathhu', # 对外我们模块的名字
    version='1.0', # 版本号
    description='这是第一个对外发布的模块，测试哦', #描述
    author='hushaobo', # 作者
    author_email='157170700@qq.com',
    py_modules=['baizhansupermathhu.demo1','baizhansupermathhu.demo2'] # 要发布的模块
)