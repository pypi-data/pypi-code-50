import pkg_resources


__version__ = pkg_resources.resource_string("pygnn", "VERSION.txt").decode("UTF-8").strip()


__all__ = ["__version__"]
