import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vampireanalysis",
    version="3.4.1",
    author="Kyu Sang Han",
    author_email="khan21@jhu.edu",
    description="Vampire Image Analysis Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://wirtzlab.johnshopkins.edu",
    packages=setuptools.find_packages(include=['vampireanalysis', 'vampireanalysis.*']),
    install_requires=[
        'scipy==1.3.3',
        'pandas==0.25.3', 
        'numpy==1.17.4', 
        'pillow==6.2.1',
        'matplotlib==3.1.2', 
        'scikit-learn==0.22', 
        'scikit-image==0.16.2',
        'opencv-python==4.1.2.30',
        'dask==2.9.0'
    ],
    # scripts=['bin/vampire.py'],
    entry_points={
        'console_scripts': ['vampire=vampireanalysis.vampire:vampire']
        },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        'Operating System :: Microsoft :: Windows',
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires='>=3'

)