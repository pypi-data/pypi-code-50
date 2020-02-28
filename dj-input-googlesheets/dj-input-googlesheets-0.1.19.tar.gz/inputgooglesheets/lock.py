from django.conf import settings


CONNECTION = None

def _get_connection():
    import redis_lock
    global CONNECTION
    if CONNECTION is None:
        CONNECTION = redis_lock.StrictRedis(**getattr(settings, 'REDIS_LOCK_CONN', {}))
    return CONNECTION


def lock_creator(key):
    "Distributed lock with redis"
    import redis_lock
    return redis_lock.Lock(_get_connection(), key)
