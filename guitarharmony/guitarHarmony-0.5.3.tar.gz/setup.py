import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
# import pypandoc
# long_description = pypandoc.convert_file('README.md', 'rst')

setuptools.setup(
    name="guitarHarmony",
    version="0.5.3",
    author="Esparami",
    author_email="heeryerate@gmail.com",
    description="A python wrapper to learn music theory in Guitar.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/heeryerate/Guitar-Harmony",
    # download_url = 'https://bitbucket.org/Xi_He/music-theory/get/0.5.1.zip',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords = ['music', 'theory', 'guitar', 'harmony'],
    python_requires='>=3.6',
)
