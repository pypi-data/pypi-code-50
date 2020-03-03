import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ingeniumpy",
    version="0.0.4",
    author="Daniel Garcia",
    author_email="dgarcia@ingeniumsl.com",
    description="Ingenium API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dani-garcia/ingeniumpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[],
    package_data={'ingeniumpy': ['bin/proxy*']},
)
