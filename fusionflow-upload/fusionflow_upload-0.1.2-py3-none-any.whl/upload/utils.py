import socket
import re
from typing import Dict, Any
from types import ModuleType

from pytz import timezone
from datetime import tzinfo

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
