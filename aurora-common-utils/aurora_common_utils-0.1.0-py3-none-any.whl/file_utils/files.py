import os
from os.path import abspath, dirname


def resource_content(file_name):
    f = open('resource/' + file_name, 'r', encoding='UTF-8')
    str_content = f.read()
    f.close()
    return str_content


def config_content(file_name):
    f = open('config/' + file_name, 'r', encoding='UTF-8')
    str_content = f.read()
    f.close()
    return str_content


def file_content(parent_dir_name, file_name):
    f = open(parent_dir_name + '/' + file_name, 'r', encoding='UTF-8')
    str_content = f.read()
    f.close()
    return str_content


def read_content(file_name, path):
    f = None
    try:
        base_dir = dirname(abspath(path))
        resource_full_path = os.path.join(base_dir, file_name)
        f = open(resource_full_path, 'r', encoding='UTF-8')
        str_content = f.read()
    finally:
        if f is not None:
            f.close()
    return str_content
