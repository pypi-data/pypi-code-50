import os

from codecs import open

from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(here, "src", "mythos", "msg", "__version__.py")

ABOUT = {}
with open(version_path, "r", "utf-8") as f:
    exec(f.read(), ABOUT)

INSTALL_REQUIRES = []

EXTRAS_REQUIRE = {
    "tests": ["flake8", "mypy", "pytest", "pytest-cov", "pytest-mock"]
}
EXTRAS_REQUIRE["dev"] = (
    ["twine>=3.1.1,<4.0.0"] + EXTRAS_REQUIRE["tests"]
)


setup(
    name=ABOUT["__title__"],
    version=ABOUT["__version__"],
    description=ABOUT["__description__"],
    long_description=ABOUT["__description__"],
    author=ABOUT["__author__"],
    license=ABOUT["__license__"],
    url=ABOUT["__url__"],
    packages=find_packages(where="src"),
    namespace_packages=["mythos"],
    package_data={"": ["LICENSE", "README.md"]},
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    tests_require=EXTRAS_REQUIRE["tests"],
    cmdclass={},
    entry_points={
        "console_scripts": [
            # "cli-command=pypackage.cli:cli"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development"
    ],
    zip_safe=False
)
