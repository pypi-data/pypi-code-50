import setuptools

setuptools.setup(
    name='PyADSNewVersionAlpha',
    version='0.1.7',
    description='Third version test',
    packages=['PyADSNewVersionAlpha'],
    package_dir={'PyADSNewVersionAlpha': 'PyADSNewVersionAlpha'},
    package_data={'PyADSNewVersionAlpha': ['html/*', 'html/bootstrap-4.3.1-dist/css/*', 'html/bootstrap-4.3.1-dist/js/*','html/images/*'], },
    include_package_data=True,
    install_requires=[
        'pyodbc',
        'jinja2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)
