from adapay_merchant.api import request_tools
from adapay_merchant.api.request_tools import request_post, request_get


class MerchantPayConf(object):
    @classmethod
    def create(cls, **kwargs):
        """
        商户入驻
        """
        return request_post(request_tools.pay_conf_create, kwargs)

    @classmethod
    def query(cls, **kwargs):
        """
         商户入驻查询
        """
        return request_get(request_tools.pay_conf_query, kwargs)

    @classmethod
    def modify(cls, **kwargs):
        """
         商户入驻修改
        """
        return request_post(request_tools.pay_conf_modify, kwargs)


