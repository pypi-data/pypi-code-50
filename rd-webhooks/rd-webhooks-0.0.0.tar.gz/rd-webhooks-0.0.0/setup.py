from setuptools import setup, find_packages

VERSION = "0.0.0"

setup(
    name="rd-webhooks",
    version=VERSION,
    license="MIT",
    author="Julien Lecomte",
    author_email="julien@lecomte.at",
    url="https://gitlab.com/jlecomte/projects/rd-webhooks",
    description="TODO",
    python_requires=">=3.4",
    packages=find_packages(exclude=["tests*"]),
    install_requires="",
    include_package_data=True,
)
