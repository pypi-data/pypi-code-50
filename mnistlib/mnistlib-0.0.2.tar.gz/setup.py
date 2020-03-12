from setuptools import setup

setup(
    name = 'mnistlib',
    version = '0.0.2',
    description = 'geometric transformations for mnist dataset',
    license = 'MIT',
    packages = ['mnistlib'],
    author = 'Oleg Zyablov',
    author_email = 'oleg.z98@mail.ru',
    keywords = ['mnist'],
    url='https://github.com/sedol1339/SkillFactory/tree/master/Module%201/mnistlib%20python%20module/dist/mnistlib-0.0.2.tar.gz',
    install_requires = [
        'mnist', 'matplotlib', 'PIL'
    ],
    include_package_data = True
)