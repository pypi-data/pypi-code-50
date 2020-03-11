from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='covid_py',
    version='0.1.5',
    description='Analysis of Corona Dataset',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Sirisha Cherala',
    author_email='sirishacherala@gmail.com',
    keywords=['Coronavirus', 'COVID']
)

install_requires = [
    'pandas', 'numpy', 'plotly'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
