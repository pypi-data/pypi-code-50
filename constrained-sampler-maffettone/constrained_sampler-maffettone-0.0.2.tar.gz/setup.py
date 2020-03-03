import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="constrained_sampler-maffettone",
    version="0.0.2",
    description="Package to generate numbers in the unit hypercube subject to constraints.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maffettone/constrained_sampler",
    packages=setuptools.find_packages(),
    install_requires=[
        'markdown',
        'numpy'
    ],
    test_suite="test",
    scripts=['bin/sampler'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6'
)
