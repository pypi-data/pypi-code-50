from setuptools import setup, find_packages

setup(
    name='Hotel_Lite',
    version='0.6',
    author='a13franciscoca',
    author_email='francasal.34@gmail.com',
    description='Gestor sencillo de un hotel o casa rural',
    long_description=open('README.rst').read(),
    license=open('LICENSE.txt').read(),
    url='https://github.com/MrNadix/HOTEL_Lite',
    packages=["Hotel_Lite"],
    package_data={'Hotel_Lite': ["*.*"]},
    classifiers=[

        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License']
)
