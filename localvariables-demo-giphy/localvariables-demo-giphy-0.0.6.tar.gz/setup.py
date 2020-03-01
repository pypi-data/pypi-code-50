import setuptools

setuptools.setup(
    name="localvariables-demo-giphy",
    version="0.0.6",
    author="Michael Barney",
    author_email="mbarneyjr5309@gmail.com",
    description="A demo for localvariables",
    long_description='long_description',
    packages=setuptools.find_packages(),
    install_requires=['giphy_client'],
    entry_points={
        "console_scripts": [
            'giphy-search=localvariables.demo:main'
        ]
    }
)
