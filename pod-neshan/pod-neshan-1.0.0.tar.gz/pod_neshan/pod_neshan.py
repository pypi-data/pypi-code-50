# coding=utf-8
import json
from os import path

from pod_base import PodBase
from . import response_handler


class PodNeshan(PodBase):
    __slots__ = "__raw_result"

    def __init__(self, api_token, token_issuer="1", config_path=None, sc_api_key="",
                 sc_voucher_hash=None):
        self.__raw_result = {}
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodNeshan, self).__init__(api_token, token_issuer, PodBase.PRODUCTION_MODE, config_path, sc_api_key,
                                        sc_voucher_hash, path.join(here, "json_schema.json"))

    def search(self, term, lat, lng, **kwargs):
        """
        جستجو

        :param str term: مختصات مبدا
        :param float lat: مختصات مقصد
        :param float lng: لیست مختصات نقاط میانی
        :return: dict
        """
        kwargs["term"] = term
        kwargs["lat"] = lat
        kwargs["lng"] = lng

        self._validate(kwargs, "search")

        print(kwargs)
        self._request.call(super(PodNeshan, self)._get_sc_product_settings("/search"), params=kwargs,
                           headers=self._get_headers(), internal=False, **kwargs)

        return self.__parse_response()

    def reverse_geo(self, lat, lng, **kwargs):
        """
        تبدیل مختصات به آدرس

        :param float lat: مختصات مقصد
        :param float lng: لیست مختصات نقاط میانی
        :return: dict
        """
        kwargs["lat"] = lat
        kwargs["lng"] = lng

        self._validate(kwargs, "reverseGeo")

        print(kwargs)
        self._request.call(super(PodNeshan, self)._get_sc_product_settings("/reverseGeo"), params=kwargs,
                           headers=self._get_headers(), internal=False, **kwargs)

        return self.__parse_response()

    def direction(self, origin, destination, way_points=None, **kwargs):
        """
        مسیریابی با ترافیک

        :param dict origin: مختصات مبدا
        :param dict destination: مختصات مقصد
        :param list way_points: لیست مختصات نقاط میانی
        :return: dict
        """
        kwargs["origin"] = origin
        kwargs["destination"] = destination
        kwargs["way_points"] = way_points

        return self.__direction(with_traffic=True, **kwargs)

    def no_traffic_direction(self, origin, destination, way_points=None, **kwargs):
        """
        مسیریابی بدون ترافیک

        :param dict origin: مختصات مبدا
        :param dict destination: مختصات مقصد
        :param list way_points: لیست مختصات نقاط میانی
        :return: dict
        """
        kwargs["origin"] = origin
        kwargs["destination"] = destination
        kwargs["way_points"] = way_points

        return self.__direction(with_traffic=False, **kwargs)

    def __direction(self, origin, destination, way_points=None, with_traffic=False, **kwargs):
        """
        مسیریابی

        :param dict origin: مختصات مبدا
        :param dict destination: مختصات مقصد
        :param list way_points: لیست مختصات نقاط میانی
        :param bool with_traffic: آیا ترافیک لحاظ شود
        :return: dict
        """

        if with_traffic:
            api_name = "direction"
        else:
            api_name = "noTrafficDirection"

        if way_points is not None:
            kwargs["waypoints"] = way_points

        kwargs["origin"] = origin
        kwargs["destination"] = destination
        self._validate(kwargs, api_name)
        kwargs["origin"] = "{},{}".format(origin["lat"], origin["lng"])
        kwargs["destination"] = "{},{}".format(destination["lat"], destination["lng"])

        if way_points is not None:
            kwargs["waypoints"] = self.__convert_points_list_to_str(way_points)
        print(kwargs)
        self._request.call(super(PodNeshan, self)._get_sc_product_settings("/" + api_name), params=kwargs,
                           headers=self._get_headers(), internal=False, **kwargs)
        return self.__parse_response()

    def distance_matrix(self, origins, destinations, **kwargs):
        """
        تعیین فاصله و زمان بین دو مختصات یا تعدادی بیشتر با در نظر گرفتن ترافیک

        :param list origins: لیست مختصات مبدا
        :param list destinations: لیست مختصات مقصد
        :return: dict
        """
        kwargs["origins"] = origins
        kwargs["destinations"] = destinations
        return self.__distance_matrix(with_traffic=True, **kwargs)

    def no_traffic_distance_matrix(self, origins, destinations, **kwargs):
        """
        تعیین فاصله و زمان بین دو مختصات یا تعدادی بیشتر بدون در نظر گرفتن ترافیک

        :param list origins: لیست مختصات مبدا
        :param list destinations: لیست مختصات مقصد
        :return: dict
        """
        kwargs["origins"] = origins
        kwargs["destinations"] = destinations
        return self.__distance_matrix(with_traffic=False, **kwargs)

    def __distance_matrix(self, origins, destinations, with_traffic=False, **kwargs):
        """
        تعیین فاصله و زمان بین دو مختصات یا تعدادی بیشتر

        :param list origins: لیست مختصات مبدا
        :param list destinations: لیست مختصات مقصد
        :param bool with_traffic: آیا ترافیک لحاظ شود
        :return: dict
        """

        if with_traffic:
            api_name = "distanceMatrix"
        else:
            api_name = "noTrafficDistanceMatrix"

        kwargs["origins"] = origins
        kwargs["destinations"] = destinations
        self._validate(kwargs, api_name)
        kwargs["origins"] = self.__convert_points_list_to_str(origins)
        kwargs["destinations"] = self.__convert_points_list_to_str(destinations)
        print(kwargs)

        self._request.call(super(PodNeshan, self)._get_sc_product_settings("/" + api_name), params=kwargs,
                           headers=self._get_headers(), internal=False, **kwargs)

        return self.__parse_response()

    def map_matching(self, points_location, **kwargs):
        """
        نگاشت نقطه بر نقشه

        :param list points_location: لیست مختصات نقاط
        :return: dict
        """
        kwargs["path"] = points_location

        self._validate(kwargs, "mapMatching")
        kwargs["path"] = self.__convert_points_list_to_str(points_location)

        print(kwargs)

        self._request.call(super(PodNeshan, self)._get_sc_product_settings("/mapMatching"), params=kwargs,
                           headers=self._get_headers(), internal=False, **kwargs)

        return self.__parse_response()

    @staticmethod
    def __convert_points_list_to_str(points):
        if type(points) == list:
            return "|".join([str(point["lat"]) + "," + str(point["lng"]) for point in points])

        return ""

    def __parse_response(self):
        return response_handler.parse_response(self._request, self._request._reference_number)

    def raw_result(self):
        return self.__raw_result
