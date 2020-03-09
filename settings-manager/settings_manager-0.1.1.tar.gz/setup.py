from setuptools import find_packages, setup

def read_file(filename: str):
    with open(filename, 'r') as fp:
        data = fp.read()
    return data

requirements = [
    'PyYAML>=5.3',
]

test_requirements = ['pytest']

setup(
    name = 'settings_manager',
    version = '0.1.1',
    author = 'John Faucett',
    author_email = 'jwaterfaucett@gmail.com',
    description = 'A settings manager for python applications',
    long_description = read_file('./README.md'),
    long_description_content_type = "text/markdown",
    url = 'https://github.com/DataDaoDe/py-settings-manager',
    license = 'MIT',
    packages = find_packages(),
    setup_requires = ['pytest-runner'],
    install_requires = requirements,
    tests_require = test_requirements,
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = '>= 3.6',
    zip_safe = False
)