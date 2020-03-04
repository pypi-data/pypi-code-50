from setuptools import setup, find_packages

requires = [
    'boto>=2.49.0,<3.0.0',
    'requests>=2.22.0,<3.0.0',
    'retrying>=1.3.3,<2.0.0',
    'pillow>=6.2.1'
]

setup(
   name='scrybe',
   version='0.2.13',
   description='Automated Experiment Tracking to improve transparency, organisation and collaboration in DS/ML projects',
   author='scrybe.ml',
   author_email='admin@scrybe.ml',
   packages=find_packages(),
   install_requires=requires,
   classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
