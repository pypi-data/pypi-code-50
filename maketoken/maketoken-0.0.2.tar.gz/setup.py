import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='maketoken',
    version='0.0.2',
    author='flynn',
    author_email='fdoctor00@gmail.com',
    url='https://github.com/yunfengsay/makeToken',
    description=u'分词工具, 把文件中的词分割成token',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[
            'jieba',
            'chardet'
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ]
)
