from setuptools import setup, find_packages

def get_version():
    d = {}
    try:
        exec(open("k3logging/__init__.py").read(), d)
    except (ImportError, RuntimeError):
        raise RuntimeError("Unable to determine version of the k3logging project", exc_info=True)
    return d["__version__"]

def get_long_description():
    with open("README.md", "r") as fh:
        return fh.read()

setup(
    name='k3logging',
    version=get_version(),
    author="Joachim Kestner",
    author_email="joachim.kestner@khoch3.de",
    description="Standard python logging extension and utility module",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    python_requires='~=3.6',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
