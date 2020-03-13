import os


# Assets Configuration
ASSETS = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'assets')
assert os.path.isdir(ASSETS)


def get_file(fn) -> str:
    fp = os.path.join(ASSETS, fn)
    assert os.path.isfile(fp)
    return fp


def get_fn_contents(fn) -> bytes:
    fp = get_file(fn=fn)
    with open(fp, 'rb') as f:
        buf = f.read()
    return buf
