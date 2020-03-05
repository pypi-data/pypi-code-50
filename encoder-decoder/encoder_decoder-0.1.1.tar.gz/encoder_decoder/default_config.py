from dtypes import InputTypes, OutputTypes
from dtypes_encode_decode import *
from dtypes_extract_wrap import *

decoders = {
    InputTypes.STRING: identity, # can be an identity function if decoding not required. 
                                      # This is so that all decoding functions follow the same pattern.
                                      # The same code can be reused.
    InputTypes.FLOAT_NDARRAY: dict_to_float_ndarray,
    InputTypes.FLOAT: string_to_float # identify function if decoding not required
}

encoders = {
    OutputTypes.STRING: identity, # can be an identity function if encoding not required. 
                                      # This is so that all encoding functions follow the same pattern.
                                      # The same code can be reused.
    OutputTypes.FLOAT_NDARRAY: float_ndarray_to_dict,
    OutputTypes.FLOAT: float_to_string # identify function if encoding not required
}


# extractors take Request object and return the input to the decoder
extract_input = {
    InputTypes.STRING: extract_data,
    InputTypes.FLOAT_NDARRAY: extract_data,
    InputTypes.FLOAT: extract_data # identify function if encoding not required
}

# wrap output takes the encoded output and places it in the appropritate position in the response
wrap_output = {
    OutputTypes.STRING: wrap_data, # can be an identity function if encoding not required. 
                                      # This is so that all encoding functions follow the same pattern.
                                      # The same code can be reused.
    OutputTypes.FLOAT_NDARRAY: wrap_data,
    OutputTypes.FLOAT: wrap_data # identify function if encoding not required
}


'''
Procedure to add support for a new data type - 

1. Add data type in InputTypes and/or OutputTypes enum
2. Add encoding and decoding functions in dtypes_encode_decode.py
3. Add extract input and wrap output functions in dtypes_extract_wrap.py
4. Configure mapping from dtype to encode/decode function in dtypes_config.py .
4. Configure extract_input and wrap_output in dtypes_config.py .
'''