from setuptools import setup

setup(
    name='django-dynsettings-ritual',
    version='1.0.0',
    packages=[
        'grimoire.django.dynsettings',
        'grimoire.django.dynsettings.migrations',
    ],
    package_data={
        'grimoire.django.dynsettings': [
            'locale/*/LC_MESSAGES/*.*'
        ]
    },
    url='https://github.com/luismasuelli/django-dynsettings-ritual',
    license='LGPL',
    author='Luis y Anita',
    author_email='luismasuelli@hotmail.com',
    description='A Django application used to store dynamic settings (i.e. settings beyond the settings.py file), '
                'and retrieve them via another special object (instead of django.conf.settings, and wrapping it).',
    install_requires=['django-trackmodels-ritual>=1.0.0', 'jsonfield>=3.0.0',
                      'django-polymorphic>=2.1.2']
)