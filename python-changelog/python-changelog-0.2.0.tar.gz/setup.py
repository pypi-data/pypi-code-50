from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
   name='python-changelog',
   version='0.2.0',
   description='A module that generates changelogs based on git tags.',
   long_description=long_description,
   long_description_content_type="text/markdown",
   keywords='changelog conventional commit git',
   author='Lennart Suwe',
   author_email='lennsa999@gmx.de',
   packages=['changelog'],
   install_requires=[
     "Click<7.1",
     "GitPython<3.2",
     "requests<2.23",
   ],
   entry_points={"console_scripts": ["pychangelog = changelog.changelog_generator:generator"]}
)
