import re
from collections import namedtuple

Route = namedtuple('Route', ('path', 'handler'))


def re_url(path, handler):
    return Route(re.compile(path), handler)


def resolve_url(urlpatterns, path):
    for route in urlpatterns:
        match = route.path.match(path)
        if not match:
            continue

        kwargs_indexes = route.path.groupindex.values()
        args = tuple(filter(lambda arg: arg not in kwargs_indexes, match.groups()))
        kwargs = match.groupdict()

        return route.handler, args, kwargs

    return None, None, None
