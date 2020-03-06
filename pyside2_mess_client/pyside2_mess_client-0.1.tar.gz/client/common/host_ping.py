# -*- coding: utf-8 -*-
# Date: 19.10.2019 22:02
# Author: MaximRaduntsev

import ipaddress as ip
from typing import Optional, Any, Callable
import socket

is_ip_address: Callable[[Any], Optional[str]] = lambda ip_host: str(ip.ip_address(ip_host)) \
    if type(ip_host) in (str, int) else None
is_host_name: Callable[[Any], Optional[Any]] = lambda host_name: host_name \
    if socket.gethostbyname(host_name) else None


def host_ping(host):
    try:
        host = is_ip_address(host)
    except Exception as e:
        try:
            host = is_host_name(host)
            # print(f'{host} - {e}, воспринимаю как доменное имя')
        except Exception as e:
            print(f'{host} - {e}, Не верные параметры узла')
    return host
