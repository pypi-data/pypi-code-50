from setuptools import setup, find_packages


setup(
    name='openstg',
    version='1.2.0',
    packages=find_packages(),
    url='https://github.com/gisce/openstg',
    license='GNU Affero General Public License v3',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    install_requires=[
        'ERPpeek==1.6.3',
        'Flask==0.12.2',
        'Flask-Cors==3.0.2',
        'Flask-Login==0.2.11',
        'Flask-RESTful==0.3.5',
        'flask-restplus==0.10.1',
        'primestg>=1.3.0',
        'marshmallow<3',
        'osconf==0.1.3',
        'pytz',
    ],
    description='API for STG-Protocol-DC Interface Specification'
)
