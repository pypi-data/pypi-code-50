from unittest import TestCase, mock
from aws.secret import get_secret_value, create_secret, delete_secret, update_secret
import time, json

class TestSecret(TestCase):
  def test_secret_string(self):
    try:
      res_plain = create_secret(f"test-secret-plain", "test string secret from unit testing secrets manager", string = "shh")
      self.assertIsNotNone(res_plain)
      self.assertIsNotNone(res_plain.get('ARN'))
      self.assertEqual(res_plain.get('Name'), f'test-secret-plain')
      self.assertEqual(res_plain.get('SecretString'), 'shh')
    except Exception as e:
      self.fail(f'Failed to create plaintext secret, see exception:\n{e}')
    finally:
      delete_secret('test-secret-plain', perma_delete = True)
      delete_secret('test-secret-binary', perma_delete = True)
      delete_secret('test-secret-1583522541-DEFAULT', perma_delete = True)
      delete_secret('test-secret-1583522541-LOW', perma_delete = True)
      delete_secret('test-secret-1583522541-MID', perma_delete = True)
      delete_secret('test-secret-1583522541-HIGH', perma_delete = True)
      delete_secret('test-secret-1583522541-', perma_delete = True)
      
  def test_secret_json(self):
    try:
      res_json = create_secret(f"test-secret-json", "test json secret from unit testing secrets manager", kvp = {'test': 'value'})
      self.assertIsNotNone(res_json)
      self.assertIsNotNone(res_json.get('ARN'))
      self.assertEqual(res_json.get('Name'), f'test-secret-json')
      self.assertEqual(json.loads(res_json.get('SecretString')), {'test': 'value'})
    except Exception as e:
      self.fail(f'Failed to create json secret, see exception:\n{e}')
    finally:
      delete_secret('test-secret-json', perma_delete = True)

  def test_secret_binary(self):
    try:
      res_binary = create_secret(f"test-secret-bin", "test binary secret from unit testing secrets manager", binary=b'test-binary')
      self.assertIsNotNone(res_binary)
      self.assertIsNotNone(res_binary.get('ARN'))
      self.assertEqual(res_binary.get('Name'), f"test-secret-bin")
      self.assertEqual(res_binary.get('SecretBinary'), b'test-binary')
    except Exception as e:
      self.fail(f'Failed to create binary secret, see exception:\n{e}')
    finally:
      delete_secret('test-secret-bin', perma_delete = True)

  def test_delete_time(self):
    stamp = f'{time.time()}'.split('.')[0]

    create_secret(f"test-secret-{stamp}", "test secret from unit testing secrets manager", string = "shh")
    self.assertTrue(delete_secret(f'test-secret-{stamp}', perma_delete = True))
    create_secret(f"test-secret-{stamp}-DEFAULT", "test secret from unit testing secrets manager", string = "shh")
    self.assertEqual(delete_secret(f'test-secret-{stamp}-DEFAULT'), 7)
    create_secret(f"test-secret-{stamp}-LOW", "test secret from unit testing secrets manager", string = "shh")
    self.assertEqual(delete_secret(f'test-secret-{stamp}-LOW', 1), 7)
    create_secret(f"test-secret-{stamp}-MID", "test secret from unit testing secrets manager", string = "shh")
    self.assertEqual(delete_secret(f'test-secret-{stamp}-MID', 15), 15)
    create_secret(f"test-secret-{stamp}-HIGH", "test secret from unit testing secrets manager", string = "shh")
    self.assertEqual(delete_secret(f'test-secret-{stamp}-HIGH', 40), 30)

  def test_get_secret(self):
    try:
      create_secret('test-get-secret-plain', 'test getting secrets while unit testing secrets manager', string = 'asdf')
      self.assertEqual(get_secret_value('test-get-secret-plain'), 'asdf')
      create_secret('test-get-secret-json', 'test getting secrets while unit testing secrets manager', kvp = {'this': 'is', 'values': 'definition'})
      self.assertEqual(json.loads(get_secret_value('test-get-secret-json')), {'this': 'is', 'values': 'definition'})
      create_secret('test-get-secret-json-key', 'test getting single value from json secret', kvp = {'a': 'asdf', 'b': 'bnm,', 'c': 'cvbn'})
      self.assertEqual(get_secret_value('test-get-secret-json-key', 'b'), 'bnm,')
      create_secret('test-get-secret-binary', 'test getting binary value from secret', binary = b'asdfghjkl')
      self.assertEqual(get_secret_value('test-get-secret-binary'), b'asdfghjkl')
    finally:
      delete_secret('test-get-secret-plain', perma_delete = True)
      delete_secret('test-get-secret-json', perma_delete = True)
      delete_secret('test-get-secret-json-key', perma_delete = True)
      delete_secret('test-get-secret-binary', perma_delete = True)

  def test_update_secret(self):
    try:
      create_secret('test-update-secret-plain', 'test updating secrets while unit testing secrets manager', string = 'asdf')
      update_secret('test-update-secret-plain', string = 'jkljkl')
      self.assertEqual(get_secret_value('test-update-secret-plain'), 'jkljkl')

      create_secret('test-update-secret-json', 'test updating secrets while unit testing secrets manager', kvp = {'this': 'is', 'values': 'definition'})
      update_secret('test-update-secret-json', kvp = {'additional': 'pairs', 'get': 'added'})
      res = json.loads(get_secret_value('test-update-secret-json'))
      self.assertEquals(res, {'this': 'is', 'values': 'definition', 'additional': 'pairs', 'get': 'added'})

      create_secret('test-update-secret-json-overwrite', 'test updating json secret and overwriting', kvp = {'a': 'asdf', 'b': 'bnm,', 'c': 'cvbn'})
      overwriter = {'d': 'zxcv', 'e': 'uiop'}
      update_secret('test-update-secret-json-overwrite', kvp = overwriter, overwriteJson = True)
      self.assertEqual(json.loads(get_secret_value('test-update-secret-json-overwrite')), overwriter)

      create_secret('test-update-secret-binary', 'test getting binary value from secret', binary = b'asdfghjkl')
      update_secret('test-update-secret-binary', binary = b'jklasdf')
      self.assertEqual(get_secret_value('test-update-secret-binary'), b'jklasdf')
    finally:
      delete_secret('test-update-secret-plain', perma_delete = True)
      delete_secret('test-update-secret-json', perma_delete = True)
      delete_secret('test-update-secret-json-overwrite', perma_delete = True)
      delete_secret('test-update-secret-binary', perma_delete = True)