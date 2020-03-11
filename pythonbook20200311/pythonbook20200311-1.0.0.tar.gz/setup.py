from setuptools import setup, find_packages

setup(
        name='pythonbook20200311',
        version='1.0.0',
        packages=find_packages(),

        author='test test',
        author_email='test@example.com',
        url='https://github.com/test/test',
        description='This is a test package',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',

        python_requires='~=3.6',

        classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Operating System :: OS Independent',
        ],

        install_requires=[
          'Click~=7.0',
        ],

        extras_require={
          's3': ['boto3~=1.10.0'],
          'gcs': ['google-cloud-storage~=1.23.0'],
        },
        package_data={'pythonbook20200311': ['data/*']},


)
