"""setup.py: setuptools control"""

from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.read().split('\n')

setup(
    name="cmdline-lpp-solver",
    packages=["lpp_solver"],
    entry_points={
        "console_scripts": ['lpp_solver = lpp_solver.simplex:main']
    },
    version="0.0.2",
    license='MIT',
    description="Python command line application with solves linear programming problems.",
    long_description=long_descr,
    author="Maxym Fuhol, Evgenii Babin",
    author_email="maxym.fugol@gmail.com, prototy791@gmail.com",
    url="https://github.com/Mtrqq/LPPSolver/blob/master/lpp_solver/__init__.py",
    download_url="https://github.com/Mtrqq/LPPSolver/archive/0.0.2.tar.gz",
    keywords = ['LINEAR PROGRAMMING', 'CMD', 'UTILITY'],
    install_requires=requirements,
      classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ]
    )
