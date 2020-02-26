import io
import os
from subprocess import run, PIPE

from setuptools import setup

NAME = "ngm"
DESCRIPTION = "A simple localhost web page creator ngm-sms-spm spam"
URL = ""
EMAIL = "neogenius14@gmail.com"
AUTHOR = "Elermond"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "3.5.1"

REQUIRED = ["aiohttp", "phonenumbers", "click"]

if "ANDROID_DATA" in os.environ:  # If device is running Termux
    run(
        ["pkg", "install", "clang"], stdout=PIPE, input="y\n", encoding="ascii",
    )

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["ngm"],
    entry_points={
        'console_scripts': ['ngm=ngm.__main__:main'],
    },
    install_requires=REQUIRED,
    extras_require={},
    package_data={"ngm": ["static/*/*", "templates/*", "services/*"]},
    license="Mozilla Public License 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
