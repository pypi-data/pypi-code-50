from setuptools import setup

setup(
    name="prichardassets",
    version="1.3",
    description="A module with a static file in it",
    author="prichard",
    author_email="philippe.richard93@gmail.com",
    include_package_data=True,
    packages=['prichardassets'],
    package_data={'prichardassets': ['*.txt']},
    install_requires=[],
)
