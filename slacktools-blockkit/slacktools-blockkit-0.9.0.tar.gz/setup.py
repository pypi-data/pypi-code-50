from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="slacktools-blockkit",
    version="0.9.0",
    author="Daniel Poland",
    author_email="dan@crispy.dev",
    long_description=long_description,
    url="https://github.com/danpoland/slacktools-blockkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
