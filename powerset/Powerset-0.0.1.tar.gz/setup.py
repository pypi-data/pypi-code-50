import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "Powerset", # Replace with your own username
    version= "0.0.1",
    author= "Marcos M. Recio",
    author_email= "marcosmanuelrecioperez@usal.es",
    description= "PowerSet is a set of 3 functions made in Python to work with lists as powerlists founded in mathematical powersets.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url= "https://github.com/MarcosRecio/PowerSet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
