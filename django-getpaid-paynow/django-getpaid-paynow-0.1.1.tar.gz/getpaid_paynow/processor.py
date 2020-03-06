""""
Settings:
    api_key
    signature_key
"""
import base64
import hashlib
import hmac
import json

import requests
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
from getpaid import PaymentStatus
from getpaid.processor import BaseProcessor


class PaymentProcessor(BaseProcessor):
    slug = "paynow"
    display_name = "mBank payNow"
    accepted_currencies = [
        "PLN",
    ]
    method = "REST"
    sandbox_url = "https://api.sandbox.paynow.pl/v1/"
    production_url = "https://api.paynow.pl/v1/"

    @classmethod
    def calc_signature(cls, obj: str, key: str) -> str:
        hashed_obj = hmac.new(key.encode(), obj.encode(), hashlib.sha256).digest()
        return base64.b64encode(hashed_obj)

    def handle_callback(self, request, *args, **kwargs):
        received_signature = request.headers.get("Signature")
        content = request.data
        key = self.get_setting("signature_key")
        signature = self.calc_signature(content, key)
        if received_signature == signature:
            payload = json.loads(request.data)
            status = payload["status"]
            if status == "CONFIRMED":
                self.payment.on_success()
            elif payload["status"] in ["REJECTED", "ERROR"]:
                self.payment.on_failure()
            else:
                self.payment.change_status(PaymentStatus.IN_PROGRESS)

        return HttpResponse("OK")

    def handle_response(self, response) -> dict:
        data = response.json()
        self.payment.external_id = data["paymentId"]
        self.payment.change_status(PaymentStatus.IN_PROGRESS)
        return dict(
            external_id=data["paymentId"],
            url=data["redirectUrl"],
            status=data["status"],
        )

    def get_redirect_params(self):
        data = self.payment.order.get_user_info()
        buyer = dict(
            email=data.get("email"),
            firstName=data.get("first_name", None),
            lastName=data.get("last_name", None),
        )
        return json.dumps(
            dict(
                amount=int(self.payment.amount * 10),
                currency=self.payment.currency,
                externalId=self.payment.pk,
                description=self.payment.description,
                continueUrl=reverse(
                    "getpaid:payment-success", kwargs=dict(pk=self.payment.pk)
                ),
                buyer=dict([(k, v) for k, v in buyer.items() if v]),
            )
        )

    def get_redirect_url(self, params=None):
        if params is None:
            return "{}payments".format(super().get_redirect_url())
        return params["redirectUrl"]

    def fetch_status(self):
        if settings.DEBUG:
            api_url = self.sandbox_url
        else:
            api_url = self.production_url
        url = "{api_url}payments/{id}/status".format(
            api_url=api_url, id=self.payment.external_id
        )
        headers = {"Api-Key": self.get_setting("api_key")}
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            status = result.json().get("status")
            if status == "CONFIRMED":
                return {"status": PaymentStatus.PAID}
            elif status in ["REJECTED", "ERROR"]:
                return {"status": PaymentStatus.FAILED}
            return {"status": PaymentStatus.IN_PROGRESS}
