# -*- coding: utf-8 -*-
import os
import binascii
import base64
import unittest
import codecs
import random
from fastutils.rsautils import newkeys
from fastutils.rsautils import load_private_key
from fastutils.rsautils import load_public_key_from_private_key
from fastutils.rsautils import encrypt
from fastutils.rsautils import decrypt


class TestRsaUtils(unittest.TestCase):

    def test01(self):
        pk0, sk0 = newkeys(1024)
        sk_text = sk0.save_pkcs1().decode()
        sk1 = load_private_key(sk_text)
        pk1 = load_public_key_from_private_key(sk_text)
        assert pk0 == pk1
        assert sk0 == sk1
    
    def test02(self):
        # if nbits == 1024, the max data length is 117
        # if nbits == 2048, the max data length is 245
        pk0, sk0 = newkeys(1024)
        for length in range(0, 117+1):
            print(length)
            data1 = os.urandom(length)
            text = encrypt(data1, pk0)
            data2 = decrypt(text, sk0)
            assert data1 == data2

if __name__ == "__main__":
    unittest.main()
