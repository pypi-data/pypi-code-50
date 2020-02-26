from setuptools import setup, find_packages

setup(
    name='mesma',
    version='1.0.0',
    description='Multiple Endmember Spectral Mixture Analysis (unmixing algorithm) and post-processing',
    author='Ann Crabbé',
    author_email='ann.crabbe@kuleuven.be',
    packages=find_packages(exclude=['*test*']),
    package_dir={
        'mesma': 'mesma',
    },
    include_package_data=True,
    zip_save=False,
    license='This program is free software; you can redistribute it and/or modify it under the terms of the GNU '
            'General Public License as published by the Free Software Foundation; either version 3 of the License, or '
            'any later version.',
    url='https://bitbucket.org/kul-reseco/mesma',
    entry_points={
        'console_scripts':
            ['mesma          = mesma.cli.mesma_cli:main',
             'mesma-shade    = mesma.cli.shade_normalisation_cli:main',
             'mesma-classify = mesma.cli.hard_classification_cli:main'
             ],
    }
)
