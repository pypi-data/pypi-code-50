from setuptools import setup, find_packages

def readme():
    with open("README.rst", encoding="utf-8") as f:
        return f.read()

# python3 setup.py sdist bdist_wheel
# twine upload dist/* --skip-existing

setup(
    name="create-flask-application",
    version="0.1.9",
    description="This is an application designed to speed up process of configuring evironment for new flask RESTful projects.",
    long_description=readme(),
    classifiers=[        
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Utilities'
    ],
    keywords='flask create generate',
    author='igoras1993',
    author_email='igor.kantorski@gmail.com',
    license='GPLv3',
    packages=['create_flask_application'],
    package_data={'create_flask_application': ['templates/*', 'templates/sphinx/*', 'templates/alembic/*', 
        'templates/flask/*', 'templates/flask/app/*', 'templates/flask/app/config/*', 'templates/flask/app/events/*', 'templates/flask/app/rest/*', 'templates/flask/app/templates/*']},
    install_requires=['jinja2'],
    entry_points={
        'console_scripts': [
            'create-flask-application=create_flask_application.cmdl:create'
        ]
    },
    include_package_data=True
)