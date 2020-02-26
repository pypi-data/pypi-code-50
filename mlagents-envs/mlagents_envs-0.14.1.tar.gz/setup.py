import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
import mlagents_envs

VERSION = mlagents_envs.__version__

here = os.path.abspath(os.path.dirname(__file__))


class VerifyVersionCommand(install):
    """
    Custom command to verify that the git tag matches our version
    See https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
    """

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setup(
    name="mlagents_envs",
    version=VERSION,
    description="Unity Machine Learning Agents Interface",
    url="https://github.com/Unity-Technologies/ml-agents",
    author="Unity Technologies",
    author_email="ML-Agents@unity3d.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=[
        "cloudpickle",
        "grpcio>=1.11.0",
        "numpy>=1.13.3,<2.0",
        "Pillow>=4.2.1",
        "protobuf>=3.6",
    ],
    python_requires=">=3.5",
    cmdclass={"verify": VerifyVersionCommand},
)
