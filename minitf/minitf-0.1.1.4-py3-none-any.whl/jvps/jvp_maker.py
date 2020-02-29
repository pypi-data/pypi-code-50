__PRIMITIVE_VJPS = {}


def def_vjp_maker(fun, vjp_maker):
    __PRIMITIVE_VJPS[fun] = vjp_maker


def get_vjp_maker(fun):
    return __PRIMITIVE_VJPS.get(fun)
