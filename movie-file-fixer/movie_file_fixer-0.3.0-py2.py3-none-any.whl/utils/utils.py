# -*- coding: utf-8 -*-
"""

Description: A compilation of utility methods for testing or production purposes.
"""

import hashlib
import math
import os
import pathlib
import shutil


def listdir_fullpath(directory):
    """

    :param str directory: The directory to search in.
    :return list: A list of files and folders as their full path.

    Returns the full path of every file or folder within a given directory.
    """
    return [os.path.join(directory, file_or_folder) for file_or_folder in os.listdir(directory)]


def is_in_list(element, the_list):
    """
    Prints boolean value of whether the element is in the list.

    * element can be a singleton value or a list of values.
    * the_list can be a single list or a list of lists.
    """
    return any([element in the_list]) or any([element in row for row in the_list])


def is_in_folder(path=None, name=None):
    """

    :param str path: The full (or relative) path of the directory to search in.
    :param str name: The file or folder name to search for.
    :return bool: True or False if the file or folder is located in the given folder path.

    Returns a boolean value whether the file or folder is located in the given folder path.
    """
    if os.path.exists(path):
        return name in os.listdir(path)
    else:
        # If the path doesn't exist, the file or folder can't very well exist in it.
        return False


def find_single_files(directory):
    """

    :param str directory: The directory to look for single files.
    :return list: A list of all single files in a given directory.

    Finds all the files without a folder within a given directory
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def find_folders(directory):
    """

    :param str directory: The directory to look for folders.
    :return list: A list of folders in the given directory.

    Finds all the folders in a given directory
    """
    return [os.path.join(directory, o) for o in os.listdir(directory) if os.path.isdir(os.path.join(directory, o))]


def get_child_file_or_folder_name(path):
    """

    :param str path: The full path to the child file or folder.
    :return str: The file or folder name.

    Returns the child file or folder name, given a full path.
    """
    return path.split(os.sep)[-1]


def get_parent_folder_name(path):
    """

    :param str path: The full path to the file or folder.
    :return str: The parent folder name.

    Returns the parent folder name, given a full path.
    """
    return str(pathlib.Path(path).parent)


def get_parent_and_child(path):
    """

    :param str path: The full path to the child file or folder.
    :return tuple: The parent folder name and the child file or folder name.

    Returns the parent folder name and the child file or folder name as a tuple.
    """
    return get_parent_folder_name(path=path), get_child_file_or_folder_name(path=path)


def silent_remove(path):
    """

    :param str path: The path of the file or folder to remove.
    :return None:

    Removes a given file or folder path, unless it raises an error.
    Doesn't throw an error if the file or folder is non-existent.
    """
    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path)


def create_trimmed_file(filepath, chunksize=64):
    """

    :param str filepath: The path of the file to be trimmed.
    :param int chunksize: The size (in KB) of the chunks.
    :return str: The new filename, which is also the `md5` hash of the new file.

    This method will take the file at the given filepath and pull two `chunksize` (in KB) sized chunks
    from the beginning and end of the file. It will then perform an `md5` hash of those chunks and
    create a new file with the hash as the filename.
    """
    readsize = chunksize * 1024
    with open(filepath, 'rb') as infile:
        data = infile.read(readsize)
        infile.seek(-readsize, os.SEEK_END)
        data += infile.read(readsize)

    root, filename = get_parent_and_child(path=filepath)
    name, extension = os.path.splitext(filename)

    new_filename = hashlib.md5(data).hexdigest() + extension
    new_filepath = os.path.join(root, new_filename)
    with open(new_filepath, 'wb') as outfile:
        outfile.write(data)

    return new_filename


def create_random_file(directory, filename, file_extension=None, filesize=128, units='kb'):
    """

    :param str directory: The directory to create the file in.
    :param str file_extension: The file extension of the file to write, if desired.
    :param int filesize: The size of the file to create.
    :param str units: The size units to use. Valid Options: ['b', 'kb', 'mb'].
    :return str: The `md5` hash of the file created.

    Writes a random file at the given `filepath` of size `filesize` (in `units`).

    i.e., If `filesize=128` and `units='kb'`, a file of size 128 KB will be written.
    """
    # 1024 ^ indexof(units)
    # 1024 ^ 0 = 1 Byte
    # 1024 ^ 1 = 1 Kilobyte
    # 1024 ^ 2 = 1 Megabyte
    kb_modifiers = ['b', 'kb', 'mb']
    if units not in kb_modifiers:
        raise Exception(f'[ERROR] Choose one of the following: {kb_modifiers}')

    # Determine the actual size of the file to write based on the index of the specified `units` parameter in
    # the `kb_modifiers` list (multiplied by the specified `filesize` parameter)
    writesize = filesize * math.pow(1024, kb_modifiers.index(units))

    filename += file_extension if file_extension is not None else ''
    filepath = os.path.join(directory, filename)
    random_bytes = os.urandom(int(writesize))
    random_bytes_hash = hashlib.md5(random_bytes).hexdigest()
    with open(filepath, 'wb') as outfile:
        outfile.write(random_bytes)

    return random_bytes_hash
