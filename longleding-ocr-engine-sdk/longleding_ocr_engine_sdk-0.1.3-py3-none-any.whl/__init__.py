# -*- coding: utf-8 -*-
import inspect

from .grpc_client import OcrEngineGRPCClient
from .models import OCREngineException

__all__ = [
    "init_service",
    "OCREngineException",
    "ocr_with_image_oss_path",
    "ocr_with_image_url",
    "ocr_with_image",
    "ocr_with_image_oss_path_and_rotate",
    "ocr_with_image_url_and_rotate",
    "ocr_with_image_and_rotate"
]
_client: OcrEngineGRPCClient


def _param_check(func):
    def wrapper(*args, **kwargs):
        global _client
        assert _client is not None, "ocr engine sdk must be init first"
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        for i, v in enumerate(args):
            p = params[i]
            assert p.annotation is inspect.Parameter.empty or isinstance(v, p.annotation), "{} must be {}.".format(p.name, str(p.annotation))
        return func(*args, **kwargs)
    return wrapper


def init_service(endpoint: str, src: str) -> None:
    global _client
    assert type(endpoint) == str, "endpoint must be a str"
    _client = OcrEngineGRPCClient(endpoint=endpoint, src=src)


@_param_check
def ocr_with_image_oss_path(oss_path: str = None) -> str:
    return _client.ocr_result_with_image_oss_path(oss_path)[0]


@_param_check
def ocr_with_image_url(image_url: str = None) -> str:
    return _client.ocr_result_with_image_url(image_url)[0]


@_param_check
def ocr_with_image(image: bytes = None) -> str:
    return _client.ocr_result_with_image(image)[0]


@_param_check
def ocr_with_image_oss_path_and_rotate(oss_path: str = None) -> (str, str):
    return _client.ocr_result_with_image_oss_path(oss_path)


@_param_check
def ocr_with_image_url_and_rotate(image_url: str = None) -> (str, str):
    return _client.ocr_result_with_image_url(image_url)


@_param_check
def ocr_with_image_and_rotate(image: bytes = None) -> (str, str):
    return _client.ocr_result_with_image(image)
