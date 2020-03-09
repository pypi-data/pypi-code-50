#!/usr/bin/env python
# -*- coding:utf-8 _*-  
"""
@author  : Lin Luo / Bruce Liu
@time    : 2020/1/20 14:09
@contact : 15869300264@163.com
"""
import base64

from Crypto.Cipher import AES


class AESUtil(object):
    def __init__(self, encrypt_key: str, mode=AES.MODE_ECB, iv=''):
        """

        :param encrypt_key:
        :param mode:
        """
        self._key = self._data_format(encrypt_key)
        self._mode = mode
        self._iv = iv
        self._aes_client = self._get_new_cipher()

    def _get_new_cipher(self):
        """

        :return:
        """
        return AES.new(self._key, self._mode)

    @staticmethod
    def _data_format(data):
        """

        :param data:
        :return:
        """
        data = str(data)
        lack = len(data) % 16
        if lack != 0:
            data += ('\0' * (16 - lack))
        return data.encode('utf-8')

    def encrypt(self, data) -> bytes:
        """

        :param data:
        :return:
        """
        data = self._data_format(data)
        res = self._aes_client.encrypt(data)
        return base64.encodebytes(res).decode('utf-8')

    def decrypt(self, data) -> str:
        """

        :param data:
        :return:
        """
        data = base64.decodebytes(data.encode('utf-8'))
        res = self._aes_client.decrypt(data)
        tmp = res.replace(b'\x00', b'')
        return tmp.decode('utf-8')
