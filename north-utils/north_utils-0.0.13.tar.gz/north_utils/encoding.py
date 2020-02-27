import codecs
import string

BASE_DIGITS = string.digits + string.ascii_uppercase


def int_to_bytes(*values: int, length: int=2) -> bytes:
    data = bytes()
    for value in values:
        data += round(value).to_bytes(length, byteorder='big', signed=True)
    return data


def int_from_bytes(value: bytes, ) -> int:
    return int.from_bytes(value, byteorder='big', signed=True)


def int_to_hex(value: int) -> str:
    return '0x' + codecs.encode(int_to_bytes(value, length=4), 'hex_codec').decode()


def convert_base(x: int, digits: str=BASE_DIGITS) -> str:
    if x < 0:
        sign = -1
    elif x == 0:
        return digits[0]
    else:
        sign = 1

    base = len(digits)
    x *= sign
    digit_list = []

    while x:
        digit_list.append(digits[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digit_list.append('-')

    digit_list.reverse()

    return ''.join(digit_list)