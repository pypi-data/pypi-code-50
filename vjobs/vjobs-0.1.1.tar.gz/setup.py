import setuptools


setuptools.setup(
    name='vjobs',
    version='0.1.1',
    url='https://gitlab.com/flaxking/virden-jobs',
    author='flaxking',
    author_email='flaxking@digitalnostril.com',
    description='Posts jobs scraped from websites to facebook',
    long_description='Posts jobs scraped from websites to facebook',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['pyyaml==5.1.1',
                      'beautifulsoup4==4.8.0',
                      'facebook-sdk==3.1.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
