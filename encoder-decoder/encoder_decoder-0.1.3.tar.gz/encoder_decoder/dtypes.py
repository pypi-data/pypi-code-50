from enum import Enum, auto

class InputTypes(Enum):
    STRING = auto() # python string
    FLOAT_NDARRAY = auto() # numpy ndarray
    FLOAT = auto() # python float or numpy float

class OutputTypes(Enum):
    STRING = auto() # python string
    FLOAT_NDARRAY = auto() # numpy ndarray
    FLOAT = auto() # python float or numpy float