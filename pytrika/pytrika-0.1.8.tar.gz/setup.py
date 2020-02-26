from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["termcolor>=1.1.0", "colorama"]

setup(
    name='pytrika',
    version='0.1.8',
    author="Rahul Acharya",
    author_email="mail.acharyarahul.now@gmail.com",
    description="This git-compatible module helps in organizing project specific web-url-resources. It does it by using the built-in bookmark-manager in browsers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/llk23r/pytrika",
    packages=find_packages(),
    install_requires=requirements,
    scripts=['pytrika/cthis', 'pytrika/fthis'],
    classifiers=[
         "Programming Language :: Python :: 3.6",
         "Operating System :: OS Independent",
    ],
)
