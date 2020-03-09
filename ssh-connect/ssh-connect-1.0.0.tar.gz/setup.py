import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name = "ssh-connect",                             # the name shown in 'pip search'. 
                                                    # note: use '-' instead of '_'
  version = "1.0.0",
  author = "li-zyang",
  author_email = "K_AEIx@163.com",
  description = "A small script to connect the existing ssh agent",
  long_description = long_description,              # from README.md, no need to modify
  long_description_content_type = "text/markdown",  # description type, no need to modify
  url = "https://github.com/li-zyang/zTools/tree/master/ssh-connect",
  packages = setuptools.find_packages(),            # grep packages automatically
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],                                                # https://pypi.org/classifiers/
  python_requires = '>=3.6',
)