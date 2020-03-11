# Copyright (c) 2019 Gunakar Pvt Ltd
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted (subject to the limitations in the disclaimer
# below) provided that the following conditions are met:

#      * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.

#      * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.

#      * Neither the name of the Gunakar Pvt Ltd/Plezmo nor the names of its
#      contributors may be used to endorse or promote products derived from this
#      software without specific prior written permission.

#      * This software must only be used with Plezmo elements manufactured by
#      Gunakar Pvt Ltd.

#      * Any software provided in binary or object form under this license must not be
#      reverse engineered, decompiled, modified and/or disassembled.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
from .constants import Constants
class PlezmoMsg(object):
    def __init__(self, msg_type, msg_len, id, data):
        self.msg_type = msg_type
        self.msg_len = msg_len
        self.id = id
        self.data = data

    @staticmethod
    def from_bytes(data):
        # 1 byte header
        hdr = data[0]
        # right shift by Constants.NUM_BITS_MSG_LEN (5 bits) to get the message type
        msg_type = hdr >> Constants.NUM_BITS_MSG_LEN
        # mask out first 3 bits (mask = 0001 1111 e.g. 0x1F) to get msg length
        msg_len = hdr & Constants.MASK_MSG_LEN
        id = PlezmoMsg.bytes_to_int(data[1:3])
        return PlezmoMsg(msg_type, msg_len, id, data[3:])

    @staticmethod
    def bytes_to_int(data):
        # convert byte array in little indian order to an int
        # example number 0x0205 is stored as [0x05, 0x02] in little endian order
        # step 1 num = 0x02, step 2 num = 0x0200, step 3 num = 0x0205
        # step 1
        dlen = len(data)
        if dlen == 0:
            return 0
        n = 1
        num = data[dlen - n]
        for x in range(0, dlen - 1):
            n += 1
            num = num << 8
            num = num | data[dlen - n]
        return int(num)

    @staticmethod
    def bytes_to_signed_int(data):
        # convert byte array in little indian order to an int
        # example number 0x0205 is stored as [0x05, 0x02] in little endian order
        # step 1 num = 0x02, step 2 num = 0x0200, step 3 num = 0x0205
        # step 1
        dlen = len(data)
        if dlen == 0:
            return 0
        n = 1
        num = data[dlen - n]
        for x in range(0, dlen - 1):
            n += 1
            num = num << 8
            num = num | data[dlen - n]
        
        if num >= 32767:
            num -= 65536

        return int(num)

    @staticmethod
    def bytes_to_int32(data):
        num = (data[3] << 24) + (data[2] << 16) + (data[1] << 8) + (data[0])
        if num >= 0x7FFFFFFF:
            num -= 0x100000000
        return num

    @staticmethod
    def generate_header(msg_type, length):
        hdr = msg_type # 3 bit msg type
        hdr = hdr << Constants.NUM_BITS_MSG_LEN # left shift by 5 bits to append length
        hdr = hdr | length
        return hdr
    
    @staticmethod
    def generate_command(msg_type, cmd_data):
        hdr = PlezmoMsg.generate_header(msg_type, 1 + len(cmd_data))
        full_cmd = []
        full_cmd.append(hdr)
        full_cmd.extend(cmd_data)
        return full_cmd

    @staticmethod
    def uint_to_bytes(value, num_bytes):
        """ Extracts each byte from value and appends it to bytearray
        in little endian order
        """

        data = []
        while value != 0:
            # extract lowest byte
            b = value & 0xFF
            # append to array
            data.append(b)
            # right shift to pr0cess next byte
            value = value >> 8
        # pad zeroes if required to make size = num_bytes
        for i in range(0, num_bytes - len(data)):
            data.append(0x00)
        return data

    @staticmethod
    def uint16_to_bytes(value):
        return PlezmoMsg.uint_to_bytes(value, 2)
    
    @staticmethod
    def uint8_to_bytes(value):
        return PlezmoMsg.uint_to_bytes(value, 1)

    @staticmethod
    def str_to_bytes(value, max_length):
        if len(value) > max_length:
            value = value[0:max_length]
        # python version specific code
        if sys.version_info[0] < (3):
            value = value.encode("hex")
            data = bytearray.fromhex(value)
        else:
            data = bytearray()
            for c in value:
                data.append(ord(c))

        if len(data) < max_length:
            for x in range(0, max_length - len(data)):
                data.append(0x00)
        return data
    
    @staticmethod
    def convert_beats(beats):
        converted = int(round(beats * Constants.SPEAKER_MIDI_FACTOR))
        data = []
        data.append(converted & 0xFF)
        val = (converted % 0x100000000) >> 8
        data.append(int(val))
        return data
