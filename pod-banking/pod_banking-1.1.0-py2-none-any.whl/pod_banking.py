# coding=utf-8
import json
from collections import OrderedDict
from os import path

import xmltodict
from pod_base import PodBase, PodException, HTTPException, APIException
from .data_ordered import DataOrdered
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from sys import version_info
import base64

from datetime import datetime


class PodBanking(PodBase):
    __slots__ = ("__private_key", "__user_name", "__raw_result")

    def __init__(self, api_token, private_key_path, user_name, token_issuer="1", server_type="sandbox",
                 config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        self.__user_name = user_name
        self.__raw_result = {}
        self.__private_key = self.__load_private_key(private_key_path)
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodBanking, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                         sc_voucher_hash, path.join(here, "json_schema.json"))

    @staticmethod
    def __load_private_key(private_key_path):
        try:
            with open(private_key_path, "r") as private_key:
                return RSA.importKey(private_key.read())

        except FileNotFoundError:
            raise PodException("private key not found")

    def get_sheba_info(self, sheba, **kwargs):
        """
        دریافت اطلاعات صاحب شماره شبا

        :param str sheba:  شماره شبا
        :return: dict
        """
        kwargs["sheba"] = sheba

        self._validate(kwargs, "getShebaInfo")
        return self._request.call(super(PodBanking, self)._get_sc_product_settings("/nzh/biz/getShebaInfo"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def get_debit_card_info(self, card_number, **kwargs):
        """
        دریافت نام و نام خانوادگی صاحب حساب

        :param str card_number:  شماره کارت
        :return: str
        """
        kwargs["cardNumber"] = card_number

        self._validate(kwargs, "getDebitCardInfo")
        return self._request.call(super(PodBanking, self)._get_sc_product_settings("/nzh/biz/getDebitCardInfo"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def get_sheba_info_and_status(self, sheba, shenase_variz="", **kwargs):
        """
        دریافت اطلاعات شبا و وضعیت حساب مرتبط با آن

        :param str sheba: شماره شبا
        :param str shenase_variz: شناسه واریز
        :return: dict
        """
        params = {
            "Sheba": sheba,
            "ShenaseVariz": shenase_variz
        }

        params = self.__prepare_params(method_name="get_sheba_info_and_status", **params)

        self._validate(params, "getShebaInfoAndStatus")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getShebaInfoAndStatus"), params=params,
            headers=self._get_headers(), **kwargs), method="GetShebaInfo")

    def get_deposit_number_by_card_number(self, card_number, **kwargs):
        """
        دریافت اطلاعات شبا و وضعیت حساب مرتبط با آن

        :param str card_number: شماره کارت
        :return: str
        """
        params = {
            "CardNumber": card_number
        }

        params = self.__prepare_params(method_name="get_deposit_number_by_card_number", **params)

        self._validate(params, "getDepositNumberByCardNumber")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getDepositNumberByCardNumber"), params=params,
            headers=self._get_headers(), **kwargs), method="GetDepositNumberByCardNumber")

    def get_sheba_by_card_number(self, card_number, **kwargs):
        """
        دریافت شماره شبا حساب مرتبط با کارت

        :param str card_number: شماره کارت
        :return: str
        """
        params = {
            "CardNumber": card_number
        }

        params = self.__prepare_params(method_name="get_sheba_by_card_number", **params)

        self._validate(params, "getShebaByCardNumber")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getShebaByCardNumber"), params=params,
            headers=self._get_headers(), **kwargs), method="GetShebaByCardNumber")

    def get_card_information(self, source_card_number, destination_card_number, **kwargs):
        """
        دریافت شماره شبا حساب مرتبط با کارت

        :param str source_card_number: شماره کارت مبدا
        :param str destination_card_number: شماره کارت مقصد
        :return: str
        """
        params = {
            "SrcCardNumber": source_card_number,
            "DestCardNumber": destination_card_number
        }

        params = self.__prepare_params(method_name="get_card_information", **params)

        self._validate(params, "getCardInformation")
        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getCardInformation"), params=params,
            headers=self._get_headers(), **kwargs), method="GetCardInformation")

    def card_to_card(self, source_card_number, destination_card_number, password, cvv2, expire_month, expire_year,
                     amount, email='', authorization_code=0, card_name='', source_comment='', destination_comment='',
                     original_address='', extra_data=None, **kwargs):
        """
        کارت به کارت

        :param str source_card_number: شماره کارت مبدا
        :param str destination_card_number: شماره کارت مقصد
        :param str password: رمز دوم کارت - رمز پویا
        :param str cvv2:
        :param str expire_month: ماه انقضا کارت به صورت دو رقمی
        :param str expire_year: سال انقضا کارت به صورت دو رقمی
        :param int amount: مبلغ انتقال
        :param str email: ایمیل
        :param str authorization_code: کد شناسایی
        :param str card_name: نام کارت
        :param str source_comment: توضیحات مبدا
        :param str destination_comment: توضیحات مقصد
        :param str original_address: آدرس IP درخواست دهنده
        :param dict extra_data: شماره کارت مقصد
        :return: str
        """

        if extra_data is None:
            extra_data = {}

        authorization_code = str(authorization_code)

        if not authorization_code:
            with_reference_number = 'true'
        else:
            with_reference_number = 'false'

        params = {
            "SrcCardNumber": source_card_number,
            "DestCardNumber": destination_card_number,
            "Password": password,
            "Cvv2": cvv2,
            "ExpireMonth": expire_month,
            "ExpireYear": expire_year,
            "Amount": amount,
            "Email": email,
            "AuthorizationCode": authorization_code,
            "WithReferenceNumber": with_reference_number,
            "CardName": card_name,
            "SrcComment": source_comment,
            "DestComment": destination_comment,
            "OriginalAddress": original_address,
            "JsonData": extra_data
        }

        params = self.__prepare_params(method_name="card_to_card", **params)

        self._validate(params, "cardToCard")
        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/cardToCard", method_type="post"), params=params,
            headers=self._get_headers(), **kwargs), method="CardToCardTransferWithoutSubDeposit")

    def card_to_card_list(self, source_card_number, min_amount, max_amount, start_date, end_date,
                          source_deposit_number='', destination_card_number='', sequence_number='',
                          reference_number='', source_note='', destination_note='', **kwargs):
        """
        گزارش کارت به کارت

        :param str source_card_number: شماره کارت مبدا
        :param int min_amount: از مبلغ
        :param int max_amount: تا مبلغ
        :param str start_date: از تاریخ به فرمت yyyy/mm/dd و به صورت میلادی
        :param str end_date: تا تاریخ به فرمت yyyy/mm/dd و به صورت میلادی
        :param str source_deposit_number: شماره سپرده مبدا
        :param str destination_card_number: شماره کارت مقصد
        :param str sequence_number:
        :param str reference_number: شماره پیگیری
        :param str source_note: توضیحات مبدا
        :param str destination_note: توضیحات مقصد
        :return: list
        """

        params = {
            "SourceCardNumber": source_card_number,
            "SourceDepositNumber": source_deposit_number,
            "DestinationCardNumber": destination_card_number,
            "MinAmount": min_amount,
            "MaxAmount": max_amount,
            "StartDate": start_date,
            "EndDate": end_date,
            "RefrenceNumber": reference_number,
            "SequenceNumber": sequence_number,
            "SourceNote": source_note,
            "DestinationNote": destination_note,
        }

        params = self.__prepare_params(method_name="card_to_card_list", **params)

        self._validate(params, "cardToCardList")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getcardToCardList"), params=params,
            headers=self._get_headers(), **kwargs), method="GetCardToCardTransferReport")

    def get_submission_cheque(self, deposit, min_amount=None, max_amount=None, start_date=None, end_date=None,
                              start_submission_date=None, end_submission_date=None, cheque_number="", row_count=10,
                              bank_code=-1, cheque_status=0, **kwargs):
        """
        استعلام چک های واگذار شده

        :param str deposit: شماره سپرده
        :param str cheque_number: شماره چک
        :param int row_count: تعداد ردیف خروجی
        :param int min_amount: از مبلغ
        :param int max_amount: تا مبلغ
        :param str start_date: از تاریخ به فرمت yyyy/mm/dd و به صورت میلادی
        :param str end_date: تا تاریخ به فرمت yyyy/mm/dd و به صورت میلادی
        :param int bank_code: کد بانک
        :param int cheque_status: وضعیت چک
        :param str start_submission_date: تاریخ واگذاری از به فرمت yyyy/mm/dd و به صورت میلادی
        :param str end_submission_date: تاریخ واگذاری تا به فرمت yyyy/mm/dd و به صورت میلادی
        :return: list
        """

        params = {
            "Deposit": deposit,
            "ChequeNumber": cheque_number,
            "MinAmount": min_amount,
            "MaxAmount": max_amount,
            "StartDate": start_date,
            "EndDate": end_date,
            "BankCode": bank_code,
            "ChequeStatus": cheque_status,
            "StartSubmisionDate": start_submission_date,
            "EndSubmissionDate": end_submission_date,
            "RowCount": row_count
        }

        params = self.__prepare_params(method_name="get_submission_cheque", **params)

        for value in params.keys():
            if params[value] is None:
                params[value] = ""

        validated_params = {
            k: v
            for k, v in params.items()
            if v is not None and v != ""
        }

        self._validate(validated_params, "getSubmissionCheque")
        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getSubmissionCheque"), params=params,
            headers=self._get_headers(), **kwargs), method="GetsubmissionCheque")

    def convert_deposit_number_to_sheba(self, deposit_number, **kwargs):
        """
        تبدیل شماره حساب به شبا

        :param str deposit_number: شماره سپرده
        :return: str
        """

        params = {
            "DepositNumber": deposit_number
        }

        params = self.__prepare_params(method_name="convert_deposit_number_to_sheba", **params)

        self._validate(params, "convertDepositNumberToSheba")
        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getConvertDepositNumberToSheba"), params=params,
            headers=self._get_headers(), **kwargs), method="ConvertDepositNumberToSheba")

    def convert_sheba_to_deposit_number(self, sheba, **kwargs):
        """
        تبدیل شماره شبا به شماره سپرده

        :param str sheba: شماره شبا
        :return: str
        """

        params = {
            "Sheba": sheba
        }

        params = self.__prepare_params(method_name="convert_sheba_to_deposit_number", **params)

        self._validate(params, "convertShebaToDepositNumber")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getConvertShebaToDepositNumber"), params=params,
            headers=self._get_headers(), **kwargs), method="ConvertShebaToDepositNumber")

    def paya_service(self, source_deposit_number, batch_paya_item_infos, file_unique_identifier=None,
                     transfer_money_bill_number="", **kwargs):
        """
        تبدیل شماره شبا به شماره سپرده

        :param str source_deposit_number: شماره سپرده مبدا
        :param list batch_paya_item_infos: لیست اطلاعات شباهای مقصد
        :param str file_unique_identifier: شناسه یکتای فایل که حتما باید با ACH شروع و ترکیبی از عدد و حروف باشد
        در صورتی که این مقدار را ارسال نکنید به صورت خودکار پر می شود
        :param str transfer_money_bill_number: در صورتیکه سپرده مبدا دارای شناسه قبض است باید این فیلد ارسال شود.
        :return: str
        """
        if file_unique_identifier is None:
            file_unique_identifier = self.__generate_file_unique_identifier()

        params = {
            "SourceDepositNumber": source_deposit_number,
            "FileUniqueIdentifier": file_unique_identifier,
            "TransferMoneyBillNumber": transfer_money_bill_number,
            "BatchPayaItemInfos": batch_paya_item_infos
        }

        validated_params = params.copy()
        params = self.__prepare_params(method_name="paya_service", **params)
        params["BatchPayaItemInfos"] = json.dumps(params["BatchPayaItemInfos"], separators=(',', ':'), ensure_ascii=False)
        validated_params = self.__prepare_params(**validated_params)

        self._validate(validated_params, "payaService")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/payaService", method_type="post"), params=params,
            headers=self._get_headers(), **kwargs), method="CoreBatchTransferPaya")

    def get_deposit_invoice(self, start_date, end_date, deposit_number="", sheba="", count=10, first_index=0, **kwargs):
        """
        دریافت صورتحساب سپرده

        :param str start_date: تاریخ شروع به فرمت yyyy/mm/dd و به صورت میلادی
        :param str end_date: تاریخ پایان به فرمت yyyy/mm/dd و به صورت میلادی
        :param str deposit_number: شماره سپرده
        :param str sheba: شماره شبا
        :param int count: تعداد خروجی
        :param int first_index: شماره اولین خروجی
        :return: list
        """

        params = {
            "DepositNumber": deposit_number,
            "Sheba": sheba,
            "StartDate": start_date+" 00:00:00:000",
            "EndDate": end_date+" 23:59:59:999",
            "FirstIndex": first_index,
            "Count": count,
        }

        if params["Sheba"] == "":
            del params["Sheba"]
        else:
            del params["DepositNumber"]
        params = self.__prepare_params(method_name="get_deposit_invoice", **params)
        validated_params = params.copy()
        validated_params["StartDate"] = start_date
        validated_params["EndDate"] = end_date

        self._validate(validated_params, "getDepositInvoice")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getDepositInvoice"), params=params,
            headers=self._get_headers(), **kwargs), method="GetDepositInvoice")

    def get_deposit_balance(self, deposit_number="", sheba="", **kwargs):
        """
        دریافت موجودی سپرده

        :param str deposit_number: شماره سپرده
        :param str sheba: شماره شبا
        :return: dict
        """

        params = {
            "DepositNumber": deposit_number,
            "Sheba": sheba
        }

        if params["Sheba"] == "":
            del params["Sheba"]
        else:
            del params["DepositNumber"]

        params = self.__prepare_params(method_name="get_deposit_balance", **params)
        validated_params = params.copy()

        self._validate(validated_params, "getDepositBalance")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getDepositBalance"), params=params,
            headers=self._get_headers(), **kwargs), method="GetDepositBalance")

    def transfer_money(self, amount, payment_id, source_deposit_number="", source_sheba="",
                       destination_deposit_number="", destination_sheba="", destination_first_name="",
                       destination_last_name="", source_comment="", destination_comment="", **kwargs):
        """
        انتقال وجه داخلی پایا

        :param int amount: مبلغ
        :param str payment_id: شناسه پرداخت
        :param str source_deposit_number: شماره حساب مبدا
        :param str source_sheba: شماره شبا مبدا
        :param str destination_deposit_number: شماره سپرده مقصد
        :param str destination_sheba: شماره شبا مقصد
        :param str destination_first_name: نام صاحب حساب مقصد
        :param str destination_last_name: نام خانوادگی حساب مقصد
        :param str source_comment: توضیحات مبدا
        :param str destination_comment: توضیحات مقصد
        :return: str
        """

        params = {
            "SourceDepositNumber": source_deposit_number,
            "SourceSheba": source_sheba,
            "DestDepositNumber": destination_deposit_number,
            "DestSheba": destination_sheba,
            "DestFirstName": destination_first_name,
            "DestLastName": destination_last_name,
            "Amount": amount,
            "SourceComment": source_comment,
            "DestComment": destination_comment,
            "PaymentId": payment_id
        }

        params = self.__prepare_params(method_name="transfer_money", **params)
        self._validate(params, "transferMoney")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/transferMoney", method_type="post"), params=params,
            headers=self._get_headers(), **kwargs), method="TransferMoney")

    def get_transfer_state(self, payment_id, date, **kwargs):
        """
        انتقال وجه داخلی پایا

        :param str payment_id: شناسه پرداخت درج شده در درخواست انتقال وجه
        :param str date: تاریخ انتقال به فرمت yyyy/mm/dd و به صورت میلادی
        :return: dict
        """

        params = {
            "Date": date,
            "PaymentId": payment_id
        }

        params = self.__prepare_params(method_name="get_transfer_state", **params)
        self._validate(params, "getTransferState")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getTransferState"), params=params,
            headers=self._get_headers(), **kwargs), method="GetTransferMoneyState")

    def bill_payment_by_deposit(self, deposit_number, bill_number, payment_id, **kwargs):
        """
        پرداخت قبض از طریق سپرده

        :param str deposit_number: شماره سپرده
        :param str bill_number: شناسه قبض
        :param str payment_id: شناسه پرداخت
        :return: str
        """

        params = {
            "PaymentId": payment_id,
            "DepositNumber": deposit_number,
            "BillNumber": bill_number,
        }

        params = self.__prepare_params(method_name="bill_payment_by_deposit", **params)
        self._validate(params, "billPaymentByDeposit")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/billPaymentByDeposit", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs), method="BillPaymentByDeposit")

    def get_card_information_by_card_info(self, source_card_number, destination_card_number, cvv2, expire_month,
                                          expire_year, pin2, **kwargs):
        """
        استعلام اطلاعات کارت و شناسه ارجاع برای کارت به کارت

        :param str source_card_number: کارت مبدا
        :param str destination_card_number: کارت مقصد
        :param str cvv2: کد cvv2 کارت مبدا
        :param str expire_month: ماه انقضا کارت مبدا
        :param str expire_year: سال انقضا کارت مبدا
        :param str pin2: رمز دوم / پویا کارت مبدا
        :return: str
        """
        params = {
            "SrcCardNumber": source_card_number,
            "DestCardNumber": destination_card_number,
            "Cvv2": cvv2,
            "ExpireMonth": expire_month,
            "ExpireYear": expire_year,
            "Pin2": pin2
        }

        params = self.__prepare_params(method_name="get_card_information_by_card_info", **params)
        self._validate(params, "getCardInformationByCardInfo")

        return self.__parse_response(self._request.call(
            super(PodBanking, self)._get_sc_product_settings("/getCardInformationByCardInfo"), params=params,
            headers=self._get_headers(), **kwargs), method="GetCardInformationByCardInfo")

    @staticmethod
    def __generate_file_unique_identifier():
        return "ACH{}".format(datetime.now().__format__("%s%f"))

    def __prepare_params(self, method_name=None, **kwargs):
        kwargs = self.__remove_empty_items(**kwargs)

        params = {"UserName": kwargs.pop("UserName", self.__user_name)}
        if "Sheba" in kwargs:
            kwargs["Sheba"] = "IR" + kwargs["Sheba"][-24:]

        params.update(kwargs)
        params["Timestamp"] = self.__get_timestamp()
        params_for_sign = self.__convert_params_to_string(**params)
        params["signature"] = self.__sign(method_name=method_name, **params_for_sign)
        return params

    @staticmethod
    def __remove_empty_items(**kwargs):
        return {key: value for key, value in kwargs.items() if value is not None and value != "" and value != {}}

    def __convert_params_to_string(self, **kwargs):
        output = {}
        for key, value in kwargs.items():
            if type(value) is not list:
                output[key] = self.__convert_to_string(value)
            else:
                output[key] = value

        return output

    @staticmethod
    def __convert_to_string(value):
        if version_info[0] == 2:
            return unicode(value)

        return str(value)

    @staticmethod
    def __get_timestamp():
        return datetime.now().__format__("%Y/%m/%d %H:%M:%S:123")

    def __sign(self, method_name=None, **params):
        if not self.__private_key:
            raise PodException("Please set Private key path")

        params = self.__get_data_for_sign(method_name=method_name, **params)
        data = json.dumps(params, separators=(',', ':'), ensure_ascii=False)
        return self.__sign_string(data, self.__private_key)

    @staticmethod
    def __sign_string(data, private_key):
        """
        امضا رشته

        :param str data: رشته
        :param private_key: کلید خصوصی
        :return: str
        """
        digest = SHA.new()
        digest.update(data.encode("utf-8"))

        signer = PKCS1_v1_5.new(private_key)
        sig = signer.sign(digest)
        if version_info[0] == 2:
            return str(base64.b64encode(sig))

        return str(base64.b64encode(sig), "utf-8")

    def __parse_response(self, result, method):
        if "statusCode" not in result:
            raise HTTPException(message="خطا در برقراری ارتباط با سرور", error_code=889, raw_result=result)

        if result["statusCode"] >= 300 or result["statusCode"] < 200:
            raise APIException(message=result["result"], error_code=889, raw_result=result)

        xml = xmltodict.parse(result["result"])

        body = xml["soap:Envelope"]["soap:Body"]

        if method + "Response" not in body:
            raise APIException(message="اطلاعات دریافتی از سرور نامعتبر است")

        response = body[method + "Response"]
        if method + "Result" not in response:
            raise APIException(message="اطلاعات دریافتی از سرور نامعتبر است")
        result = response[method + "Result"]
        result = json.loads(result)
        self.__raw_result = result
        if not result["IsSuccess"]:
            raise APIException(message=result["Message"], error_code=result["MessageCode"],
                               reference_number=self._request._reference_number)

        return result["Data"]

    def last_raw_result(self):
        """
        دریافت خروجی خام آخرین سرویس

        :return: dict
        """
        return self.__raw_result

    @staticmethod
    def __get_data_for_sign(method_name=None, **kwargs):
        if version_info[0] >= 3:
            return kwargs

        data = {
            "get_sheba_info_and_status": DataOrdered.get_sheba_info_and_status(),
            "get_deposit_number_by_card_number": DataOrdered.get_deposit_number_by_card_number(),
            "get_sheba_by_card_number": DataOrdered.get_sheba_by_card_number(),
            "get_card_information": DataOrdered.get_card_information(),
            "card_to_card": DataOrdered.card_to_card(),
            "card_to_card_list": DataOrdered.card_to_card_list(),
            "get_submission_cheque": DataOrdered.get_submission_cheque(),
            "convert_deposit_number_to_sheba": DataOrdered.convert_deposit_number_to_sheba(),
            "convert_sheba_to_deposit_number": DataOrdered.convert_sheba_to_deposit_number(),
            "paya_service": DataOrdered.paya_service(),
            "get_deposit_invoice": DataOrdered.get_deposit_invoice(),
            "get_deposit_balance": DataOrdered.get_deposit_balance(),
            "transfer_money": DataOrdered.transfer_money(),
            "get_transfer_state": DataOrdered.get_transfer_state(),
            "bill_payment_by_deposit": DataOrdered.bill_payment_by_deposit(),
            "get_card_information_by_card_info": DataOrdered.get_card_information_by_card_info()
        }

        data_ordered = data.get(method_name, None)

        if data_ordered is None:
            return kwargs

        data_ordered.update(kwargs)
        output = OrderedDict()
        for key, value in data_ordered.items():
            if value is not None and value != "" and value != {}:
                output[key] = value

        return output
