import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpg-0bs1d1an",
    version="0.0.10",
    author="Guido Kroon (@0bs1d1an)",
    author_email="gkroon@maelstrom.ninja",
    description="Risk plot generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/0bs1d1an/rpg",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Topic :: Security',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.6',
    install_requires=[
        'matplotlib',
    ],
    package_data={
        'rpg': [
            'data/*.png',
        ],
    },
    entry_points={
        'console_scripts': [
            'rpg=rpg.__main__:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://gitlab.com/0bs1d1an/rpg/issues',
        'Source': 'https://gitlab.com/0bs1d1an/rpg/',
    },
)
