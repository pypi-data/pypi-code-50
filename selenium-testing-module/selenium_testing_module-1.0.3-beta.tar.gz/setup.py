from distutils.core import setup
setup(
    name='selenium_testing_module',
    packages=['selenium_testing_module'],
    version='1.0.3-beta',
    license='MIT',
    description='TYPE YOUR DESCRIPTION HERE',
    author='Navaz Alani',
    author_email='nalani@uwaterloo.ca',
    url='https://github.com/navaz-alani/selenium-testing-module/',
    download_url='https://github.com/navaz-alani/selenium-testing-module/archive/v0.1-beta.tar.gz',
    keywords=[
        'testing',
        'selenium',
        'webdriver',
        'automation'
    ],
    install_requires=[
        'selenium',
        'webdrivermanager',
        'colorama'
    ],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
