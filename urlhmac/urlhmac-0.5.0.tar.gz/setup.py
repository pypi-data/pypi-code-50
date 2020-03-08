#!/usr/bin/env python3
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class TestRunner(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox

        tox.cmdline(self.test_args)


setup(
    author="Florian Ludwig",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    name="urlhmac",
    version="0.5.0",
    url="",
    description="",
    install_requires=[],
    extras_requires={"test": ["pytest"], "docs": ["sphinx_rtd_theme"]},
    packages=["urlhmac"],
    include_package_data=True,
    cmdclass={"test": TestRunner},
)
