# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Packages tflite_support python scripts and libraries."""

import glob
import os
import sys
import setuptools
from setuptools import Extension
from setuptools import setup
from setuptools.command.build_ext import build_ext

# Do not rename "_VERSION", as build_pip_package.sh depends on it.
_VERSION = '0.1.0a0.dev3'

_DESCRIPTION = """TFLite Support is a toolkit that helps users to develop ML and deploy TFLite models onto mobile devices. It consists of the following major components:
 - TFLite Support Util Library: a cross-platform library that helps to deploy TFLite models onto mobile devices.
 - TFLite Model Metadata: includes both human and machine readable information about what a model does and how to use the model.
 - TFLite Support Codegen: an executable that generates model interface automatically based on the TFLite Metadata and the Support Util Library. The model interface comes with high level APIs to interact with the model, such as loading and processing data, running inference, etc.

This PyPI package includes the Python bindings for following features:
 - Metadata populator and displayer: can be used to populate the metadata and associated files into the model, as well as converting the populated metadata into the json format.
 - Android Codegen tool: generates the Java model interface used in Android for a particular model.
"""


class PybindInclude(object):
  """Helper class to determine the pybind11 include path.

  The purpose of this class is to postpone importing pybind11
  until it is actually installed, so that the ``get_include()``
  method can be invoked.
  """

  def __init__(self, user=False):
    self.user = user

  def __str__(self):
    import pybind11  # pylint: disable=g-import-not-at-top
    return pybind11.get_include(self.user)


TFLS_SRC_PATH = os.path.join('src', 'tensorflow', 'lite', 'experimental',
                             'support')
ext_modules = [
    Extension(
        '_pywrap_codegen',
        # Not using recursive glob as it's python3 only
        glob.glob(os.path.join(TFLS_SRC_PATH, 'codegen', '*.cc')),
        include_dirs=[
            PybindInclude(),
            PybindInclude(user=True),
            'include',
            'src',
        ],
        language='c++'),
    Extension(
        '_pywrap_flatbuffers',
        glob.glob(os.path.join(TFLS_SRC_PATH, 'metadata', '*.cc')) +
        glob.glob(os.path.join('src', 'flatbuffers', '*.cpp')),
        include_dirs=[
            PybindInclude(),
            PybindInclude(user=True),
            'include',
            'src',
        ],
        language='c++'),
]


# As of Python 3.6, CCompiler has a `has_flag` method.
# cf http://bugs.python.org/issue26689
def has_flag(compiler, flagname):
  """Return a boolean indicating whether a flag name is supported on  the specified compiler."""
  import tempfile  # pylint: disable=g-import-not-at-top
  with tempfile.NamedTemporaryFile('w', suffix='.cc') as f:
    f.write('int main (int argc, char **argv) { return 0; }')
    try:
      compiler.compile([f.name], extra_postargs=[flagname])
    except setuptools.distutils.errors.CompileError:
      return False
  return True


def cpp_flag(compiler):
  """Return the -std=c++[11/14] compiler flag."""
  flags = ['-std=c++14',
           '-std=c++11']  # disable c++17 because of pybind11 compilation error

  for flag in flags:
    if has_flag(compiler, flag):
      return flag

  raise RuntimeError('Unsupported compiler -- at least C++11 support '
                     'is needed!')


class BuildExt(build_ext):
  """A custom build extension for adding compiler-specific options."""
  c_opts = {
      'msvc': ['/EHsc'],
      'unix': [],
  }
  l_opts = {
      'msvc': [],
      'unix': [],
  }

  if sys.platform == 'darwin':
    darwin_opts = ['-stdlib=libc++', '-mmacosx-version-min=10.7']
    c_opts['unix'] += darwin_opts
    l_opts['unix'] += darwin_opts

  def build_extensions(self):
    ct = self.compiler.compiler_type
    opts = self.c_opts.get(ct, [])
    link_opts = self.l_opts.get(ct, [])
    if ct == 'unix':
      opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
      opts.append(cpp_flag(self.compiler))
      if has_flag(self.compiler, '-fvisibility=hidden'):
        opts.append('-fvisibility=hidden')
    elif ct == 'msvc':
      opts.append('/DVERSION_INFO=\\"%s\\"' % self.distribution.get_version())
    for ext in self.extensions:
      ext.extra_compile_args = opts
      ext.extra_link_args = link_opts
    build_ext.build_extensions(self)


setup(
    name='tflite-support',
    version=_VERSION,
    author='Google, LLC',
    author_email='packages@tensorflow.org',
    description='TFLite Support is a toolkit that helps users to develop ML and deploy TFLite models onto mobile devices.',
    long_description=_DESCRIPTION,
    packages=['tflite_support'],
    ext_modules=ext_modules,
    ext_package='tflite_support',
    entry_points={
        'console_scripts': ['tflite_codegen=tflite_support.codegen:main']
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['pybind11>=2.4', 'absl-py>=0.7.0'],
    setup_requires=['pybind11>=2.4'],
    cmdclass={'build_ext': BuildExt},
    include_package_data=True,
    zip_safe=False,
)
