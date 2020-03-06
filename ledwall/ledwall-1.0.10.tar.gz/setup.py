import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ledwall",
    version="1.0.10",
    author="Klaas Nebuhr (FirstKlaas)",
    author_email="klaas@nebuhr.de",
    description="A simple but powerful library to control WS2812b LED panel.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FirstKlaas/LEDWall/tree/master/python",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyserial',
        'inputs',
        'paho-mqtt'
    ],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)