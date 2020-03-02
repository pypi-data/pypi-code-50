from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
# long_description = 'Empirical Mode Decomposition, EMD'


setup(  name='emdpy_z',
        version='0.0.3',
        description='Empirical Mode Decomposition, EMD',
        author='zhf026',
        author_email='zhf026@outlook.com',
        url='https://github.com/zhf026/emd',
        packages=['emdpy', 'emdpy.eqs', 'emdpy.insert_value'],
        install_requires=['numpy', 'scipy', 'matplotlib', 'pandas'],     
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
)