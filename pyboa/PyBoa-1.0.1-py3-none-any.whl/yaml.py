from functools import wraps
import yaml
from .boa_obj import boa
from .boa_wraps import boa_wraps


def boa_wraps_yaml(fun, Loader):
    @wraps(fun)
    def dec(*args, **kwargs):
        return boa(fun(*args, Loader=Loader, **kwargs))
    return dec


load = boa_wraps_yaml(yaml.load, Loader=yaml.SafeLoader)  # make safe_load the default
load_all = boa_wraps_yaml(yaml.load_all, Loader=yaml.SafeLoader)  # make safe_load the default

safe_load = boa_wraps(yaml.safe_load)
unsafe_load = boa_wraps(yaml.unsafe_load)
full_load = boa_wraps(yaml.full_load)
