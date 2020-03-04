import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RachitRobotarium", # Replace with your own username
    version="0.0.1",
    author="Rachit Bhargava",
    author_email="rachitbhargava99@gmail.com",
    description="Enhanced package for Georgia Tech's Robotarium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)