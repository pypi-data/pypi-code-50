from setuptools import setup

setup(
    name="bambooclatx",
    version='0.0.1',
    package_dir={'': 'src'},
    packages=[
        'bambooclatx',
        'bambooclatx.commands',
        'bambooclatx.providers'
    ],
    author='John Doe',
    author_email='john@doe.com',
    install_requires=[],
    include_package_data=True,
)
