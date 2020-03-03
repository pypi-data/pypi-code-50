import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edison-ml",
    version="0.1.0",
    author="jiangplus",
    author_email="jiang.plus.times@gmail.com",
    description="simple machine learning pipeline toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiangplus/edison",
    packages=setuptools.find_packages(),
    scripts = ["edi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # install_requires=[
    #     'boto3',
    # ],
)
