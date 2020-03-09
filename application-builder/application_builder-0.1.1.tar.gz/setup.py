from setuptools import setup, find_packages

with open('./README.md', 'r') as f:
    readme_text = f.read()

requirements = []

test_requirements = ['pytest']

setup(
    name = 'application_builder',
    version = '0.1.1',
    author = 'John Faucett',
    author_email = 'john.faucett@datadao.de',
    description = 'manage application data and functionality in one place',
    long_description = readme_text,
    long_description_content_type = 'text/markdown',
    packages = find_packages(),
    setup_requires = ['pytest-runner'],
    install_requires = requirements,
    tests_require = test_requirements,
    license = 'MIT',
    url = 'https://github.com/DataDaoDe/py-application_builder',
    python_requires = '>= 3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)