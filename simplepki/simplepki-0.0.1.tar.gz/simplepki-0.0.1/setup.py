import setuptools

with open('README.md', 'r') as r:
    long_description = r.read()

setuptools.setup(
    name='simplepki',
    version='0.0.1',
    author='Jove Dahle',
    description='A simple CLI for making a root CA',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'simplepki=simplepki:cli',
        ],
    },
    install_requires=[
        'cryptography>=2.8',
        'click>=7.1.1',
        'questionary>=1.5.1'
    ]
)