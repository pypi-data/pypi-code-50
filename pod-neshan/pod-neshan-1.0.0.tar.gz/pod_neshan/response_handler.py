# coding=utf-8
import json

from pod_base import APIException


def parse_response(request, reference_number):
    print(request.original_result)
    __raw_result = request.original_result

    if "statusCode" not in __raw_result:
        raise APIException(message="اطلاعات دریافتی از سرور نامعتبر است", error_code=887,
                           reference_number=reference_number)

    if 300 > __raw_result["statusCode"] >= 200:
        try:
            return json.loads(__raw_result["result"])
        except ValueError as e:
            raise APIException(message=__raw_result["result"], error_code=887,
                               reference_number=reference_number)

    raise APIException(
        message="خطای غیرمنتظره ایی رخ داده است (status code {})".format(__raw_result["statusCode"]),
        error_code=887, reference_number=reference_number)
