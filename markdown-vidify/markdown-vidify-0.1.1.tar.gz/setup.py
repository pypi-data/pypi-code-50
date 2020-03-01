import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    author = "Jason Hamilton-Smith",
    autor_email = "hs.jason@gmail.com",
    classifiers = [
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup",
    ],
    description = "Video tag generator markdown extension",
    entry_points = {
            "markdown.extensions": ["vidify = vidify:VidifyExtension"]
    },
    install_requires = requirements,
    keywords = "makrdown video html5 html5video",
    license = "GPLv3",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    maintainer = "Jason Hamilton-Smith",
    maintainer_email = "hs.jason@gmail.com",
    name = "markdown-vidify",
    packages = setuptools.find_packages(),
    python_requires = ">=2.7.15, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    url = "https://github.com/zchfvy/vidify",
    version = "0.1.1",
)
