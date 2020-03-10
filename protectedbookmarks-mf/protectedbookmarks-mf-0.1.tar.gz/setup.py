from setuptools import setup
 
setup(
    name='protectedbookmarks-mf',
    packages=['protectedbookmarks-mf'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='GNU', # La licencia que tenga tu paqeute
    description='A utility to save your bookmarks in your own pc, with password and encryptation.',
    author='Matias Fanger',
    author_email='matiasfanger@outlook.com',
    url='https://github.com/RDCH106/mypackage', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/RDCH106/parallel_foreach_submodule/archive/v0.1.tar.gz', # Te lo explico a continuación
    keywords='bookmarks', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paqeute
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)