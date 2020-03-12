from setuptools import setup, find_packages
import io

setup(
    name='classify-ifchange',
    version='0.0.1',
    description='nlu service tools for classification',
    long_description="xxx",
    long_description_content_type="text/markdown",
    url='https://www.ifchange.com',
    author='ai3',
    author_email='ai3@ifchange.com',
    license='Apache License 2.0',
    install_requires=['nlutools', 'scipy', 'sklearn', 'numpy'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
