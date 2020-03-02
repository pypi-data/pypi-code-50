from setuptools import setup
#from . import replacess_pycahr

packages = ["smart"]
setup(
    name="pycahrm_external",  # 包名称
    version="1.1.2",  # 包版本
    description="pycahrm external tools",  # 包详细描述
    long_description="引号替换",  # 长描述，通常是readme，打包到PiPy需要
    author="QQ：2920007919",  # 作者名称
    author_email="2920007919@qq.com",  # 作者邮箱
    url="http://106.12.87.246:8080/myhotupdate/homepage/",  # 项目官网
    packages=packages,
    python_requires=">=2.7",  # Python版本依赖
    # install_requires=pyperclip,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    classifiers=[  # 程序的所属分类列表
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
