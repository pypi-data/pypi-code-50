from setuptools import setup, find_packages
from spectral_libraries.package_variables import *
# read the contents of your README file
with open(path.join(path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    read_me = f.read()
    read_me_intro = ' '.join(read_me.splitlines()[3:5])

setup(
    name=package_name_pip,
    version=long_version,

    description=read_me_intro,
    description_content_type='text/x-rst',
    long_description=read_me,
    long_description_content_type='text/x-rst',
    keywords=keywords,

    author=author,
    author_email=author_email,

    url=bitbucket_home,
    project_urls={
        'Documentation': read_the_docs,
        'Source Code': bitbucket_src,
        'Issue Tracker': bitbucket_issues,
    },

    packages=find_packages(exclude=['*test*']),
    data_files=[("", ["LICENSE.txt"])],
    include_package_data=True,
    zip_save=False,

    entry_points={
        'console_scripts':
            ['emc      = spectral_libraries.cli.ear_masa_cob_cli:main',
             'ies      = spectral_libraries.cli.ies_cli:main'],
    },

    classifier='License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
)
