import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tabular-data-synthesizer',
    version="0.2",
    author="Bauke Brenninkmeijer",
    author_email="bauke.brenninkmeijer@gmail.com",
    description="A package to evaluate how close a synthetic data set is to real data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Baukebrenninkmeijer/Tabular-data-synthesizer',
    keywords=['SYNTHETIC-DATA', 'GANs', 'SAMPLING', 'FAKE-DATA', 'TEST-DATA'],  # Keywords that define your package best
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'sdgym',
        'tqdm',
        'psutil',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
