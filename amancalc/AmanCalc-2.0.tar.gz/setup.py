import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="AmanCalc",
 
    #version of the module
    version="2.0",
 
    #Name of Author
    author="Aman Mishra",
 
    #your Email address
    author_email="mishra.aman180@gmail.com",
 
    #Small Description about module
    description="Use For Calculation Of Two Numbers.",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="",
    packages=["AmanCalc"],

    #package data
    include_package_data=True,

    #Dependencies
    install_requires=[""],
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
