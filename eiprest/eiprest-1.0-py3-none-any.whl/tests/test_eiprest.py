import unittest

from eiprest import EipRest, EipRestException

class TestEipRest(unittest.TestCase):

  def test_param2str_with_none(self):
    self.assertEqual('', EipRest.param2str(None))

  def test_param2str_with_empty_dict(self):
    self.assertEqual('', EipRest.param2str({}))

  def test_param2str_with_invalid_int(self):
    with self.assertRaises(EipRestException):
      EipRest.param2str(2)

  def test_param2str_with_dict(self):
    self.assertEqual('param1=very+%28uncommon%29+%26+value%2F&param2=toto', 
                     EipRest.param2str({'param1': 'very (uncommon) & value/', 'param2': 'toto'}))

  def test_param2dict_with_none(self):
    self.assertEqual({}, EipRest.param2dict(None))

  def test_param2dict_with_bad_separator(self):
    with self.assertRaises(EipRestException):
      EipRest.param2dict("key1=val1,key2=val2")

  def test_param2dict_with_empty_key(self):
    with self.assertRaises(EipRestException):
      EipRest.param2dict("key1=val1&=val2")

  def test_param2dict_with_empty_value(self):
    with self.assertRaises(EipRestException):
      EipRest.param2dict("key1=val1&key2=")

  def test_param2dict_with_plain_text(self):
    self.assertEqual({"key1": "val1", "key2": "val2"}, EipRest.param2dict("key1=val1&key2=val2"))

  
