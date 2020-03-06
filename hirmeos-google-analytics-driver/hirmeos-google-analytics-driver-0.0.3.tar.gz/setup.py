from setuptools import setup


with open('google_analytics_driver/README.rst', 'r') as f:
    long_description = f.read()

requirements = [
    'hirmeos-clients>=0.0.6',
    'google-api-core>=1.14.3',
    'google-api-python-client>=1.7.11',
    'google-auth>=1.6.3',
]


setup(
    name='hirmeos-google-analytics-driver',
    version='0.0.3',
    author='Rowan Hatherley',
    author_email='rowan.hatherley@ubiquitypress.com',
    description='Functions required by google_analytics_driver',
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hirmeos/google_analytics_driver',
    packages=['google_analytics_driver'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7'
)
