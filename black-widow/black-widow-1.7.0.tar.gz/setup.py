#!/usr/bin/env python3

import os

from setuptools import setup


def find_packages(path, base="", exclude=()):
    """ Find all packages in path """
    packages = []
    for item in os.listdir(path):
        if item[0] == '.':
            continue
        if path in exclude:
            continue
        directory = os.path.join(path, item)
        if os.path.isdir(directory):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            if module_name in exclude:
                continue
            packages.append(module_name)
            packages.extend(find_packages(directory, module_name, exclude))
    return packages


with open("./src/black_widow/README.md", "r") as fh:
    long_description = fh.read()


with open("./src/black_widow/requirements.txt", "r") as fh:
    install_requires = fh.readlines()


setup(
    name="black-widow",
    version='1.7.0',
    author="Fabrizio Fubelli",
    author_email="fabri.fubels@gmail.com",
    description="Offensive penetration testing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/offensive-hub/black-widow",
    packages=find_packages(
        'src',
        exclude=(
            'black_widow.docker',
            'black_widow.docs',
            'black_widow.lessons',
            'black_widow.resources.logos',
            'black_widow.resources.social'
        )
    ),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    package_data={
        '': [
            '*.html',
            '*.css',
            '*.js',
            '*.eot', '*.svg', '*.ttf', '*.woff', '*.woff2',
            '*.png', '*.jpg', '*.ico',
            'LICENSE',
            'requirements.txt',
            'black-widow-ascii.txt'
            # 'web.wsgi'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Natural Language :: English",
        "Topic :: Education :: Testing",
        'Topic :: Software Development :: Build Tools',
        "Topic :: System :: Clustering",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Hardware :: Symmetric Multi-processing",
        "Topic :: Utilities"
    ],
    entry_points={
        'console_scripts': [
            'black-widow = black_widow:main',
        ]
    },
    python_requires='>=3.6',
    keywords='black-widow penetration testing offensive cyber security pentest sniffing',
    project_urls={
        'Documentation': 'https://docs.black-widow.io',
        'Source': 'https://github.com/offensive-hub/black-widow',
        'Tracker': 'https://github.com/offensive-hub/black-widow/issues',
    },
    install_requires=install_requires
)
