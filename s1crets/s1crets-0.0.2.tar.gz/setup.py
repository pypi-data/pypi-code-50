import io
import re
import setuptools

with io.open("README.md", "rt", encoding="utf8") as f:
    long_description = f.read()

with io.open("s1crets/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

setuptools.setup(
    name="s1crets",
    version=version,
    author="NAGY, Attila",
    author_email="nagy.attila@gmail.com",
    description="Convenience wrapper for AWS Parameter Store/Secrets Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bra-fsn/s1crets",
    packages=setuptools.find_packages(),
    scripts=['bin/s1crets'],
    install_requires=['cachetools', 'click>=7.0', 'boto3>=1.9.61'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
