from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'


def read(filename: str):
    with open(Path(__file__).parent / filename, mode='r', encoding='utf-8') as f:
        return f.read()


setup(
    name='qmap_interpolation',
    packages=find_packages(),
    version=VERSION,
    author='Vladimir Starostin',
    author_email='vladimir.starostin@uni-tuebingen.de',
    description='Interpolation of diffraction images to reciprocal space.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    include_package_data=True,
    python_requires='>=3.6.*',
    install_requires=[
        'numpy>=1.18.1',
        'box_interpolation'
    ],
)
