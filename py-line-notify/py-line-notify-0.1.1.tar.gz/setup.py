import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py-line-notify',
    version='0.1.1',
    author="Kittinan Srithaworn",
    description="Simple package for Line Notify",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=['requests'],
    keywords='Line Notify',
    url="https://github.com/kittinan/py-line-notify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],

    project_urls={
        'Bug Reports': 'https://github.com/kittinan/py-line-notify/issues',
        'Source': 'https://github.com/kittinan/py-line-notify',
    },
)
