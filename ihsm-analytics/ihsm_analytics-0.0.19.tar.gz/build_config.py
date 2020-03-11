from setuptools import setup

readme = ''
with open('readme.md', mode='r', encoding='utf-8') as fd:
    readme = fd.read()

setup(
    name='ihsm_analytics',
    author='Huy Nguyen',
    author_email='huy.nguyen@ihsmarkit.com',
    packages=['ihsm_analytics'],
    install_requires=['numpy', 'pandas', 'scipy', 'sklearn', 'xgboost'], # TODO: add required packages
    url='https://ihsmarkit.com/',
    long_description=readme,
    include_package_data=True,
    version='0.0.19', # TODO: update version for each upload
    license='MIT',
    description='The package provides advanced geo-analytics functionalities.',
    classifiers=[
        # The full list is here: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.7'
)