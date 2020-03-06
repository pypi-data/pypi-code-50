import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailutils", # Replace with your own username
    version="0.0.2",
    author="Srinivas Choudhury",
    author_email="hi@srinivaschoudhury.com",
    description="This package is helpful for performing various arithmetic operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SrinivasChoudhury/mailutils",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
