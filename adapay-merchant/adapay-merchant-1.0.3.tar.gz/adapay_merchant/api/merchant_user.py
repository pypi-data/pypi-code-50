from adapay_merchant.api import request_tools
from adapay_merchant.api.request_tools import request_post, request_get


class MerchantUser(object):
    @classmethod
    def create(cls, **kwargs):
        """
        商户开户进件
        """
        return request_post(request_tools.merchant_user_create, kwargs)

    @classmethod
    def query(cls, **kwargs):
        """
        查询商户开户信息
        """
        return request_get(request_tools.merchant_user_query, kwargs)


