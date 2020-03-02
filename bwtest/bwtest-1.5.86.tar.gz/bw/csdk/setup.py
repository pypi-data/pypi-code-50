# coding=utf-8
from __future__ import print_function

import glob
import os
import shutil
from distutils.core import setup
from distutils.extension import Extension
from distutils.util import get_platform

from Cython.Distutils import build_ext

remove_files = ['cpp_sdk.cpp', 'cpp_sdk.pyd',
                'cpp_sdk.cp36-win32.pyd', 'cpp_sdk.cp36-win_amd64.pyd',
                'cpp_sdk.cp37-win32.pyd', 'cpp_sdk.cp37-win_amd64.pyd',
                'libbw3.so', 'bwsdk.dll']
for f in remove_files:
    if os.path.exists(f):
        os.remove(f)

platform = get_platform()
dlllibdir = './lib/{}'.format(platform)
ext_modules = [Extension("cpp_sdk",
                     ["cpp_sdk.pyx"],
                     language='c++',
                     include_dirs=['./include'],
                     library_dirs=[dlllibdir],
                     libraries=["bwsdk"],
                     extra_compile_args=['/MT']
                     )]

setup(
  name='cpp_sdk',
  cmdclass={'build_ext': build_ext},
  ext_modules=ext_modules,
)

dllext = '*.dll'
if platform.startswith('linux'):
    dllext = '*.so'
dllfiles = glob.iglob(os.path.join('./lib/{}/'.format(platform), dllext))
for f in dllfiles:
    if os.path.isfile(f):
        shutil.copy2(f, './{}'.format(os.path.split(f)[1]))
