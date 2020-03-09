
import random
import string
import os


def gnr_string(length=4):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def gnr_path(prefix='test', min_layer=1, max_layer=3):
    if prefix:
        return os.path.join(
            prefix,
            '/'.join([gnr_string() for _ in range(random.randint(min_layer, max_layer))])
        )
    else:
        return '/'.join([gnr_string() for _ in range(random.randint(min_layer, max_layer))])
