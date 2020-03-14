from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='aws_ecs_cluster',
    version='1.0.0',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    packages=find_packages(exclude=['venv', 'test']),
    description=(
        'AWS CDK package that correctly manages ECS Cluster.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'aws_cdk.core>=1.27.0,<1.28.0',
        'aws_cdk.aws_cloudformation>=1.27.0,<1.28.0',
        'aws_cdk.aws_ec2>=1.27.0,<1.28.0',
        'aws_cdk.aws_ecs>=1.27.0,<1.28.0',
        'aws_cdk.aws_iam>=1.27.0,<1.28.0',
        'aws_cdk.aws_lambda>=1.27.0,<1.28.0',
    ],
    author='Laimonas Sutkus',
    author_email='laimonas@idenfy.com, laimonas.sutkus@gmail.com',
    keywords='AWS CDK ECS Cluster',
    url='https://github.com/idenfy/AwsEcsCluster.git',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
)
