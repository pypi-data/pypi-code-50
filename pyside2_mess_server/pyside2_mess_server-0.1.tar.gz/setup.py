from setuptools import setup, find_packages

setup(
    name="pyside2_mess_server",
    version="0.1",
    description="PySide2 messenger - Server package",
    author="MaximR",
    author_email="support@geekbrains.ru",
    packages=find_packages(),
    install_requires=['dynaconf', 'sqlalchemy', 'pycryptodome', 'pyside2']
)
