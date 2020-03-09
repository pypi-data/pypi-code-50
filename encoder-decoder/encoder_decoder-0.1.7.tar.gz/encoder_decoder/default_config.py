from .dtypes_encode_decode import *
from .dtypes_extract_wrap import *
from . import DTypes

decoders = {
    DTypes.STRING: identity, # can be an identity function if decoding not required. 
                                      # This is so that all decoding functions follow the same pattern.
                                      # The same code can be reused.
    DTypes.FLOAT_NDARRAY: dict_to_float_ndarray,
    DTypes.FLOAT: string_to_float # identify function if decoding not required
}

encoders = {
    DTypes.STRING: identity, # can be an identity function if encoding not required. 
                                      # This is so that all encoding functions follow the same pattern.
                                      # The same code can be reused.
    DTypes.FLOAT_NDARRAY: float_ndarray_to_dict,
    DTypes.FLOAT: float_to_string # identify function if encoding not required
}


# extractors take Request object and return the input to the decoder
extract = {
    DTypes.STRING: extract_data,
    DTypes.FLOAT_NDARRAY: extract_data,
    DTypes.FLOAT: extract_data # identify function if encoding not required
}

# wrap output takes the encoded output and places it in the appropritate position in the response
wrap = {
    DTypes.STRING: wrap_data, # can be an identity function if encoding not required. 
                                      # This is so that all encoding functions follow the same pattern.
                                      # The same code can be reused.
    DTypes.FLOAT_NDARRAY: wrap_data,
    DTypes.FLOAT: wrap_data # identify function if encoding not required
}


'''
Procedure to add support for a new data type - 

1. Add data type in InputTypes and/or OutputTypes enum
2. Add encoding and decoding functions in dtypes_encode_decode.py
3. Add extract input and wrap output functions in dtypes_extract_wrap.py
4. Configure mapping from dtype to encode/decode function in dtypes_config.py .
4. Configure extract and wrap in dtypes_config.py .
'''