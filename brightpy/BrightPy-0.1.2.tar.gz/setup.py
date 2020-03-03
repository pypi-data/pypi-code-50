import pathlib
import setuptools

setuptools.setup(
    name='BrightPy',
    version='0.1.2',
    author='Cheaterman',
    author_email='the.cheaterman@gmail.com',
    description='Control the backlight through sysfs.',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/Cheaterman/BriPy',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'bripy = brightpy:main',
        'bripy-ac = brightpy:ac',
        'bripy-battery = brightpy:battery',
    ]},
)
