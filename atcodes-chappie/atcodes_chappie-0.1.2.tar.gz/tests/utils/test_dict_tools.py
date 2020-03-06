from unittest import TestCase

from chappie.utils.dict_tools import DictTools


class TestDictTools(TestCase):
    """Test Dict Tools"""

    def setUp(self):
        """Some Initial data setup"""
        self.tmp_dict = {
            'item1': '1',
            'item2': '2',
            'group1': {
                'item1': '11',
                'item2': '12',
            }
        }

        self.dict_to_append = {
            'group2': {
                'item2': '22',
            }
        }

        self.dict_to_update = {
            'group1': {
                'item1': 'one-one',
            }
        }

    def tearDown(self):
        """ """

    def test_dict_tools_update(self):
        """Adding and updating dictionary should work at depth"""

        self.tmp_dict = DictTools.update_dict(self.tmp_dict, self.dict_to_append)
        self.assertEqual(self.tmp_dict['group2']['item2'], '22')

        self.tmp_dict = DictTools.update_dict(self.tmp_dict, self.dict_to_update)
        self.assertEqual(self.tmp_dict['group1']['item1'], 'one-one')
