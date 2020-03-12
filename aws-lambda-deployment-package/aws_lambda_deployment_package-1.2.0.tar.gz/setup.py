from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='aws_lambda_deployment_package',
    version='1.2.0',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    packages=find_packages(exclude=['venv', 'test']),
    description=(
        'AWS package that helps you create lambda deployment packages.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
    ],
    author='Laimonas Sutkus',
    author_email='laimonas@idenfy.com, laimonas.sutkus@gmail.com',
    keywords='AWS Lambda Function Deployment Package',
    url='https://github.com/idenfy/AwsLambdaDeploymentPackage.git',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
)
