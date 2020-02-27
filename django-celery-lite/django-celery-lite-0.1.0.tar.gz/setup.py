from setuptools import setup, find_packages

version = '0.1.0'

packages = find_packages()

setup(
    name='django-celery-lite',
    version=version,
    description='A Django celery lite integration for the Django framework.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shinz Natkid',
    author_email='shinznatkid@gmail.com',
    url='https://github.com/shinznatkid/django-celery-lite',
    packages=find_packages(),
    install_requires=[
    ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
