import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="izitest",
    version="1.0.2",
    author="Kenji 'Nhqml' Gaillac",
    license="GNU GPLv3",
    description="Easily run an executable against a test suite",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/nhqml/izitest",
    packages=setuptools.find_packages("izitest"),
    include_package_data=True,
    package_data={
        "izitest": [
            "py.typed",
        ],
    },
    platforms=[
        "Any",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyYAML>=5.2',
        'termcolor>=1.1.0',
    ],
)
