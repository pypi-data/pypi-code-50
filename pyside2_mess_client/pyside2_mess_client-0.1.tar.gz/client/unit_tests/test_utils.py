# Date: 22/09/2019 05:06
# Author: MaximRaduntsev
import unittest
import json

from common.utils import get_time, write_bytes, read_bytes, send_message, get_message
from config.settings import *


class TestMsgEncode:
    """
    Тестовый класс для тестирования отпраки и получения, при создании требует словарь,
    который будет прогонятся через тестовую функцию
    """

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_msg = {}
        self.received_msg = {}

    def send(self, test_dict):
        """
        Тестовая функция отправки, корретно кодирует сообщение,
        так-же сохраняет что должно было отправлено в сокет.
        :param test_dict:
        :return:
        """
        json_test_msg = json.dumps(self.test_dict)
        self.encoded_msg = json_test_msg.encode(BASE_ENCODING)
        self.received_msg = test_dict

    def recv(self):
        json_test_msg = json.dumps(self.test_dict)
        return json_test_msg.encode(BASE_ENCODING)


class TestUtilsFunctions(unittest.TestCase):
    """
    Тесты функций common.py
    """

    test_dict_resp = {
        ACTION: PRESENCE,
        TIME: get_time(),
        USER: {
            ACCOUNT_NAME: GUEST,
            STATUS: STATUS
        }
    }
    test_dict_response_ok = RESPONSE_OK
    test_dict_response_err = RESPONSE_BAD_REQUEST

    def test_correct_write_bytes(self):
        """
        Преобразование из словаря в байты
        """
        self.assertEqual(write_bytes({'мама': 'папа'}),
                         b'{"\\u043c\\u0430\\u043c\\u0430": "\\u043f\\u0430\\u043f\\u0430"}')

    def test_incorrect_write_bytes(self):
        """
        Исключение при неверном типе данных
        """
        self.assertRaises(TypeError), lambda: write_bytes([1, 2, 3])

    def test_correct_read_bytes(self):
        """
        Соответствие чтения из байт в словарь
        """
        self.assertEqual(read_bytes(b'{"\\u043c\\u0430\\u043c\\u0430": "\\u043f\\u0430\\u043f\\u0430"}'),
                         {'мама': 'папа'})

    def test_incorrect_read_bytes(self):
        """
        Иключение при неправильном типе данных
        """
        self.assertRaises(TypeError, lambda: read_bytes([1, 2, 3]))

    def test_send_msg(self):
        """
        Работа фукции отправки и корректность отправки словаря
        :return:
        """

        test_socket = TestMsgEncode(self.test_dict_resp)  # экземпляр тестового словаря
        send_message(test_socket, self.test_dict_resp)  # сохранение результатов в тестовом сокете

        # Проверка равенства результата кодирования и результата тестируемой функции
        self.assertEqual(test_socket.encoded_msg, test_socket.received_msg)
        # Иключение при неправильном типе данных
        self.assertRaises(TypeError, lambda: send_message(test_socket, [555, 2]))

    def test_get_msg(self):
        """
        Тест функции приёма сообщения
        :return:
        """
        test_sock_ok = TestMsgEncode(self.test_dict_response_ok)
        test_sock_err = TestMsgEncode(self.test_dict_response_err)
        # Проверка расшифровки правильного словаря
        self.assertEqual(get_message(test_sock_ok), self.test_dict_response_ok)
        # Проверка расшифровки неправильного словаря
        self.assertEqual(get_message(test_sock_err), self.test_dict_response_err)


if __name__ == '__main__':
    unittest.main()
