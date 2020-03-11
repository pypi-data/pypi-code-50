# coding=utf-8

from pod_base import APIException


def response_handler(result, reference_number):
    if "hasError" not in result:
        raise APIException(message="اطلاعات دریافتی از سرور نامعتبر است", error_code=887,
                           reference_number=reference_number)

    if result["hasError"]:
        result.setdefault("status", result.get("data", "خطایی رخ داده است"))

        result.setdefault("statusCode", 500)
        raise APIException(message=result["status"], error_code=result["statusCode"],
                           reference_number=reference_number)

    if "data" in result:
        return result["data"]
    elif "result" in result:
        return result["result"]

    return result
