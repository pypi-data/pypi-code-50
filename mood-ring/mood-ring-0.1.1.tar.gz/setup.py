import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mood-ring",
    version="0.1.1",
    author="Joshah Moors",
    description="Novelty mood ring object that returns a mood as a string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshah-moors/mood-ring",
    packages=['mood_ring'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
