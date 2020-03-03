from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="Yatagan",
    version="0.0.1",
    author="Ahmed Selim Üzüm",
    author_email="ahmedselimuzum@gmail.com",
    description="A package to make CTFs easier",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedselim2017/yatagan",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
