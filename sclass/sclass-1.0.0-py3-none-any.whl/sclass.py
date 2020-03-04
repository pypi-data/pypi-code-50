
class PrivateException(Exception):
    pass

class sclass(object):
    def __getattribute__(self, attr):
        if attr.startswith('__'):
            return super(sclass, self).__getattribute__(attr)
        else:
            try:
                if attr.startswith('_'):
                    raise PrivateException()
                else:
                    return super(sclass, self).__getattribute__(attr)
            except NameError:
                raise NameError
