import os

from collections import ChainMap


class DictionaryHelper(object):
    """
    Dictionary utilities.
    """

    @classmethod
    def inverse(cls, dict_):
        """
        Convert the input dictionary and inverse the key/value pairs.
        :param dict_: the input `dict` to convert.
        """
        return {value: key for key, value in dict_.items()}

    @classmethod
    def merge(cls, *dicts):
        """
        Merge mappings together into a single dictionary.
        :param *dicts: any number of `dict` objects to merge.
        """
        return dict(ChainMap(*dicts))


class Mapping(dict):
    """
    Dict subclass to add a fallback value for unmapped values.
    """

    def __missing__(self, key):
        return key


def add_file_affix(filename, affix):
    """
    Adds a affix to a filename before the extension.
    :param filename: raw filename to affix.
    :param affix: the affix to add.
    """
    parts = filename.split('.')
    parts[-2] += affix
    return '.'.join(parts)


def rename_file_in_path(path, new_name):
    """
    Rename the filename part of a complete path. The file extension is
    preserved with this rename.
    :param path: the complete path, containing the filename and extension.
    :param new_name: the new filename, excluding the extension.
    """
    path, file = os.path.split(path)
    file, extension = os.path.splitext(file)
    return os.path.join(path, (new_name + extension))
