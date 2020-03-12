import inspect
import re
import socket
from datetime import tzinfo
from functools import partial
from types import CodeType, FunctionType, ModuleType
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from pytz import timezone

# script config
gloabl_conf_reg = re.compile(r'__upload_(\w+)__', re.I | re.UNICODE)
# timezone setting,
tz_reg = re.compile(r'GMT([+-]?\d{1,2})(:\d{1,2})?', re.I)


def get_name(type_):
    try:
        return type_.__name__
    except AttributeError:
        return type(type_).__name__


def get_default_port(schema: str):
    """return conanical transport protocol port number

    :param schema: [description]
    :type schema: str
    """
    # IANA internet service
    try:
        socket.getservbyname(schema)
    except OSError:
        # not a IANA assigned service
        # TODO: add hdfs, redis default port
        return None


def get_module_configs(module: ModuleType) -> Dict[str, Any]:
    """extract global variable from module's global namespace
    gloabl name like __upload_{name}__ consider as a configure
    :return: [description]
    :rtype: [type]
    """
    configs: Dict[str, Any] = {}
    for name in vars(module).keys():
        config_match = gloabl_conf_reg.match(name)
        if config_match:
            configs.update({config_match.group(1):
                            getattr(module, name)
                            })

    return configs


def get_tz(tz_str: str) -> tzinfo:
    """get timezone info from tz string, string must conform to
    ``GMT[+|-]TZH:TZM``, TZH, TZM represents timezone hour,minute
    offset to UTC time

    .. caution::
    current timezone minute part truncate
    TODO: add minute info

    :param tz_str: string conform to timezone literal expression
    :type tz_str: str
    :raises ValueError: con't parse tz str correctly or it contains
        not wrong values.
    :return: timezone info
    :rtype: tzinfo

    >>> from pytz import timezone
    >>> tz_str = "GMT+08"
    >>> tz = get_tz(tz_str)
    >>> tz == timezone("Etc/GTM+8)

    """
    tz = tz_reg.match(tz_str)
    if not tz:
        raise ValueError(
            "tz string [{}] must conform to pattern ``GMT[+|-]TZH:TZM".
            format(tz_str)
        )
    # tz_min contains ":" and optional
    tz_hour, tz_min = tz.groups()
    if tz_min:
        tz_min = tz_min[1:]
    print(tz_hour)
    if not -12 <= int(tz_hour) < 12:
        raise ValueError(
            "tz string [{}] timezone hour part must in [-12, 12)".
            format(tz_str)
        )
    if tz_min and 00 <= int(tz_min) < 60:
        raise ValueError(
            "tz string [{}] timezone minute part must in [0, 60)".
            format(tz_str)
        )

    return timezone("Etc/GMT{:+}".format(int(tz_hour)))


def to_callable(
    raw_func: Union[str, CodeType], g=None,
    defaults: Tuple[Any] = None,
    kwdefaults: Dict[str, Any] = None
) -> Callable:
    """convert function define to Callable object to called in
    later usage, currently not support clousers(netsted function)

    :param raw_func: input value
    :type raw_func: Union[str, CodeType]
    :param g: if raw_func is a ``CodeType`` or ``str``
        object, pass it to function
    :param defaults: defautls value passed to ``CodeType`` object
    :param kwdefaults: defautls only contain positional arguments defualt,
       this used to invlude kwonly keywords default
    :return: callable receive one arguemnt
    :rtype: Callable
    :raise ValueError: raw_func cann't construct a leagal callable
    """
    # global function
    g = g or {}

    def _check(func: Callable) -> Optional[Callable]:
        """check func only have one optional parameter

        if callable have any default value parameters, will bind
        them to the callable
        """
        emp: List = []
        argspec = inspect.getfullargspec(func)
        if len(argspec.args) - len(argspec.defaults or emp) != 1 or \
           len(argspec.kwonlyargs) - len(argspec.kwonlydefaults or emp) != 0:
            return None
        else:
            # default value
            bound = func
            if argspec.defaults:
                d_size = len(argspec.defaults)
                bound = partial(
                    bound,
                    **dict(zip(argspec.args[len(argspec.args)-d_size:],
                               argspec.defaults))
                )
            # kwar-default value
            if argspec.kwonlydefaults:
                bound = partial(
                    bound, **argspec.kwonlydefaults
                )

            return bound

    if callable(raw_func):
        func = raw_func
    elif isinstance(raw_func, str):
        prev_g = g.copy()
        exec(raw_func, prev_g)
        for var in prev_g:
            if var == "__builtins__":
                continue
            if callable(prev_g[var]) and var not in g:
                func = prev_g[var]
                break
        else:
            raise ValueError("no callable found in %s" % raw_func)
    else:
        func = FunctionType(
            raw_func, globals=g, name=raw_func.co_name,
            argdefs=defaults
        )
        if kwdefaults:
            func = partial(func, **kwdefaults)
    res = _check(func)

    if not res:
        raise ValueError("can not covert input to callable check:\n {!r}".
                         format(raw_func))
    return res
