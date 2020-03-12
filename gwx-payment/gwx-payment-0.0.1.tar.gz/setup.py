import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="gwx-payment",
    version="0.0.1",
    author="Jerric Calosor",
    author_email="jerric.calosor@groworx.com.au",
    description="Payment gateway integration bridge for python, specifically flask based applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/groworxdigitalengineering/gwx-payment/src/master",
    packages=setuptools.find_packages(),
    package_data={'gwx_payment': ['config/*', ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
