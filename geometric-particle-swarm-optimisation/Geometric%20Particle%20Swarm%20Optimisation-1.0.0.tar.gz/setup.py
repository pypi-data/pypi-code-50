from setuptools import setup

def readme():
    with open('README.md') as f :
        README=f.read()
    return README

setup(
    name="Geometric Particle Swarm Optimisation",
    version="1.0.0",
    description="A python package to find the best features in a dataset using Geometric Particle Swarm Optimisation",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/LegenderDePavilo/GPSO",
    author="Lakshajyoti Paul",
    author_email="klakshajyotipaul@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pso"],
    include_package_data=True,
    install_requires=["numpy","pandas","gc","math"]
    )
