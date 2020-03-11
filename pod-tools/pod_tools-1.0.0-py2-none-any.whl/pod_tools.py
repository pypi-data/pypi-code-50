# coding=utf-8
from os import path

from pod_base import PodBase, calc_offset


class PodTools(PodBase):

    def __init__(self, api_token, token_issuer="1", config_path=None, sc_api_key="",
                 sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodTools, self).__init__(api_token, token_issuer, PodBase.PRODUCTION_MODE, config_path, sc_api_key,
                                       sc_voucher_hash, path.join(here, "json_schema.json"))

    def pay_bill(self, bill_id, payment_id, access_token=None, **kwargs):
        """
        پرداخت قبض خدماتی از طریق موجودی کیف پول

        :param str bill_id:  شناسه قبض
        :param str payment_id:  شناسه پرداخت
        :param str access_token:  اکسس توکن کاربر، در صورت ارسال این پارامتر، توکن کسب و کار در نظر گرفته نخواهد شد
        :return: dict
        """
        kwargs["billId"] = bill_id
        kwargs["paymentId"] = payment_id

        headers = self._get_headers()
        if access_token is not None:
            headers["_token_"] = access_token

        self._validate(kwargs, "payServiceBill")

        return self._request.call(super(PodTools, self)._get_sc_product_settings("/nzh/payServiceBill"), params=kwargs,
                                  headers=headers, **kwargs)

    def payed_bill_list(self, page=1, size=50, access_token=None, **kwargs):
        """
        لیست قبض های پرداخت شده

        :param int page:  شماره صفحه
        :param int size:  تعداد رکورد در خروجی
        :param str access_token:  اکسس توکن کاربر، در صورت ارسال این پارامتر، توکن کسب و کار در نظر گرفته نخواهد شد
        :return: list
        """
        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size

        headers = self._get_headers()
        if access_token is not None:
            headers["_token_"] = access_token

        self._validate(kwargs, "getServiceBillList")

        return self._request.call(super(PodTools, self)._get_sc_product_settings("/nzh/getServiceBillList"),
                                  params=kwargs, headers=headers, **kwargs)
