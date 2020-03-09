import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easylogcli",
    version="1.2.2",
    description="[easylog](https://github.com/prprprus/easylog) 的 Python 客户端实现",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prprprus/easylog-client",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
