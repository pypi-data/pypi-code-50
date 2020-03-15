import setuptools

setuptools.setup(
    name='trellogy',
    version='2.0.3',
    author="Chianti Scarlett",
    author_email="chianti.scarlett@gmail.com",
    description="Trello board managing tool via Trello REST API",
    url="https://github.com/chiantiscarlett/trellogy",
    packages=["trellogy"] or setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
