import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                 name="myio", # Replace with your own username
                 version="0.0.1",
                 author="Peter Szabo",
                 author_email="info@smarthome.ninja",
                 description="This package contains myIO-server communication",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/SmarthomeNinja/home-assistant",
                 packages=setuptools.find_packages(),
                 classifiers=[
                              "Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                              ],
                 python_requires='>=3.6',
                 )
