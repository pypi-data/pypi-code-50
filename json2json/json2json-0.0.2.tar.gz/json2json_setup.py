import setuptools

setuptools.setup(
    name='json2json',
    version='0.0.2',
    author='rdgoite',
    author_email='rodrey@ebi.ac.uk',
    description='A tool for converting JSON documents to another JSON document format.',
    url='https://github.com/ebi-ait/ingest-archiver/tree/master/conversion',
    packages=setuptools.find_packages(include='conversion'),
    python_requires='>=3.6'
)