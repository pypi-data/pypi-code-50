from setuptools import setup

setup(
    name = 'mnistlib',
    version = '0.0.11',
    description = 'geometric transformations for mnist dataset',
    license = 'MIT',
    packages = ['mnistlib'],
    author = 'Oleg Zyablov',
    author_email = 'oleg.z98@mail.ru',
    keywords = ['mnist'],
    install_requires = [
        'mnist', 'matplotlib', 'Pillow', 'numpy'
    ],
    include_package_data = True
)