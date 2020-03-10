from distutils.core import setup
setup(
    name='fitanalytics',         # How you named your package folder (MyLib)
    packages=['fitanalytics'],   # Chose the same as "name"
    version='1.2',      # Start with a small number and increase it with every change you make
    license='MIT',
    description='FitAnalytics AI Library',   # Give a short description about your library
    author='Vinícius R. Ferraz',                   # Type in your name
    author_email='viniciusrfrz@gmail.com',      # Type in your E-Mail
    url='https://github.com/FitAnalytics/fitanalytics',   # Provide either the link to your github or to your website
    download_url='https://github.com/FitAnalytics/fitanalytics/archive/v_01.2.tar.gz',  # I explain this later on
    keywords=['fitanalytics', 'classification', 'multiclass'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'numpy',
        'pandas',
        'nltk',
        'gensim',
        'keras',
        'tensorflow=2.1.0',
        'scikit-learn',
        'pickle-mixin',
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
