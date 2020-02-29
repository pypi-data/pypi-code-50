from setuptools import setup
setup(
    name='finders',
    description=
    'Finders - Find resources to determine if you want to keep them',
    py_modules=['finders'],
    version='0.1.1',
    license='MIT',
    install_requires=[
        'boto3',
    ],
    download_url='https://github.com/acaire/finders/archive/0.1.1.tar.gz',
    url='https://github.com/acaire/finders',
    author='Ash Caire',
    author_email='ash.caire@gmail.com',
    keywords=[
        'finders', 'keepers', 'resource', 'discovery', 'aws', 'cloudformation',
        'stacks'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
