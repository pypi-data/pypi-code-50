from enum import Enum, auto

class DTypes(Enum):
    STRING = auto() # python string
    FLOAT_NDARRAY = auto() # numpy ndarray
    FLOAT = auto() # python float or numpy float