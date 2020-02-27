import pathlib
import re
import subprocess

from setuptools import setup

ROOT = pathlib.Path(__file__).parent

# with open(ROOT / "libsplw" / "requirements.txt", "r", encoding="utf-8") as f:
#     REQUIREMENTS = f.read().splitlines()

setup(
    name="libspl",
    author="Starwort",
    url="https://github.com/Starwort/LibSPLIWACA",
    license="GNU GPL 3",
    description="Python utility library for the SPLIWACA project",
    project_urls={
        "Code": "https://github.com/Starwort/LibSPLIWACA",
        "Issue tracker": "https://github.com/Starwort/LibSPLIWACA/issues",
    },
    version="0.0.3",
    packages=["libsplw"],
    include_package_data=True,
    # install_requires=REQUIREMENTS,
    python_requires=">=3.6.0",
    keywords="LibSPLIWACA SPLIWACA splw",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)

