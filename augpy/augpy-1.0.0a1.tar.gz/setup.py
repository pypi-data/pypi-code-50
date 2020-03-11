import os
import os.path as pt
import sysconfig
import multiprocessing
from math import log2
import re

from setuptools import setup
from setuptools import find_packages
from setuptools import Extension
from setuptools.command.build_ext import build_ext

from generate_saturate_cast_cuh import generate_saturate_cast_cuh


PACKAGE_DIR = pt.abspath(pt.dirname(__file__))


class CMakeExtension(Extension):
    def __init__(self, name, cmake_root):
        # don't invoke the original build_ext for this special extension
        super().__init__(name, sources=[])
        self.cmake_root = cmake_root


def cvar(name):
    return sysconfig.get_config_var(name)


class cmake_build_ext(build_ext):
    user_options = build_ext.user_options + [
        # The format is (long option, short option, description).
        ('cuda-ccs=', None, "CUDA compute capabilities to build for "
                            "(separated by ';'), defaults to '60;61;70;75'"),
        ('jobs=', 'j', 'number of parallel build processes')
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        super().initialize_options()
        # noinspection PyAttributeOutsideInit
        self.cuda_ccs = '60;61;70;75'
        # noinspection PyAttributeOutsideInit
        self.jobs = int(4*log2(multiprocessing.cpu_count())-2)

    def run(self):
        # build cmake extensions separately
        cmake_exts = [ext for ext in self.extensions
                      if isinstance(ext, CMakeExtension)]
        for ext in cmake_exts:
            self.extensions.remove(ext)
            self.build_cmake(ext)
        # build other extensions
        super().run()
        # add cmake extensions
        self.extensions.extend(cmake_exts)

    def build_cmake(self, ext):
        import pybind11

        ext_dir = pt.abspath(pt.dirname(self.get_ext_fullpath(ext.name)))
        if not pt.exists(ext_dir):
            os.makedirs(ext_dir)
        cur_dir = pt.abspath(os.curdir)
        build_dir = pt.join(self.build_temp, ext.name)
        if not pt.exists(build_dir):
            os.makedirs(build_dir)
        os.chdir(build_dir)

        config = 'Debug' if self.debug else 'Release'
        include_dirs = [
            pybind11.get_include(True),
            pybind11.get_include(),
            cvar('INCLUDEPY'),
        ]
        link_flags = cvar('LINKFORSHARED').split(' ')
        link_flags.append('-Wl,--strip-all,--exclude-libs,ALL')
        suffix = cvar('EXT_SUFFIX')
        generate_saturate_cast_cuh()
        self.spawn([
            'cmake',
            '-DCMAKE_BUILD_TYPE=' + config,
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + ext_dir,
            '-DPYLINKOPTIONS=' + ';'.join(link_flags),
            '-DPYINCLUDE=' + ';'.join(include_dirs),
            '-DPYSUFFIX=' + suffix,
            '-DCUDA_CCS=' + self.cuda_ccs,
            pt.join(PACKAGE_DIR, ext.cmake_root),
        ])
        if not self.dry_run:
            self.spawn([
                'cmake',
                '--build',
                '.',
                '--config', config,
                '--',
                '-j%s' % self.jobs
            ])
        os.chdir(cur_dir)


ext_modules = [
    CMakeExtension('augpy._augpy', 'augpy'),
]


packages = find_packages(
    include=['augpy', 'augpy.*'],
    exclude=[]
)


package_data = {
    package: [
        # '*.txt',
        # '*.json'
    ]
    for package in packages
}


with open(pt.join(PACKAGE_DIR, 'requirements.txt')) as f:
    dependencies = [l.strip(' \n') for l in f]


with open(pt.join(PACKAGE_DIR, 'build-requirements.txt')) as f:
    build_dependencies = [l.strip(' \n') for l in f]


with open(pt.join(PACKAGE_DIR, 'README.rst')) as f:
    description = f.read()


def read(*names):
    with open(pt.join(PACKAGE_DIR, *names), encoding='utf8') as f:
        return f.read()


# pip's single-source version method as described here:
# https://python-packaging-user-guide.readthedocs.io/single_source_version/
def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='augpy',
    version=find_version('augpy', '__init__.py'),
    author='Joachim Folz',
    author_email='joachim.folz@dfki.de',
    description='Lightweight CUDA tensor functions with a focus on image data augmentation.',
    long_description=description,
    long_description_content_type='text/x-rst; charset=UTF-8',
    keywords='CUDA tensor math data augmentation image affine warp transform gaussian blur gamma correction',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    ext_modules=ext_modules,
    packages=packages,
    package_data=package_data,
    setup_requires=build_dependencies,
    install_requires=dependencies,
    cmdclass={'build_ext': cmake_build_ext},
    zip_safe=False,
    project_urls={
        'Documentation': 'https://gitlab.com/jfolz/augpy/blob/master/README.rst',
        'Source': 'https://gitlab.com/jfolz/augpy',
        'Tracker': 'https://gitlab.com/jfolz/augpy/issues',
    },
)
