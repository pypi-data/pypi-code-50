import setuptools

with open('readme.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="nimbusinator",
    version="0.2.2",
    author="Tim Adams",
    author_email="adamstimb@gmail.com",
    description="RM Nimbus GUI for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamstimb/nimbusinator",
    packages=setuptools.find_packages(),
    package_data={'nimbusinator': ['data/*']},
    install_requires=[
        "PySDL2",
        "Pillow",
        "numpy",
        "simpleaudio",
        "pynput==1.4.5",
        "psutil",
        "pygame>=1.9.3,<2.0;python_version!='3.3'",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)