import setuptools

with open("README.md", "r") as f:
  long_description = f.read()

setuptools.setup(
  name='eiprest',
  version='1.0',
  description='Python module for SOLIDserver REST API',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://gitlab.com/charlyhong/eiprest',
  author='Charles Hong',
  author_email='ch@efficientip.com',
  license='MIT',
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=['requests',],
)
