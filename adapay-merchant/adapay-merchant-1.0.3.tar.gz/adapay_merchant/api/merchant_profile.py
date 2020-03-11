from adapay_merchant.api import request_tools
from adapay_merchant.api.request_tools import request_post
import os


class MerchantProfile(object):

    @classmethod
    def mer_profile_picture(cls, **kwargs):
        """
        代理商（渠道商）上送商户证照
        :param kwargs:
        :return:
        """

        file_path = kwargs.get('file')
        file_dict = {'file': (os.path.basename(file_path), open(file_path, 'rb'), 'application/octet-stream')}
        kwargs.pop('file')
        return request_post(request_tools.profile_picture, kwargs, file_dict)

    @classmethod
    def mer_profile_for_audit(cls, **kwargs):
        """
        代理商（渠道商）将商户证照信息提交审核接口
        :param kwargs:
        :return:
        """

        return request_post(request_tools.profile_audit, kwargs)


