from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aiocqhttp-sanic',
    version='1.2.3a1',
    url='https://github.com/KawashiroNitori/python-aiocqhttp-sanic',
    license='MIT License',
    author='Richard Chien, KawashiroNitori',
    author_email='richardchienthebest@gmail.com',
    description='A Python SDK with async I/O for CQHTTP (Based on Sanic).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=('aiocqhttp', 'aiocqhttp.*')),
    package_data={
        '': ['*.pyi'],
    },
    install_requires=['sanic<=19.9.0', 'httpx>=0.11,<1.0'],
    extras_require={
        'all': ['ujson'],
    },
    python_requires='>=3.7',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Robot Framework',
    ],
)
