import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="supwsd",
    version="1.2.5",
    author="Simone Papandrea",
    author_email="papandrea.simone@gmail.com",
    description="Python binding to the SupWSD RESTful service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://supwsd.net",
    license='CC BY-NC-SA 3.0',
    keywords='Supervised Word Sense Disambiguation Translation',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
)