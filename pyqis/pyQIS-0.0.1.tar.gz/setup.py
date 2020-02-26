from setuptools import setup

setup(
    name="pyQIS",
    version="0.0.1",
    author="Sefa Eyeoglu",
    author_email="contact@scrumplex.net",
    description="QIS client for German university information servers.",
    license="GPL3",
    keywords="pyQIS client library university grade results",
    url="https://gitlab.com/Scrumplex/pyqis",
    packages=["pyQIS"],
    install_requires=["requests", "beautifulsoup4", "lxml"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
