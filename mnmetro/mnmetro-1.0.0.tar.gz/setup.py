import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mnmetro", # Replace with your own username
    version="1.0.0",
    author="Tristan Jahnke",
    author_email="trjahnke@gmail.com",
    description="A wrapper for the Minnesota Metro API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trjahnke/mnmetro",
    packages=["mnmetro"],
    install_requires=["certifi", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires='>=3.6',
)