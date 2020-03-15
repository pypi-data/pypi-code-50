def init_lib():
    import ctypes
    import pkg_resources
    ctypes.CDLL(pkg_resources.resource_filename(__name__, "libaio.so.1"))
