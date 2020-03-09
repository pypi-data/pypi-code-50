"""Setup file"""
import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="general-conversors",
  version="1.0.3",
  author="Golden M",
  author_email="support@goldenmcorp.com",
  description="Library for convert N-level dictionaries to one-level dictionaries",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/goldenm-software/general-conversors",
  packages=setuptools.find_packages(),
  python_requires='>=3.6',
)
