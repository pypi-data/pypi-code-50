import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="StellarLog",
  version="0.0.7",
  author="Powerfulbean",
  author_email="powerfulbean@gmail.com",
  description="A Lib for Easy Logging",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/powerfulbean/StellarLog",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)