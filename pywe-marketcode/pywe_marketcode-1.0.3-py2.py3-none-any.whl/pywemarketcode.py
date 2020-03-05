# -*- coding: utf-8 -*-

from pywe_decrypt.code import decrypt as code_decrypt
from pywe_token import BaseToken, final_access_token


class MarketCode(BaseToken):
    def __init__(self, appid=None, secret=None, token=None, storage=None):
        super(MarketCode, self).__init__(appid=appid, secret=secret, token=token, storage=storage)
        # 一物一码接口文档, Refer: https://developers.weixin.qq.com/doc/offiaccount/Unique_Item_Code/Unique_Item_Code_API_Documentation.html
        # 2.2 申请二维码接口
        self.APPLYCODE = self.API_DOMAIN + '/intp/marketcode/applycode'
        # 2.3 查询二维码申请单接口
        self.APPLYCODEQUERY = self.API_DOMAIN + '/intp/marketcode/applycodequery'
        # 2.4 下载二维码包接口
        self.APPLYCODEDOWNLOAD = self.API_DOMAIN + '/intp/marketcode/applycodedownload'
        # 2.5 激活二维码接口
        self.CODEACTIVE = self.API_DOMAIN + '/intp/marketcode/codeactive'
        # 2.6 查询二维码激活状态接口
        self.CODEACTIVEQUERY = self.API_DOMAIN + '/intp/marketcode/codeactivequery'
        # 2.7 code_ticket换code接口
        self.TICKETTOCODE = self.API_DOMAIN + '/intp/marketcode/tickettocode'

    def applycode(self, isv_application_id, code_count, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.APPLYCODE,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            data={
                'isv_application_id': isv_application_id,
                'code_count': code_count,
            },
        )

    def applycodequery(self, isv_application_id, application_id, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.APPLYCODEQUERY,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            data={
                'isv_application_id': isv_application_id,
                'application_id': application_id,
            },
        )

    def applycodedownload(self, application_id, code_start, code_end, appid=None, secret=None, token=None, storage=None, decrypted=True, iv=None):
        res = self.post(
            self.APPLYCODEDOWNLOAD,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            data={
                'application_id': application_id,
                'code_start': code_start,
                'code_end': code_end,
            },
        )
        # {
        #     "errcode": 80309,
        #     "errmsg": "子任务文件过期, ... hint: [6g6r8a0651d236]"
        # }
        if res.get('errcode') != 0:
            return res
        if not decrypted:
            return res
        return code_decrypt(res.get('buffer', ''), iv=iv)

    def codeactive(self, application_id, activity_name, product_brand, product_title, product_code, wxa_appid, wxa_path, code_start, code_end, wxa_type=0, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.CODEACTIVE,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            data={
                'application_id': application_id,
                'activity_name': activity_name,
                'product_brand': product_brand,
                'product_title': product_title,
                'product_code': product_code,
                'wxa_appid': wxa_appid,
                'wxa_path': wxa_path,
                'wxa_type': wxa_type,
                'code_start': code_start,
                'code_end': code_end,
            },
        )

    def codeactivequery(self, application_id=None, code_index=None, code=None, code_url=None, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.CODEACTIVEQUERY,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            data={
                'application_id': application_id,
                'code_index': code_index,
                'code': code,
                'code_url': code_url,
            },
        )

    def tickettocode(self, code_ticket, openid, appid=None, secret=None, token=None, storage=None):
        return self.post(
            self.TICKETTOCODE,
            params={
                'access_token': final_access_token(self, appid=appid, secret=secret, token=token, storage=storage),
            },
            data={
                'code_ticket': code_ticket,
                'openid': openid,
            },
        )


marketcode = MarketCode()
applycode = marketcode.applycode
applycodequery = marketcode.applycodequery
applycodedownload = marketcode.applycodedownload
codeactive = marketcode.codeactive
codeactivequery = marketcode.codeactivequery
tickettocode = marketcode.tickettocode
