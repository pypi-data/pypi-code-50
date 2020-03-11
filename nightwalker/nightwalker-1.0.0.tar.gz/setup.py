from setuptools import setup, find_packages
from io import open

setup(
    name='nightwalker',
    version='1.0.0',
    description='Neural Network Supervision Platform',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/systemcorp-ai/NightWalker',
    packages= find_packages(),
    author='SYSTEM CORP.',
    author_email='contact@systemcorp.ai',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        "Operating System :: OS Independent"
    ],
    install_requires=[
          'requests',
      ],
)


