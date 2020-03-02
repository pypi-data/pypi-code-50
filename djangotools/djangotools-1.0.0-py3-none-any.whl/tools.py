# This function extract first key of given kwargs.
def get_first_kwarg(kwargs):
    first_key = None
    for key, value in kwargs.items():
        first_key = key
        if key is not None:
            break
    return first_key
