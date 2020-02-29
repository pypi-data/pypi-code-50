from setuptools import setup

REQUIREMENTS = []

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(name = "matrixHandler",
      version = "0.2.0",
      description = "a small module which adds a Matrix class to be used as a new data type",
      long_description=open("README.md").read(),
      long_description_content_type='text/markdown',
      url = "https://github.com/EliotMcNab/pyMatrix.git",
      author = "Eliot McNab",
      author_email = "",
      license = "MIT",
      packages = [],
      classifiers = CLASSIFIERS,
      requires = REQUIREMENTS,
      python_requires = ">=3",
      keywords = "Matrix, Matrixes, Mathemacis, Maths, Algebra",
)