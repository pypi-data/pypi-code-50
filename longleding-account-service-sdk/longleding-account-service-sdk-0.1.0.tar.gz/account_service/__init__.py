# -*- coding: utf-8 -*-
import inspect
from typing import List

from .models import UserPagination, User
from .grpc_client import AccountServiceGRPCClient

__all__ = [
    "init_service"
]

_client: AccountServiceGRPCClient


def _param_check(func):
    def wrapper(*args, **kwargs):
        global _client
        assert _client is not None, "system settings service sdk must be init first"
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        for i, v in enumerate(args):
            p = params[i]
            assert p.annotation is inspect.Parameter.empty or isinstance(v, p.annotation), "{} must be {}.".format(
                p.name, str(p.annotation))
        return func(*args, **kwargs)

    return wrapper


def init_service(endpoint: str, src: str) -> None:
    global _client
    assert type(endpoint) == str, "endpoint must be a str"
    _client = AccountServiceGRPCClient(endpoint=endpoint, src=src)


@_param_check
def get_user_list(id_list: list) -> List[User]:
    return _client.get_user_list(id_list)


@_param_check
def get_user_page_list(current_page: int = 1, page_size: int = 10, username: str = '',
                       phone: str = '', email: str = '') -> UserPagination:
    return _client.get_user_page_list(current_page, page_size, username, phone, email)
