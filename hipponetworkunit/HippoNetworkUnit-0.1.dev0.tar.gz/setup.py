try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name="HippoNetworkUnit",
        version="0.1.dev",
        author="Pedro Garcia-Rodriguez",
        author_email="pedro.garcia@unic.cnrs-gif.fr",
        packages=["HippoNetworkUnit",
                  # capabilities 
                  "HippoNetworkUnit.capabilities",
                  # tests
                  "HippoNetworkUnit.tests",
                  # scores
                  "HippoNetworkUnit.scores"
                  ],
        url="https://github.com/pedroernesto/HippoNetworkUnit",
        license="BSD Clause-3",
        # description="",
        # long_description="",
        install_requires=["sciunit>=0.1.3.1"]
)

