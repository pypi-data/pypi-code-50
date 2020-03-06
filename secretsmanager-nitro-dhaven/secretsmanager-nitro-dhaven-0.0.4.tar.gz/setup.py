import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secretsmanager-nitro-dhaven", # Replace with your own username
    version="0.0.4",
    author="David Haven",
    author_email="david.haven@gonitro.com",
    description="Some helper functions to make it easier to interact with AWS secretsManager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['boto3>=1.12.1',
                      'argparse>=1.4.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: System Administrators",
        "Environment :: Console"
    ],
    python_requires='>=3.6',
)
