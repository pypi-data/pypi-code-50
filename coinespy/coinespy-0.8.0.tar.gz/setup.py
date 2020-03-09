import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coinespy",
    version="0.8.0",
    author="Bosch_Sensortec GmbH",
    author_email="rolf.kaack@bosch-sensortec.com",
    description="Python wrapper for coinesAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.bosch-sensortec.com/",
    packages=['coinespy'],
    package_data={'coinespy': ['libcoines_64.dll',
                               'libcoines_32.dll',
                               'libcoines_64.so',
                               'libcoines_32.so',
                               'libcoines.dylib',
                               'libcoines_armv7_32.so']
                  },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires='>=2.6, <4',
)
