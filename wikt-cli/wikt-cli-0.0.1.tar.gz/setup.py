from setuptools import setup, find_packages

setup(
    name='wikt-cli',
    version='0.0.1',
    description='An English Wiktionary frontend for CLI.',
    # long_description=open('./README.md').read(),
    # long_description_content_type='text/markdown',
    keywords='wiktionary dictionary cli',
    license='MIT',
    # url='https://github.com/fakefred/ascim',
    author='fakefred',
    author_email='fakefred@protonmail.ch',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wikt=wikt.__main__:main'
        ]
    },
    python_requires='>=3.5',
    install_requires=['wiktionaryparser'],
    project_urls={
        'LiberaPay': 'https://liberapay.com/fakefred/donate'
    }
)
