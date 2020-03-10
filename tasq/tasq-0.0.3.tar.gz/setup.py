import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = "jinja2 pyyaml typer braceexpand".split()

setuptools.setup(
    name="tasq",
    version="0.0.3",
    author="Tom Breuel",
    author_email="tmbdev+remove@gmail.com",
    description="Task handlinlg.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tmbdev/tasq",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ["tasq=tasq.tasq:app"],
    },
    install_requires=install_requires,
)
