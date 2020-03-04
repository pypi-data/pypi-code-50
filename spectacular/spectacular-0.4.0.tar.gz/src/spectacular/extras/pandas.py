from spectacular.schemas import primitive
from spectacular.extras.base import type_checker, TYPE_CHECKERS


try:
    import pandas
except ImportError:
    pass
else:

    def data_frame(description=None):
        return primitive("data_frame", description)

    @type_checker(TYPE_CHECKERS, "data_frame")
    def _is_data_frame(_checker, value):
        return isinstance(value, pandas.DataFrame)
