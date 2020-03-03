from setuptools import find_packages, setup

setup(
    name='BrightPy',
    version='0.1.1',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'bripy = brightpy:main',
        'bripy-ac = brightpy:ac',
        'bripy-battery = brightpy:battery',
    ]},
    author='Cheaterman',
    author_email='the.cheaterman@gmail.com',
    description='Control the backlight through sysfs',
    license='MIT',
)
