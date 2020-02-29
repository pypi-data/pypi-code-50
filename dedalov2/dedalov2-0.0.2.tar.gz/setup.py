
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dedalov2",
    python_requires='>=3.7.2',
    version="0.0.2",
    author="Jesse Donkervliet",
    author_email="j.donkervliet+dedalo@gmail.com",
    description="Explain groups of URIs on the Semantic Web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "."},
    packages=["dedalov2"],
    install_requires=[
        "hdt>=2.2.1",
        "psutil>=5.6.3",
    ],
    url="https://github.com/jdonkervliet/dedalov2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
