#python3 setup.py sdist upload
#twine upload dist/libretronic-1.0.8.tar.gz

from distutils.core import setup
setup(
name = 'libretronic',
version = '1.0.9',
packages=['libretronic'],
author = 'M. en I. Margarito Navarrete-Mendoza',
author_email = 'ni_tronic@hotmail.com',
url = 'https://github.com/Nitronic666/firts.git',
description = 'Libreria de Trabajo',
)