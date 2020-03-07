from setuptools import setup, find_packages

setup(
    name="open_detection",
    version="0.2",
    url="https://github.com/killf/open_detection",
    author="killf",
    author_email="killf@foxmail.com",
    license="Apache2.0",
    description="A simple and powerful toolkit for object detection and instance segmentation.",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires='>=3.7',
    long_description="A simple and powerful toolkit for object detection and instance segmentation.",
    classifiers=[],
    keywords=[]
)
