from setuptools import setup, find_packages


setup(
    name="livesplit-id-normalizer",
    version="0.1.0",
    description=(
        "Livesplit split file ids can get out of whack upon manual edit, normalize to start from 1"
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="livesplit-id-normalizer",
    author="Jon Robison",
    author_email="narfman0@gmail.com",
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    test_suite="tests",
    entry_points={
        "console_scripts": ["livesplit-normalize=livesplit_id_normalizer.cli:start"]
    },
)
