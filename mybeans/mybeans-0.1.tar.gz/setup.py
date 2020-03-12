from setuptools import setup
setup(
    name='mybeans',
    packages=['beans'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='LGPL v3', # La licencia que tenga tu paqeute
    description='A example',
    author='agomez66',
    author_email='agomez66@xtec.cat',
    url='https://github.com/agomez66/examplebeans', # Usa la URL del repositorio de GitHub
    keywords='It is a example develop', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paqeute
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)
