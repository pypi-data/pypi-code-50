import requests
from django.conf import settings

REQUEST_TIMEOUT = getattr(settings, "OFFLINE_REQUEST_TIMEOUT", 300)


class OfflineCollect():
    def _headers(self):
        return {"Authorization": f"Token {settings.ETOOLS_OFFLINE_TOKEN}"}

    def _url(self):
        return settings.ETOOLS_OFFLINE_API

    def _url_detail(self, code):
        return f"{self._url()}{code}/"

    def get(self, code):
        """Get form by code"""
        response = requests.get(
            self._url_detail(code),
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT,
        )
        return response.status_code, response.json()

    def list(self):
        """Get list of forms"""
        response = requests.get(
            self._url(),
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT,
        )
        return response.status_code, response.json()

    def add(self, data):
        """Add form"""
        response = requests.post(
            self._url(),
            data=data,
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT,
        )
        return response.status_code, response.json()

    def update(self, code, accessible_by=None, expiry_date=None):
        """Update form, limited to specific fields"""
        data = {}
        if accessible_by:
            data["accessible_by"] = accessible_by
        if expiry_date:
            data["expiry_date"] = expiry_date
        if not data:
            return 400, {"message": "No data provided."}
        response = requests.patch(
            self._url_detail(code),
            data=data,
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT,
        )
        return response.status_code, response.json()

    def delete(self, code):
        """Add form"""
        response = requests.delete(
            self._url_detail(code),
            headers=self._headers(),
            timeout=REQUEST_TIMEOUT,
        )
        return response.status_code, response.json()
