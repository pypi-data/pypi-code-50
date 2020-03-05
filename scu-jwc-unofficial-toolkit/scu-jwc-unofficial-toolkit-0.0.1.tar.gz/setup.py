import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="scu-jwc-unofficial-toolkit",
    version="0.0.1",
    author="KXXH",
    author_email="zjm97@outlook.com",
    description="An unofficial toolkit for scu jwc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KXXH/SCU_JWC_toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "icalendar"
    ]
)
