import setuptools


setuptools.setup(
    name='django-frontapp',
    version='0.0.0',
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    description='',
    url='https://github.com/humitos/django-frontapp',
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    keywords='django front frontapp',
    project_urls={
        'Documentation': 'https://django-frontapp.readthedocs.io/',
        'Source': 'https://github.com/humitos/django-frontapp',
        'Tracker': 'https://github.com/humitos/django-frontapp/issues',
    },
)
