from setuptools import setup, find_packages

setup(
    name="open_detection",
    version="0.2.2",
    author="killf",
    author_email="killf@foxmail.com",
    maintainer="killf",
    maintainer_email="killf@foxmail.com",
    contact="killf",
    contact_email="killf@foxmail.com",
    url="https://github.com/killf/open_detection",
    license="Apache2.0",
    description="A simple and powerful toolkit for object detection and instance segmentation.",
    long_description="A simple and powerful toolkit for object detection and instance segmentation.",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires='>=3.7',
    classifiers=[],
    keywords=["object detection", "instance segmentation", "deep learning"]
)
