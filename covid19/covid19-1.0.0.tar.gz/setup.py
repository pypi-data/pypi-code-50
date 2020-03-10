
import setuptools
setuptools.setup(
    name="covid19",
    version="1.0.0",
    description="A powerfull , flexible and modern python module that keeps track of Covid19 infections worldwide or by country name",
    url="https://github.com/Jakeisbored/covid19",
    author="Jake",
    author_email="jstyle07072004@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["requests","bs4"]
)
