from ..geometry.rectangle import Rectangle

import random


def int_to_bitmask(i: int) -> str:
    """
    Converts and int value to and bitmask string
    """
    result = 0
    for _ in range(i):
        result >>= 1
        result |= 0b10000000
    return result


def convert_byte(image, x, y, high_color=(0, 0, 0), mask=0xFF):
    if y >= image.height:
        return 0
    if x >= image.width:
        return 0

    result = 0
    for b in range(x, x + 8):
        result = result << 1
        if b < image.width:
            color = image.getpixel((b, y))
            if color == high_color:
                result |= 1

    return result & mask


def convert_image_to_progmem_bitmask(
    name, image, x, y, width=None, height=None, high_color=(0, 0, 0)
):
    if width is None:
        width = image.width
    if height is None:
        height = image.height
    number_of_blank_bits = width % 8
    print(number_of_blank_bits)
    result = "const uint8_t {}[] PROGMEM = {} 0x{:02x}, 0x{:02x},\n    ".format(
        name, "{", width, height
    )
    bit_pos = range(x, x + width, 8)

    for row in range(height):
        bytes = [convert_byte(image, x, row, high_color) for x in bit_pos]

        if number_of_blank_bits > 0:
            last_byte = bytes[-1:]
            last_byte[0] &= int_to_bitmask(number_of_blank_bits)
            bytes[-1:] = last_byte

        bytes = ["B{:08b}".format(b) for b in bytes]
        result += ", ".join(bytes)
        result += "\n    "

    result += "};"
    return result
