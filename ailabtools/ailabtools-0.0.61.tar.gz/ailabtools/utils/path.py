import os

def dir_path(p):
    return os.path.abspath(os.path.join(p, os.pardir))

def makedirs(p):
    os.makedirs(p, exist_ok=True)

def ensure_dir(p):
    makedirs(dir_path(p))

def readlines(file, spliter=None):
    with open(file, 'r', encoding='utf8') as f:
        all_line = f.readlines()
        all_line = [l.strip() for l in all_line]
        if spliter is not None:
            all_line = [l.split(spliter) for l in all_line]
    return all_line