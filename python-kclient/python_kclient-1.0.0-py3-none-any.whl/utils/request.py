import base64
import os


def make(data: dict = None, files: dict = None) -> dict:

    req = {}

    if data is not None:
        for k in data:
            if type(data[k]) == str or type(data[k]) == int or type(data[k]) == float:
                val = data[k]
            else:
                raise ValueError(f'unsupported data type {type(data[k])}')
            req[k] = val

    if files is not None:
        for k in files:
            if not os.path.isfile(files[k]):
                raise ValueError(f'file {k} is absent')
            with open(files[k], "rb") as image_file:
                data = base64.b64encode(image_file.read()).decode()
            req[k] = data

    return req
