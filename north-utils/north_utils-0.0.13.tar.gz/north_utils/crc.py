import codecs


def build_crc16_table():
    result = []
    for byte in range(256):
        crc = 0x0000
        for _ in range(8):
            if (byte ^ crc) & 0x0001:
                crc = (crc >> 1) ^ 0xa001
            else:
                crc >>= 1
            byte >>= 1
        result.append(crc)
    return result


crc16_table = build_crc16_table()


def build_crc(data: bytes) -> int:
    crc = 0xffff
    for a in data:
        idx = crc16_table[(crc ^ a) & 0xff]
        crc = ((crc >> 8) & 0xff) ^ idx

    return crc


def build_modbus_crc(data: bytes) -> bytes:
    crc = build_crc(data)
    return crc.to_bytes(2, 'little')


def build_c9_crc(data: bytes) -> bytes:
    crc = build_crc(data)
    return codecs.encode(crc.to_bytes(2, 'big'), 'hex_codec').upper()
