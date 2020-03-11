import setuptools
def get_readme():
    with open("README.md", "r") as fh:
        readme = fh.read()
    return readme
def get_version():
    with open("VERSION", "r") as fh:
        version= fh.read()
    minor_version = int(version[-2:])
    new_version   = version[:-2] + str(minor_version + 1)
    with open("VERSION", "w") as fh:
        fh.write(new_version)
    return version

setuptools.setup(
     name='jr_data_science',  
     version=get_version(),
     author="romain jouin",
     author_email="romain.jouin@gmail.com",
     description="Data Science help functions",
     long_description=get_readme(),
     long_description_content_type="text/markdown",
     url="https://github.com/romainjouin/data-science",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
