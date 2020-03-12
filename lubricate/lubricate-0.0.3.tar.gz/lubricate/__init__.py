# coding=utf-8
# Filename: __init__.py
from pkg_resources import get_distribution, DistributionNotFound

version = get_distribution(__name__).version
