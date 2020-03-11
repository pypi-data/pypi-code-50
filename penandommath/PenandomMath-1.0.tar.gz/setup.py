from distutils.core import setup

setup(
    name='PenandomMath', #对外模块显示的名称
    version='1.0',  #版本号
    description='第一个对外发布的模块，用来测试的哟', #描述
    author='Penandom', #作者名
    author_email='penandom@163.com', #作者邮箱
    py_modules=['penandomMath.demo1', 'penandomMath.demo2'] #要发布的模块
)