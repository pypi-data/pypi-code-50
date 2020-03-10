"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject

author: "Ilham Bintang"
email: "ilham@keyreply.com"

"""

from setuptools import setup, find_packages
import covid_nlp

setup(
    name='Covid-NLP',
    version=str(covid_nlp.__VERSION__),
    packages=find_packages(),
    description='Covid-19 Chatbot engine to decode question and reply with context',
    long_description=str(
        'Covid-19 Chatbot engine to decode question and reply with context'),
    url='https://github.com/nullphantom/covid-19-chatbot-engine',
    author='Ilham Bintang',
    author_email="ilham@keyreply.com",
    license="Apache License, Version 2.0",

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[],
    package_data={'': ['data.csv']},
    include_package_data=True,
)