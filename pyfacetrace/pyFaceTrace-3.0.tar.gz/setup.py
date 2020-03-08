# coding:utf-8
from setuptools import setup
# or
# from distutils.core import setup  
setup(
        name='pyFaceTrace',   
        version='3.0',   
        description='easy Face Recognition fo python',   
        author='funny4875',  
        author_email='funny4875@gmail.com',  
        url='https://github.com/funny4875/pyFaceTrace.git',      
        packages=['pyFaceTrace'],
        install_requires=['numpy','scikit-image'] #opencv-python and dlib should install by user individually
)