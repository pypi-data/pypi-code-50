import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='aiohttp-openapi',
     version='0.1.2',
     author="Matija Bogdanovic",
     author_email="matija.bogdanovic@gmail.com",
     description="OpenAPI documentation builder for aiohttp server.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.5',
     include_package_data=True,
     install_requires=['aiohttp'],
 )
