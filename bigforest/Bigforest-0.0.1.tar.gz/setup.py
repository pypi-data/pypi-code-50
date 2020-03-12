import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bigforest",
    version="0.0.1",
    author="kenspy",
    author_email="381717500@qq.com",
    description="Distributed node router",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kensdm/forest/tree/master",
    packages=setuptools.find_packages(),
    install_requires=[
        "pickleshare",
        "pymysql"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)