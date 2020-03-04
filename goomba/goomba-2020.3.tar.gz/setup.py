import re, datetime
from setuptools import setup, find_packages

# Version
version = None
with open("./goomba/__init__.py", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip().strip('"')
assert version is not None, "Check version in soothsayer/__init__.py"

setup(name='goomba',
      version=version,
      description='Architecture for building creating pipelines',
      url='https://github.com/jolespin/goomba',
      author='Josh L. Espinoza',
      author_email='jespinoz@jcvi.org',
      license='BSD-3',
      packages=find_packages(include=("*", "./*")),
      install_requires=[
      "scandir",
      "pathlib2",
      "tqdm >=4.19",
      "tzlocal",
      ],
)
