from distutils.core import Extension


def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    setup_kwargs.update(
        {"ext_modules": [Extension("unibuf._unibuf", ["unibuf/_unibuf.c"])]}
    )

