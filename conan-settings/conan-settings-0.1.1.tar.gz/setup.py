from setuptools import setup, find_packages


setup(
    name='conan-settings',
    version='0.1.1',
    author='Eero Rikalainen',
    author_email='eerorika@gmail.com',
    url='https://github.com/eerorika/conan-settings',
    description='Modify Conan settings.yml configuration',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'HiYaPyCo',
        'conan',
    ],
    entry_points={
        'console_scripts': [
            'conan-settings = conan_settings.cli:main'
        ]
    },
)
