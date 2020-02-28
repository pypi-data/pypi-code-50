from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="iot-manager-client",
    version="0.0.1",
    packages=["iot_manager_client"],
    author="Dylan Crockett",
    author_email="dylanrcrockett@gmail.com",
    license="MIT",
    description="A client used for connecting to a IoT Manager Server instance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dylancrockett/iot-manager-client",
    project_urls={
        "Documentation": "https://iotmanager-client.readthedocs.io/",
        "Source Code": "https://github.com/dylancrockett/iot-manager-client"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8'
)
