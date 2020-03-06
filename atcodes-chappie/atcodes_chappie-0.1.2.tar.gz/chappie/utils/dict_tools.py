import sys
import collections


class DictTools():
    """ Dicttools provides some dictionary helper functions """
    @staticmethod
    def update_dict(dictionary, new_record):
        """Update dict.
        - Updates the dictionary (add new or update data if record already exists)
        """
        # Python3 replace iteritems() with items()
        if sys.version_info < (3, 0):
            key_value_list = new_record.iteritems()
        else:
            key_value_list = new_record.items()

        for k, v in key_value_list:
            if isinstance(v, collections.Mapping):
                r = DictTools.update_dict(dictionary.get(k, {}), v)
                dictionary[k] = r
            else:
                dictionary[k] = new_record[k]
        return dictionary
