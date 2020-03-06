# Date: 22/09/2019 05:05
# Author: MaximRaduntsev
import time
import unittest
from common.utils import get_time
from jim.errors import MaxLongUsernameError
from jim.core import Message as Obj
from config.settings import *

from log.client_log_config import logger

# sys.path.append(os.path.join(os.getcwd(), '..'))
date_format = '%Y-%m-%d %H:%M:%S'
presence_message = Obj.presence
param_time = time.strftime(date_format)


class TestPresenceMessage(unittest.TestCase):
    def test_response_presence_msg(self):
        """
        Проверка возврата правлиьного ответа,
        при передаче корректных данных в функцию
        presence_message()
        """
        self.assertEqual(presence_message(logger, GUEST, None).to_dict, {
            ACTION: PRESENCE,
            TIME: param_time,
            USER: {
                ACCOUNT_NAME: GUEST
            }
        })

    def test_default_name(self):
        """
        Проверка возврата имени пользователя,
        в presence_message() без аргументов
        """
        self.assertNotEqual(presence_message(logger, None, None).to_dict, {
            ACTION: PRESENCE,
            TIME: param_time,
            USER: {
                ACCOUNT_NAME: GUEST
            }
        })

    def test_response_raises_presence(self):
        """
        Иключение при неправильном типе данных,
        в аргументе presence_message()
        """
        self.assertRaises(TypeError), lambda: presence_message(['NOT A STRING'],
                                                               123,
                                                               {'NOT A STRING'}).to_dict

    def test_raises_user_long(self):
        """
        Иключение при слишком длинном имени пользователе,
        переданном в качестве аргумента функции
        presence_message()
        """
        long_username = 'MAX_NAME_LEN-MAX_USERNAME_LEN'
        # presence_message(logger, long_username, None).to_dict

        with self.assertRaises(MaxLongUsernameError):
            presence_message(logger, long_username, None).to_dict

    def test_is_action(self):
        """
        Проверка ключа ACTION в результате работы presence_message()
        """
        self.assertTrue(presence_message(logger, GUEST, None).to_dict[ACTION])

    def test_action_is_presence(self):
        """
        Проверка PRESENCE в ключе ACTION в результате работы presence_message()
        """
        self.assertEqual(presence_message(logger, GUEST, None).to_dict[ACTION], PRESENCE)

    def test_is_time(self):
        """
        Проверка ключа TIME в результате работы presence_message()
        """
        self.assertTrue(presence_message(logger, GUEST, None).to_dict[TIME])

    def test_action_in_time(self):
        """
        Проверка времени в ключе ACTION в результате работы presence_message()
        """
        self.assertEqual(presence_message(logger, GUEST, None).to_dict[TIME], param_time)

    def test_user_in_presence(self):
        """
        Проверка ключа USER в результате работы функции presence_message()
        """
        self.assertTrue(presence_message(logger, GUEST, None).to_dict[USER])

    def test_account_name_in_user(self):
        """
        Проверка ключа ACCOUNT_NAME в словаре ключа USER в результате работы presence_message()
        """
        self.assertTrue(presence_message(logger, GUEST, None).to_dict[USER][ACCOUNT_NAME])

    def test_user_in_account_name(self):
        """
        Проверка дефолтного имени пользователя в ключе ACCOUNT_NAME в результате работы presence_message()
        """
        self.assertEqual(presence_message(logger, GUEST, None).to_dict[USER][ACCOUNT_NAME], GUEST)

    def test_user(self):
        """
        Проверка дефолтного имени пользователя в ключе ACCOUNT_NAME в результате работы presence_message()
        """
        # user = Obj.user

        # print(message_obj.user)
        # print(message[USER])

        # message_class = presence_message(logger, GUEST, None)
        # print(message_class.user)
        # self.assertEqual(presence_message(logger, GUEST, None).to_dict[USER][ACCOUNT_NAME], GUEST)

        # Если это сообщение о присутствии, принимаем и отвечаем
        message = {
            ACTION: PRESENCE,
            TIME: param_time,
            USER: {
                ACCOUNT_NAME: GUEST
            }
        }
        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == PRESENCE and \
                TIME in message_obj.to_dict and USER in message_obj.to_dict:
            print('PRESENCE,', message_obj.user)

        # Если это сообщение, то добавляем его в очередь сообщений. Ответ не требуется.
        message = {
            ACTION: MESSAGE,
            TIME: param_time,
            DESTINATION: DESTINATION,
            SENDER: ACCOUNT_NAME,
            MESSAGE_TEXT: message,
        }
        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == MESSAGE and \
                DESTINATION in message_obj.to_dict and TIME in message_obj.to_dict and \
                SENDER in message_obj.to_dict and MESSAGE_TEXT in message_obj.to_dict and \
                message_obj.destination == DESTINATION:
            print('MESSAGE,', 'signal', message_obj.destination)

        # Если это запрос известных пользователей
        message = {
            ACTION: USERS_REQUEST,
            TIME: param_time,
            ACCOUNT_NAME: GUEST
        }
        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == USERS_REQUEST and \
                ACCOUNT_NAME in message_obj.to_dict and message_obj.user == GUEST:
            print('ACTIVE,', message_obj.user)

        # Если это запрос контакт-листа
        message = {
            ACTION: GET_CONTACTS,
            TIME: param_time,
            USER: GUEST
        }
        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == GET_CONTACTS and \
                USER in message_obj.to_dict and message_obj.user == GUEST:
            print('GET_CONTACTS,', message_obj.user)

        # Если это добавление-удаление контакта
        message = {
            ACTION: ADD_CONTACT,
            TIME: param_time,
            USER: GUEST,  # тот, кто в данный момент добавляет новый контакт
            ACCOUNT_NAME: USER,  # тот, кого добавили
        }
        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == ADD_CONTACT and \
                ACCOUNT_NAME in message_obj.to_dict and USER in message_obj.to_dict and \
                message_obj.user == GUEST:
            print('ADD_CONTACT - DEL_CONTACT,', message_obj.user, ' create/delete ', USER)

        # Если клиент выходит
        message = {
            ACTION: QUIT,
            TIME: param_time,
            ACCOUNT_NAME: GUEST
        }
        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == QUIT and \
                ACCOUNT_NAME in message_obj.to_dict and message_obj.user == GUEST:
            print('QUIT,', message_obj.user)

        suc = Obj.accepted(ACCEPTED)
        er = Obj.error_resp(ERROR)
        f = Obj.forbidden(BAD_REQUEST)

        print(suc.to_dict, type(suc.to_dict))
        print(er.to_dict, type(er.to_dict))
        print(f.to_dict, type(f.to_dict))

    def test_user2(self):
        # Если это сообщение, то добавляем его в очередь сообщений. Ответ не требуется.
        message = {
            ACTION: MESSAGE,
            TIME: param_time,
            DESTINATION: DESTINATION,
            SENDER: ACCOUNT_NAME,
            MESSAGE_TEXT: 'message',
        }

        message_obj = Obj(message)

        if ACTION in message_obj.to_dict and message_obj.action == MESSAGE and \
                DESTINATION in message_obj.to_dict and TIME in message_obj.to_dict and \
                SENDER in message_obj.to_dict and MESSAGE_TEXT in message_obj.to_dict and \
                message_obj.destination == DESTINATION:
            print('MESSAGE,', 'signal,', message_obj.destination)

        # suc = Obj.accepted(ACCEPTED)
        # er = Obj.error_resp(ERROR)
        # f = Obj.forbidden(FORBIDDEN)
        #
        # print(suc.to_dict, type(suc.to_dict))
        # print(er.to_dict, type(er.to_dict))
        # print(f.to_dict, type(f.to_dict))


if __name__ == '__main__':
    unittest.main()
