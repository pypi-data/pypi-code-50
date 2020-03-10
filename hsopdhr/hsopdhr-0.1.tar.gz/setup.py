from setuptools import setup
setup(name='hsopdhr',
version='0.1',
description='This package generates dhr reports of HSOP in html and pdf formats',
url='https://github.com/yarlagadda1990/test',
author='yarlagadda',
author_email='yarlagadda.anusha@gmail.com',
license='',
packages=['dhrpackage'],
zip_safe=False,
entry_points={'console_scripts': ['hsopdhr = dhrpackage.__main__:main'] },)
