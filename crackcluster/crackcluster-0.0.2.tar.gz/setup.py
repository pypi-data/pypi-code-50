import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name='crackcluster',
    version='0.0.2',
    description='A joint demo on why classes are great, and how to make something pip installable',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='James Wild',
    author_email='jwild2@sheffield.ac.uk',
    url='https://github.com/wildjames/crackcluster',
    # packages=setuptools.find_packages(),
    install_requires=['numpy', 'matplotlib', 'pprint'],
    python_requires='>=3.6',
    scripts=[
          'scripts/cluster.py',
          'scripts/solar_system.py',
    ]
)