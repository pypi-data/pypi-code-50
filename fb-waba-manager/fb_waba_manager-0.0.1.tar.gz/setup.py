from setuptools import setup


setup(
    name='fb_waba_manager',
    packages=['fb_waba_manager'],
    package_dir={'fb_waba_manager': 'src/fb_waba_manager'},
    version='v0.0.1',
    license='MIT',
    description='Helper to handle with facebook\'s waba',
    author='Gabriel Rodrigues dos Santos',
    author_email='gabrielr@take.net',
    url='https://github.com/chr0m1ng/fb-waba-manager',
    download_url='https://github.com/chr0m1ng/fb-waba-manager/archive/v0.0.1.tar.gz',
    keywords=['facebook', 'graph api', 'waba'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
