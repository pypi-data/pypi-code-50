from functools import wraps
import yaml
from .boa_obj import boa
from .boa_wrap import boa_wrap


def boa_wrap_yaml(fun, Loader):
    @wraps(fun)
    def dec(*args, **kwargs):
        return boa(fun(*args, Loader=Loader, **kwargs))
    return dec


load = boa_wrap_yaml(yaml.load, Loader=yaml.SafeLoader)  # make safe_load the default
load_all = boa_wrap_yaml(yaml.load_all, Loader=yaml.SafeLoader)  # make safe_load the default

safe_load = boa_wrap(yaml.safe_load)
unsafe_load = boa_wrap(yaml.unsafe_load)
full_load = boa_wrap(yaml.full_load)
