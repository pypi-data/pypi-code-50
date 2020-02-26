from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='FitHome_readings',
    version='0.0.2',
    description='Get active power readings from the mongo db and put into a pandas DataFrame.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["readings"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pymongo==3.4.0", "pandas==1.0.1"],
)
