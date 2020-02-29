import setuptools

# TODO: add script "update_license.py" to show current versions (easy_requp.py, setup.py, github), ask new version,
#       check new version format, update files and git, and show new versions.

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="easy-requp",
    version="0.0.1",
    description="Easily manage Python packages based on requirements file specifications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucatrv/easy-requp",
    author="Luca Trevisani",
    author_email="lucatrv@hotmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    keywords="package manager pip requirements",
    packages=setuptools.find_packages(),
    install_requires=["pip", "setuptools"],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["easy-requp=easy_requp:main",],},
)
