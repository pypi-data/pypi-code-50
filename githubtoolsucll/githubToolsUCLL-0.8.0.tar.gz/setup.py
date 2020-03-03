from distutils.core import setup
setup(
    name='githubToolsUCLL',
    packages=['githubToolsUCLL'],
    version= '0.8.0',
    license='MIT',
    description='A collection of tools to make UCLL assignments easier for both teachers and students.',
    author='De Vogeltjes',
    author_email='joery.mertens@student.ucll.be',
    url='https://github.com/dieterDehaes/github-tools',
    entry_points = {
        'console_scripts': [ 
                                'createToken=githubToolsUCLL.createToken:main',
                                'pullIssues=githubToolsUCLL.pullIssues:main',
                                'pushIssues=githubToolsUCLL.pushIssues:main',
                                'cloneRepos=githubToolsUCLL.cloneRepos:main',
                                'createIssue=githubToolsUCLL.createIssue:main',
                                'issuesToFile=githubToolsUCLL.pullToFile:main',
                                'fileToIssues=githubToolsUCLL.createFromFile:main',
                                'githubToolsUcll=githubToolsUCLL.help:main',
                            ]
    },
    install_requires = [
        'pyyaml',
        'gitpython',
        'xlwt',
        'xlrd',
        'requests'
    ],
    zip_safe=False
)