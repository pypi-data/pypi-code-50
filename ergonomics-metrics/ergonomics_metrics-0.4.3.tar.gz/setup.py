import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

long_description = long_description.replace("./Resources/pose.gif", "https://raw.githubusercontent.com/rs9000/ergonomics/master/Resources/pose.gif")

setuptools.setup(
     name='ergonomics_metrics',
     version='0.4.3',
     author="Rosario Di Carlo",
     author_email="rs.dicarlo@gmail.com",
     description="Ergonomics metrics",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/rs9000/ergonomics",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )