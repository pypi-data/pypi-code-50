from setuptools import setup

setup(
    name = 'mnistlib',
    version = '0.0.1',
    description = 'geometric transformations for mnist dataset',
    license = 'MIT',
    packages = ['mnistlib'],
    author = 'Oleg Zyablov',
    author_email = 'oleg.z98@mail.ru',
    keywords = ['mnist'],
    url='https://github.com/sedol1339/SkillFactory/tree/master/module%201/mnistlib%20python%20module',
    install_requires = [
        'mnist'
    ],
    include_package_data = True
)