from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

packages = find_packages(exclude=['tests*'])

setup(
    name='pvlv',
    version='0.0.1',
    license='LGPLv3',

    author='AbbestiaDC',
    author_email='not.simone.scuola@outlook.com',
    description='Bot Framework for Pavlov',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/The-Pavlov-Project/pvlv',

    packages=packages,
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],

    python_requires='>=3.6',
    install_requires=[
        'pvlv-database',
        'pvlv-commando',
        'pvlv-img_builder',
        'SpeechRecognition==3.8.1',
        'pydub==0.23.1',
    ],
)
