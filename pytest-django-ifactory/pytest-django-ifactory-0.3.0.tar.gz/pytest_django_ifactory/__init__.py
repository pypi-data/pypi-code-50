"""A model instance factory for pytest-django."""

import pkg_resources

try:
    distribution = pkg_resources.get_distribution("pytest-django-ifactory")
except pkg_resources.DistributionNotFound:
    pass
else:
    __version__ = distribution.version
