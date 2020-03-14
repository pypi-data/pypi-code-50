from setuptools import setup

with open('README.md',encoding = 'utf-8')as fl:
    long_description = fl.read()

setup(
    name='getwebtitle',
    version='0.0.4',
    description='A function to get a website title',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Zhang',
    author_email='secret@xxx.com',
    url='https://github.com/suifengpiaoyang/packagingLearning',
    download_url='https://github.com/suifengpiaoyang/packagingLearning/archive/master.zip',
    py_modules=['getwebtitle'],
    license='GPL',
    install_requires=['requests', 'lxml'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ]
)
