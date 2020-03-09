
from setuptools import setup

setup(
    name='BiImageTransform',
    version='0.1.0-alpha1',
    license='MIT',

    packages=[ 'BiImageTransform', ],

    install_requires=[
        'torch',
        'torchvision',
        'scikit-image',
        'Pillow',
        'numpy',
    ],

    author='aoirint',
    author_email='aoirint@gmail.com',

    url='https://github.com/aoirint/BiImageTransform',

    description='PyTorch Transform for color image and grayscale mask',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
