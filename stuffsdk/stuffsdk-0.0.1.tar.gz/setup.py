import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setuptools.setup(
    name="stuffsdk",
    version="0.0.1",
    author="Ashish Sahu",
    author_email="ashish@stuffsdk.com",
    description="Stuffsdk Management Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpiralDeveloper/stuffsdk",
    packages=setuptools.find_packages(),
    entry_points ={
            'console_scripts': [
                'stuffsdk = src.stuff_mining:main'
            ]
    },
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)