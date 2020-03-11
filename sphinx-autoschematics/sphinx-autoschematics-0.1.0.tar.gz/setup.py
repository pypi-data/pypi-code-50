from setuptools import setup

with open("README.md", "r") as readme_fd:
    long_description = readme_fd.read()

setup(
    name="sphinx-autoschematics",
    version="0.1.0",
    description="sphinx-autoschematics provides sphinx extenions for documenting schematics models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Evan Borgstrom",
    author_email="evan@borgstrom.ca",
    url="https://github.com/NerdWalletOSS/sphinx-autoschematics",
    license="Apache License Version 2.0",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    install_requires=["six"],
    packages=["autoschematics"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ],
)
