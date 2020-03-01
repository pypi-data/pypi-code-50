
def add(a, b):
    """[summary]

    Arguments:
        a {[type]} -- [description]
        b {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return a + b


def divide(a, b):
    """[summary]

    Arguments:
        a {[type]} -- [description]
        b {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if b == 0:
        raise ValueError('b cant be zero')
    return a/b
