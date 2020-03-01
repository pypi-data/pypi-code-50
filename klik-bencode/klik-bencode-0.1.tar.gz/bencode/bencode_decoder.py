def decode_int(value):
    """Decoding the Bencode value to native int value"""
    end_position = value.find("e")
    if len(value[1:end_position]) > 1:
        if value[1] == "-":
            if value[2] == "0":
                raise ValueError("Negative Zero is not allowed!")
        if value[1] == "0":
            raise ValueError("Leading Zero is not allowed")
    decoded_integer = int(value[1:end_position])
    bencode_data = value[end_position:]
    if len(bencode_data) == 1:
        bencode_data = ""
    return decoded_integer, bencode_data


def decode_string(value):
    """Decoding Bencode value to native string value"""
    delimiter_position = value.find(":")
    length_of_decoded_string = int(value[:delimiter_position])
    string_start_position = delimiter_position + 1
    decoded_string = value[
        string_start_position : string_start_position + length_of_decoded_string
    ]
    bencode_data = value[delimiter_position + length_of_decoded_string + 1 :]
    return decoded_string, bencode_data


def decode_list(value):
    """Decoding Bencode value to native list value"""
    bencode_data = value[1:]
    decoded_list = []
    while len(bencode_data) > 1:
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        decoded_list.append(decoded_value)
        if bencode_data == "ee":
            bencode_data = ""
    bencode_data = ""
    return decoded_list, bencode_data


def decode_dictionary(value):
    """Decoding Bencode value to native dictionary value"""
    bencode_data = value[1:]
    decoded_dict = {}
    while bencode_data:
        decoded_key, bencode_data = bencode_decoder(bencode_data=bencode_data)
        if not decoded_key.isalpha():
            raise TypeError(f"Keys can only be string. But {decoded_key} is not")
        decoded_value, bencode_data = bencode_decoder(bencode_data=bencode_data)
        decoded_dict[decoded_key] = decoded_value
        if bencode_data == "ee":
            bencode_data = ""
    bencode_data = ""

    return decoded_dict, bencode_data


def bencode_decoder(bencode_data):
    """Decoding Bencode string to native python data types"""
    if bencode_data[0] == "i":
        decoded_value, bencode_data = decode_int(value=bencode_data)
    elif bencode_data[0].isdigit():
        decoded_value, bencode_data = decode_string(value=bencode_data)
    elif bencode_data[0] == "l":
        decoded_value, bencode_data = decode_list(value=bencode_data)
    elif bencode_data[0] == "d":
        decoded_value, bencode_data = decode_dictionary(value=bencode_data)
    else:
        raise TypeError("Not a proper Bencode String")
    return decoded_value, bencode_data


def decoder(bencode_data):
    """Returns the python native data type decoded from Bencode String"""
    decoded_value, _ = bencode_decoder(bencode_data)
    return decoded_value
