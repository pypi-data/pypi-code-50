import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="O_NLP_Preprocessor-Emeka_Onyebuchi", # Replace with your own username
    version="0.0.2",
    author="Emeka Onyebuchi",
    author_email="chybyke.emeka@gmail.com",
    description="A python package that has various libraries for processing NLP text. While just specifying the pandas column, it automatically removes stopwords, tokenizes it, stems it and lemmatizes it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emeka-darthvader/O-NLP-Preprocessor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)