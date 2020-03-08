from distutils.core import setup

setup(
    name='MLChallenge',
    version='0.1.0',
    author='Tushar Mehta',
    author_email='mehta.tushar@outlook.com',
    packages=['mlchallenge', 'mlchallenge.test'],
    scripts=['bin/model.py','bin/model1..ipynb'],
    url='http://pypi.python.org/pypi/MLChallenge/',
    license='LICENSE.txt',
    description='Plexure ML Challenge.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pandas",
        "numpy",
		"matplotlib"
		"seaborn"
		"scipy"
		"pandas_profiling"
		"sklearn"
    ],
)