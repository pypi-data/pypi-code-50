from .sqlite import SqliteStorageBackend

BACKENDS = {
    'sqlite': {
        'object': SqliteStorageBackend,
        'params': ['db_path']
    }
}