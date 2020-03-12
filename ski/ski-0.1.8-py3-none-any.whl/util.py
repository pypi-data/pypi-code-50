import os

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. '+directory)

def parent_directory(n):
    path = ''
    while n:
        path = os.path.join(path,os.pardir)
        n -= 1
    path = os.path.abspath(path)
    return path