from distutils.core import setup
import setuptools

setup(
    name='openapi3-fuzzer',
    packages=setuptools.find_packages(),
    version='0.1',
    license='gpl-3.0',
    description='Openapi3 fuzzer',
    author='VolkerWessels Telecom',
    author_email='opensource@vwt.digital',
    url='https://github.com/vwt-digital/openapi3-fuzzer/tree/master',
    keywords=['Openapi3', 'fuzzer', 'vwt'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
