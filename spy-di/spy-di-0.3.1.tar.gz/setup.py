import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='spy-di',
    version='0.3.1',
    author='Maksim Penkov',
    author_email='me@madmax.im',
    description='A Simple PYthon Dependency Injection Library',
    keywords='dependency-injection di',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/madmax_inc/spydi',
    packages=['spydi'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
