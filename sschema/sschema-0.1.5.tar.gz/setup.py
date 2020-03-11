#!/usr/bin/python3

import os
from setuptools import setup
from setuptools.command.install import install
import stat


class FixPermsInstall(install):
    '''Custom install class just to fix permissions for the schema data.'''
    def run(self):
        '''Fix schema data permissions.'''
        install.run(self)

        no_exec_mask = ~(stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        for filepath in self.get_outputs():
            parent = os.path.basename(os.path.dirname(filepath))
            if parent != 'schema':
                continue

            # Open the file so there's no race between the stat and the
            # chmod.
            with open(filepath, 'r') as f:
                fd = f.fileno()
                st = os.fstat(fd)
                os.fchmod(fd, st.st_mode & no_exec_mask)

# Keep the long description in sync with the README.
script_dir = os.path.dirname(os.path.realpath(__file__))
readme_path = os.path.join(script_dir, 'README.md')
with open(readme_path, 'r') as f:
    long_desc = f.read()

setup(
    name='sschema',
    version='0.1.5',
    description='A library and prebuilt schemas for handling edge sensor data',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Martin Kelly',
    author_email='mkelly@xevo.com',
    license='Apache',
    python_requires='>=3',
    install_requires=[
        'PyYAML',
        'simpleeval',
        'jsonschema'
    ],
    packages=['sschema', 'sschema.handler'],
    package_data={'sschema': ['schema/*']},
    cmdclass={
        'install': FixPermsInstall
    },
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Natural Language :: English',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3 :: Only',
                 'Topic :: Software Development :: Embedded Systems',
                 'Topic :: Software Development :: Testing :: Acceptance',
                 ]
)
