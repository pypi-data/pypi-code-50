from setuptools import setup


if __name__ == '__main__':
    setup(
        name='KGlobal',
        version='1.0.12',
        author='Kevin Russell',
        packages=['KGlobal_Core', 'KGlobal_Core.data', 'KGlobal_Core.sql'],
        scripts=['KGlobal.py'],
        url='https://github.com/KLRussell/Python_KGlobal_Package',
        description='SQL Handling, Object Shelving, Data Encryption, XML Parsing/Writing, E-mail Parsing, Logging',
        install_requires=[
            'pandas',
            'future',
            'sqlalchemy',
            'pyodbc',
            'portalocker',
            'cryptography',
            'independentsoft.msg',
            'exchangelib',
            'bs4',
            'six',
        ],
        zip_safe=False
    )
