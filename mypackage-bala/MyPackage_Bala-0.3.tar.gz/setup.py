import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='MyPackage_Bala',
     version='0.3',
     author="Bala",
     author_email="balamca08@gmail.com",
     description="A Trading utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/balaseenivasan/PythonPackage",
     packages=["MyPackage_Bala"],
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
