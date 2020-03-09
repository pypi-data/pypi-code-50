from distutils.core import setup
setup(
    name = 'OverwatchAchievementExporter',
    packages = ['OverwatchAchievementExporter'],
    version = '1.0.0',
    license='apache-2.0',
    description = 'Python API to fetch a player\'s Overwatch achievements',
    author = 'Mario Lubenka',
    author_email = 'mario.lubenka@googlemail.com',
    url = 'https://github.com/saitho/galaxy_overwatch_achievement_exporter',
    download_url = 'https://github.com/saitho/galaxy_overwatch_achievement_exporter/archive/v1.0.0-1.tar.gz',
    keywords = ['Overwatch', 'achievements'],
    install_requires=[
        'requests',
        'lxml',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
)