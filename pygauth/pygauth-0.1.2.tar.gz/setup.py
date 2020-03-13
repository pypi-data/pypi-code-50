import setuptools

with open("requirements.txt", "r") as f:
    install_requires = [o for o in [i.split("#")[0] for i in f.readlines()] if len(o) > 0]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygauth",
    version="0.1.2",
    install_requires=install_requires,
    author="Spazzlo",
    description="A Python helper library for Google Authentication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spazzlo/pygauth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
