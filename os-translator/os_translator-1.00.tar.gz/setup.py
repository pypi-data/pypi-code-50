from distutils.core import setup

setup(
    name='os_translator',
    packages=['os_translator'],
    version='1.00',
    license='MIT',
    description='Run this module to translate a string to a given language using Google Translate API.',
    author='Oz Shabat',
    author_email='admin@os-apps.com',
    url='https://github.com/osfunapps/os-translator-py',
    keywords=['python', 'osfunapps', 'osapps', 'Google Translate', 'api'],
    install_requires=['google'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
