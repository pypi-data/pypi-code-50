from setuptools import setup

setup(
    name='datapenosql',
    version='0.2',
    packages=['dpsql', 'dpsql.table', 'dpsql.table.model', 'dpsql.table.helpers', 'dpsql.table.service'],
    url='https://github.com/compufreq/datapenosql.git',
    license='MIT License',
    author='Alaa Alhorani',
    author_email='alaa.alhorani@outlook.com',
    description='DataPeno SQL Query Builder Utility',
    classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.6',
)
