from setuptools import setup, find_packages

setup(name='chombopy',
      version='0.1.2',
      description='Running, analysing and plotting Chombo simulations',
      url='https://github.com/jrgparkinson/mushy-layer',
      author='Jamie Parkinson',
      author_email='jamie.parkinson@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      setup_requires = ['wheel'],
      python_requires='>=3.6',
      install_requires=['matplotlib>=3.0.0',
                        'Shapely>=1.6.0',
                        'geopandas>=0.6.2',
                        'scipy>=1.2.0',
                        'scikit-image>=0.16.2'],
      zip_safe=False)
