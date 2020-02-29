import setuptools

setuptools.setup (
    name='computype',
    version='0.0.1',
    description='A library that looks like the computer is typing and stuff, see https://codeberg.org/RevelCorp/Computype',
    author = "Revel Corp (Jason Wang specifically)",
    packages = setuptools.find_packages(),
    author_email="revel.corporation@mailfence.com",
    install_requires = ['keyboard'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.0',
    url = 'https://codeberg.org/RevelCorp/Computype',
    license = ("MIT"),
    long_description = "A library that looks like the computer is typing and stuff, see https://codeberg.org/RevelCorp/Computype",
    long_description_content_type = 'text/markdown'
)
