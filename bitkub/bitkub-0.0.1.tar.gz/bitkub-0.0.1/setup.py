from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='bitkub',
    version='0.0.1',
    description='Python library for bitkub.com api.',
    long_description=readme(),
    url='',
    author='sang_sakarin',
    author_email='sang_sakarin@outlook.com',
    license='sang_sakarin',
    install_requires=[],
    scripts=[],
    keywords='',
    packages=['bitkub'],
    package_dir={'bitkub': '/home/sakarin/Desktop/worksplace/bitkub/bitkub/bitkub'},
)
