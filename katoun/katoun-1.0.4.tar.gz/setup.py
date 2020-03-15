from setuptools import setup

setup(
    name='katoun',
    author='Tiffany Souterre',
    version='1.0.4',
    packages=['katoun'],
    description="An application to display my beybey katoun in ASCII <3",
    entry_points={
        'console_scripts': ['katoun=katoun.main:main']
    }
)
