from setuptools import setup

setup(
    name='zappa_scheduler',
    version='1.0.3',
    packages=['zappa_scheduler'],
    url='https://github.com/wisaac407/zappa-call-later',
    license='MIT License',
    author='andytwoods, Isaac Weaver',
    author_email='andytwoods@gmail.com, wisaac407@gmail.com',
    description='store future tasks in the db and call them after set delays',
    install_requires=['django-picklefield']
)
