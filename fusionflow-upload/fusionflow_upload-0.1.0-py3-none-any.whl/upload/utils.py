def get_name(type_):
    try:
        return type_.__name__
    except AttributeError:
        return type(type_).__name__
