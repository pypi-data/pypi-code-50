# coding=utf-8
import json
from os import path

from pod_base import PodBase
from .response_handler import response_handler

class PodAI(PodBase):
    __slots__ = "__raw_result"

    def __init__(self, api_token, token_issuer="1", config_path=None, sc_api_key="",
                 sc_voucher_hash=None):
        self.__raw_result = {}
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodAI, self).__init__(api_token, token_issuer, PodBase.PRODUCTION_MODE, config_path, sc_api_key,
                                    sc_voucher_hash, path.join(here, "json_schema.json"))

    def speech_to_text(self, link_file, **kwargs):
        """
        تبدیل صوت به متن

        :param str link_file:  آدرس فایل صوتی
        :return: dict
        """
        kwargs["linkFile"] = link_file

        self._validate(kwargs, "speechToText")

        return self.__parse_response(self._request.call(super(PodAI, self)._get_sc_product_settings("/speechToText"),
                                                        params=kwargs, headers=self._get_headers(), internal=False,
                                                        **kwargs))

    def image_processing_authentication(self, image1, image2, mode, **kwargs):
        """
        احراز هویت از روی عکس

        :param str image1:  آدرس فایل تصویر اول
        :param str image2:  آدرس فایل تصویر دوم
        :param str mode:  آدرس فایل تصویر دوم
        :return: dict
        """
        kwargs["image1"] = image1
        kwargs["image2"] = image2
        kwargs["mode"] = mode

        self._validate(kwargs, "imageProcessingAuthentication")
        return self.__parse_response(
            self._request.call(super(PodAI, self)._get_sc_product_settings("/imageProcessingAuthentication"),
                               params=kwargs, headers=self._get_headers(), internal=False, **kwargs))

    def nlu_banking(self, text, **kwargs):
        """
        فهم متن در حوزه بانکی

        :param str text:  متن
        :return: dict
        """
        kwargs["text"] = text

        self._validate(kwargs, "NLUBanking")
        return self.__parse_response(self._request.call(super(PodAI, self)._get_sc_product_settings("/NLUBanking"),
                                                        params=kwargs, headers=self._get_headers(), internal=False,
                                                        **kwargs))

    def nlu_iot(self, text, **kwargs):
        """
        فهم متن در حوزه اینترنت چیزها

        :param str text:  متن
        :return: dict
        """
        kwargs["text"] = text

        self._validate(kwargs, "NLUIOT")
        return self.__parse_response(self._request.call(super(PodAI, self)._get_sc_product_settings("/NLUIOT"),
                                                        params=kwargs, headers=self._get_headers(), internal=False,
                                                        **kwargs))

    def license_plate_reader(self, image, is_crop=False, **kwargs):
        """
        پلاک خوان

        :param str image:  آدرس فایل تصویر
        :param bool is_crop:
        :return: list
        """
        kwargs["image"] = image
        kwargs["isCrop"] = is_crop

        self._validate(kwargs, "plate")
        return self.__parse_response(self._request.call(super(PodAI, self)._get_sc_product_settings("/plate"),
                                                        params=kwargs, headers=self._get_headers(), internal=False,
                                                        **kwargs))

    def __parse_response(self, result):
        result = json.loads(result)
        self.__raw_result = result.copy()
        return response_handler(result, self._request._reference_number)

    def raw_result(self):
        return self.__raw_result
