import unittest
from unittest.mock import patch
from techcombine.utils import LINENotify
from techcombine.utils import make_message_from_dict

class LineNotifyTastCase(unittest.TestCase):
    def setUp(self):
        self.data = {
                "email": 'test@mail.com',
                "first_name": 'test',
                "phone_number": '0123456789',
                "created_at": '2020-02-27 14:49:35.693253+00:00',
            }

    def test_make_message_from_dict(self):
        message = make_message_from_dict(self.data)
        message_rest = "email : kittipat.phongsak@gmail.com\nfirst_name : kittipat\nphone_number : 0952237753\ncreated_at : 2020-02-27 14:49:35.693253+00:00"
        self.assertEqual(message, message_rest)

