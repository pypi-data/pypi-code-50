import os


def getenv(key):
    return os.getenv(f'PYTHONANYWHERE_API_CLIENT_{key}')
