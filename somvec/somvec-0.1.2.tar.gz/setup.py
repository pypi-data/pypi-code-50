from setuptools import setup

#with open("README.md", "r") as fh:
#    long_description = fh.read()

long_description = """

This is a vectorised python implementation of the Self-Organising Map (SOM) algorithm. It was created for use in the author's master dissertation and has now been released for anyone who might want to benefit from it. Please inform me of any additional functionality that might be desired.

## Features: ##

* Fits and plots features, Best Matching Unit (BMU) counts and training curves for SOM
* Quantisation or topological error based stopping criteria
* Hypercube or random uniform weight initialisation
* Periodic Boundary Conditions (PBC) allowing the SOM to wrap like a torous
* Semi-Supervised training mode whereby the labels for a supervised learning problem are used to update the weights of the SOM but not to find the BMU
* Clusters SOM nodes using K-Means clustering and plots cluster maps
* Models, clusters and images are automatically saved (this is configurable)
* Quantisation and topological errors are automatically logged to a csv file for each run of the model (with parameter values saved for reproducibility)
* Has been used to fit data for a masters dissertation on a dataset with an excess of 1 million records

BitBucket repo: https://bitbucket.org/GeoffreyClark/somvec

"""

setup(name='somvec',
      version='0.1.2',
      description='A vectorised implementation of the Self-Organising Map (SOM) algorithm',
      long_description=long_description,
      url='https://bitbucket.org/GeoffreyClark/somvec',
      author='Geoffrey Clark',
      author_email='geoffreyrussellclark@gmail.com',
      license='MIT',
      packages=['somvec'],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      )
