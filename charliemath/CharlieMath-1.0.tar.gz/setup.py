from distutils.core import setup

setup(
    name="CharlieMath",   #对外我们模块的名字
    version='1.0',    #版本号
    description='这是第一个对外发布的模块，里面只有数学方法，要于测试哦',   #描述
    author='haoguangchen',   #作者
    author_email='561909738@qq.com',
    py_modules = ['CharlieMath.demo1','CharlieMath.demo2'] #要发布的模块
)