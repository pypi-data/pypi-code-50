

import setuptools


long_description = """
自动化网盘管理工具，支持百度云盘、谷歌云盘、坚果云等多个网盘的文件管理，自动上传和下载，分享链接自动保存等。
"""


setuptools.setup(
    name='py_cloud',
    version='1.0.0',
    description='A toolkit for automatic cloud disk management',
    long_description=long_description,
    author='dandanlemuria',
    author_email='18110980003@fudan.edu.cn',
    url='https://github.com/LemuriaChen/pycloud',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],
    keywords='cloud disk, download, upload, share',
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium==3.141.0',
    ],
)
