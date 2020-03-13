from setuptools import setup

setup(name='rsvpmeetup',
      version='0.1',
      description='A Module to Autoamatically rsvp yes to events in configured events',
      url='https://github.com/vishwesh-D-kumar/MeetupRSVP',
      author='Vishwesh Kumar',
      author_email='vishwesh18119@iiitd.ac.in',
      license='MIT',
      packages=['rsvpmeetup'],
      install_requires=[
          'requests',
      ],
      scripts=['rsvpcron'],
      include_package_data=True,
      zip_safe=False)