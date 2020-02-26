"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='adafruit-circuitpython-featherwing',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='CircuitPython library that provides FeatherWing specific classes for those that '
                'require a significant amount of initialization.',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing',

    # Author details
    author='Adafruit Industries',
    author_email='circuitpython@adafruit.com',

    install_requires=['Adafruit-Blinka', 'adafruit-circuitpython-busdevice',
                      'adafruit-circuitpython-register', 'adafruit-circuitpython-ina219',
                      'adafruit-circuitpython-seesaw', 'adafruit-circuitpython-ht16k33',
                      'adafruit-circuitpython-dotstar', 'adafruit-circuitpython-neopixel',
                      'adafruit-circuitpython-ds3231', 'adafruit-circuitpython-gps',
                      'adafruit-circuitpython-adxl34x', 'adafruit-circuitpython-adt7410'],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='adafruit ina219 featherwing joy joywing i2c '
             'hardware micropython circuitpython',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['adafruit_featherwing'],
)
