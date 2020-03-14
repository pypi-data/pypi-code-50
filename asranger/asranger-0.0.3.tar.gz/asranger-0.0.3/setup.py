from setuptools import setup

setup(
    name='asranger',
    version='0.0.3',
    description='Ranger - a synergistic optimizer using RAdam '
                '(Rectified Adam) and LookAhead in one codebase ',
    license='Apache',
    install_requires=['torch'],
    url="https://github.com/mpariente/Ranger-Deep-Learning-Optimizer",
    long_description='',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)