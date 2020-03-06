from setuptools import setup


with open('crossref_citedby_driver/README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='hirmeos-crossref-citedby-driver',
    version='0.0.1',
    author='Rowan Hatherley',
    author_email='rowan.hatherley@ubiquitypress.com',
    description='Functions required by the crossref-citedby-driver',
    install_requires=[
        'beautifulsoup4==4.8.0',
        'lxml==4.4.1',
        'requests==2.22.0',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hirmeos/crossref-citedby-driver',
    packages=['crossref_citedby_driver'],
    classifiers=[],
)
