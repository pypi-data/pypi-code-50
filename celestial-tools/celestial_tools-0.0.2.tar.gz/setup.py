from setuptools import setup
from os import path, getenv
from sys import exit
from setuptools.command.install import install

here = path.abspath(path.dirname(__file__))

VERSION_MAJOR = 0
VERSION_MINOR = 0
VERSION_BUGFIX = 2
VERSION_STRING = "{}.{}.{}".format(VERSION_MAJOR, VERSION_MINOR, VERSION_BUGFIX)

TAG_ENV_VARIABLE = 'CIRCLE_TAG'
TAG_VERSION_PREFIX = "celestial_tools_"

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = getenv(TAG_ENV_VARIABLE, "")
        # Make sure the tag starts with "celestial_tools_
        if not tag.startswith(TAG_VERSION_PREFIX):
            info = "Git tag: {0} is not formatted correctly".format(
                tag
            )
            exit(info)
        # Make sure the version after "celestial_tools_" matches our VERSION_STRING
        if tag[len(TAG_VERSION_PREFIX):] != VERSION_STRING:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION_STRING
            )
            exit(info)


setup(
    name='celestial_tools',
    version=VERSION_STRING,
    description='A collection of tools for managing and debugging embedded software',  # Optional
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pseudodesign/celestial',
    author='PseudoDesign',
    author_email='info@pseudo.design',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=["celestial_tools"],
    python_requires='>=3.5',
    install_requires=[],
    extras_require={
        'test': ['coverage', 'behave'],
        'docs': ['sphinx'],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={

    },
    entry_points={
        'console_scripts': [
            'celestial_dual_rootfs_update=celestial_tools.client.dual_rootfs_update:dual_rootfs_update_cmdline',
        ],
    },
    cmdclass={
        'verify_tag': VerifyVersionCommand,
    }
)
