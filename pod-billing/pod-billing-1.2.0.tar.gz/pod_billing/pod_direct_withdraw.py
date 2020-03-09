# coding=utf-8
from __future__ import absolute_import
from os import path

from pod_base import PodBase, calc_offset, InvalidDataException


class PodDirectWithdraw(PodBase):

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services_direct_withdraw.json")
        super(PodDirectWithdraw, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                                sc_voucher_hash, path.join(here, "json_schema_direct_withdraw.json"))

    def define_direct_withdraw(self, username, private_key, deposit_number, wallet, on_demand, min_amount, max_amount,
                               **kwargs):
        """
        تعریف امکان برداشت از سپرده مشتری توسط انتقال وجه

        :param str username: نام کاربری وب سرویس دریافتی از بانک
        :param str private_key: محتویات کلید خصوصی دریافتی از بانک
        :param str deposit_number: شماره حساب مبدا در بانک پاسارگاد
        :param str wallet: کد کیف پول
        :param bool on_demand: تامین موجودی کیف پول در لحظه، در زمان کمبود موجودی
        :param int min_amount: حداقل موجودی در کیف پول برای برداشت به اندازه `max_amount` در زمان کمبود موجودی
        :param int max_amount: حداکثر مبلغ افزایش موجودی در زمان کمبود موجودی
        :return: dict
        """
        kwargs["username"] = username
        kwargs["privateKey"] = private_key
        kwargs["depositNumber"] = deposit_number
        kwargs["wallet"] = wallet
        kwargs["onDemand"] = on_demand
        kwargs["minAmount"] = min_amount
        kwargs["maxAmount"] = max_amount

        self._validate(kwargs, "defineDirectWithdraw")

        return self._request.call(
            super(PodDirectWithdraw, self)._get_sc_product_settings("/nzh/biz/defineDirectWithdraw", method_type="post")
            , params=kwargs, headers=self._get_headers(), **kwargs)

    def direct_withdraw_list(self, page=1, size=50, **kwargs):
        """
        دریافت لیست مجوزها

        :param int page: شماره صفحه
        :param int size: تعداد در هر صفحه
        :return: list
        """
        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size
        self._validate(kwargs, "directWithdrawList")

        return self._request.call(
            super(PodDirectWithdraw, self)._get_sc_product_settings("/nzh/biz/directWithdrawList", method_type="post")
            , params=kwargs, headers=self._get_headers(), **kwargs)

    def update_direct_withdraw(self, id, username, private_key, deposit_number, wallet, on_demand, min_amount,
                               max_amount, **kwargs):
        """
        به روز رسانی مجوز برداشت مستقیم

        :param int id: شناسه مجوز پرداخت مستقیم
        :param str username: نام کاربری وب سرویس دریافتی از بانک
        :param str private_key: محتویات کلید خصوصی دریافتی از بانک
        :param str deposit_number: شماره حساب مبدا در بانک پاسارگاد
        :param str wallet: کد کیف پول
        :param bool on_demand: تامین موجودی کیف پول در لحظه، در زمان کمبود موجودی
        :param int min_amount: حداقل موجودی در کیف پول برای برداشت به اندازه `max_amount` در زمان کمبود موجودی
        :param int max_amount: حداکثر مبلغ افزایش موجودی در زمان کمبود موجودی
        :return: dict
        """
        kwargs["id"] = id
        kwargs["username"] = username
        kwargs["privateKey"] = private_key
        kwargs["depositNumber"] = deposit_number
        kwargs["wallet"] = wallet
        kwargs["onDemand"] = on_demand
        kwargs["minAmount"] = min_amount
        kwargs["maxAmount"] = max_amount

        self._validate(kwargs, "updateDirectWithdraw")

        return self._request.call(
            super(PodDirectWithdraw, self)._get_sc_product_settings("/nzh/biz/updateDirectWithdraw", method_type="post")
            , params=kwargs, headers=self._get_headers(), **kwargs)

    def revoke_direct_withdraw(self, id, **kwargs):
        """
        لغو مجوز برداشت مستقیم

        :param int id: شناسه مجوز پرداخت مستقیم
        :return: boolean
        """
        kwargs["id"] = id

        self._validate(kwargs, "revokeDirectWithdraw")

        return self._request.call(
            super(PodDirectWithdraw, self)._get_sc_product_settings("/nzh/biz/revokeDirectWithdraw", method_type="post")
            , params=kwargs, headers=self._get_headers(), **kwargs)
