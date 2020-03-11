from setuptools import setup, find_packages


def main():
    setup(
        name='tas',
        use_scm_version=True,
        description='',
        version='0.0.6',
        url='https://github.com/zveryansky/tas',
        author='Aleksandr Zverianskii',
        author_email='',
        license='MIT',
        classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        ],
        keywords='',
        packages=find_packages(exclude=['templates']),
        install_requires=['requests'],
    )

if __name__ == '__main__':
    main()
