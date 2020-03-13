import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="ex-package-JStox",
    version="0.0.1",
    author="JStox",
    description="An example package",
    long_description=long_description,
    long_description_contrant_type='text/markdown',
    url='https://www.github.com/JStox/example_package',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy'],
    python_requires='>=3.6')
