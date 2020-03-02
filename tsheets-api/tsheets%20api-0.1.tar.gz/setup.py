import setuptools

with open("README.md", "r") as file_handler:
    long_description = file_handler.read()

setuptools.setup(
    name = 'tsheets api',
    version = '0.1',
    author = 'Marek Schir',
    license = 'MIT',
    author_email = 'schir2@gmail.com',
    description = 'TSheets API Client',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/schir2/tsheets-api',
    packages=setuptools.find_packages(),
    keywords = 'tsheets api gps',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)