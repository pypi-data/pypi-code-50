# from setuptools import setup, find_packages
# setup(
#     name="ONAL",
#     version="0.1",
#     packages=find_packages(),
# )



from setuptools import setup
from os import path


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

DIR = path.dirname(path.abspath(__file__))
# INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()




setup(
    name='ONAL',
    packages=['ONAL','ONAL/classes','ONAL/functions','ONAL/tests','ONAL/utils','ONAL/functions/community','ONAL/functions/components','ONAL/functions/graph_embedding','ONAL/functions/not_sorted','ONAL/functions/structural_holes','ONAL/functions/graph_embedding/node2vec'],
    description="ONAL testing",
    long_description=README,
    long_description_content_type='text/markdown',
    # install_requires=INSTALL_PACKAGES,
    version='0.0.1',
    license="MIT",
    url='https://github.com/willingnesshxl/OpenGraph',
    author='A, B, C, D',
    author_email='ONAL@163.com',
    keywords=['ONAL'],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-sugar'
    ],
    package_data={
        # include json and pkl files
        '': ['*.json', 'models/*.pkl', 'models/*.json'],
    },
    include_package_data=True,
    python_requires='>=3',
    install_requires = ['gensim==3.8.1', #'numpy==1.18.1'
    ],
)
