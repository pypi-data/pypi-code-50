from distutils.core import setup

setup(
    name='BIO465',  # How you named your package folder (MyLib)
    packages=['BIO465'],  # Chose the same as "name"
    version='0.35',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Class content for students at BYU who are taking BIO 465 - Capstone in Bioinformatics',
    # Give a short description about your library
    author='Samuel Payne, Thomas Molina, Teancum Paquette',  # Type in your name
    author_email='samuel.payne@byu.edu',  # Type in your E-Mail
    url='https://github.com/user/PayneLab/BIO465',  # Provide either the link to your github or to your website
    download_url='https://github.com/PayneLab/BIO465/archive/v_035.tar.gz',  # I explain this later on
    keywords=['Bioinformatics', 'BIO465', 'BYU', 'CPTAC', 'BIOLOGY'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'validators',
        'beautifulsoup4',
        'numpy',
        'pandas',
        'setuptools', 'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
