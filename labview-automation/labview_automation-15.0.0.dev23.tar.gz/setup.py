try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='labview_automation',
      version='15.0.0.dev23',
      description='Tools for working with LabVIEW',
      license='MIT',
      include_package_data=True,
      packages=['labview_automation', 'lv_listener'],
      download_url = 'https://gitlab.com/croningroup/chemputer/python_labview_automation/-/archive/v0.1.0/python_labview_automation-v0.1.0.tar.gz',
      install_requires=['psutil', 'pymongo', 'hoplite>=15.0.0.dev11']
      )
