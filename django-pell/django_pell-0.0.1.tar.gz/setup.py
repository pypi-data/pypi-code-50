from setuptools import setup, find_packages
from subprocess import Popen

import sys
import shutil


VERSION = "0.0.1"


if sys.argv[-1] == "publish":
    print("Publishing django-pell")

    process = Popen(["python", "setup.py", "sdist"])
    process.wait()

    process = Popen(["twine", "upload", "dist/"])
    process.wait()


if sys.argv[-1] == "test":
    print("Running tests only on current environment.")

    process = Popen(["pytest", "--cov=django_pell", "--cov-report=html"])
    process.wait()

    sys.exit()


with open("README.md") as f:
    readme = f.read()


setup(
    name="django_pell",
    version="0.0.1",
    description="Django pell WYSIWYG widget",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Bradley Stuart Kirton",
    author_email="bradleykirton@gmail.com",
    url="https://gitlab.com/BradleyKirton/django-pell/",
    license="MIT",
    packages=find_packages(exclude=["tests", "example"]),
    include_package_data=True,
    install_requires=["django"],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pytest-sugar",
            "django-coverage-plugin",
            "pytest-django",
            "bumpversion",
            "twine",
        ]
    },
    zip_safe=False,
    keywords="django",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
    ],
)
