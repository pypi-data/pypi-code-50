from datetime import datetime, timedelta
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable, PermissionDenied

from .mixins import CredentialMixin

__all__ = ('LimitOffsetPaginationListAPIView',)


class StandardResultsPagination(LimitOffsetPagination):
    default_limit = 1000
    max_limit = 1000


class LimitOffsetPaginationListAPIView(CredentialMixin, ListAPIView):
    """
    limit=1000
    offset=1000
    for calculation:
        rewrite get_calculation method -> dict
    for dynamic fields:
        (Need DynamicFieldSerializer)
        rewrite get_fields  method -> list
    you always have:
    self.integration_id
    self.date_form
    self.date_to
    """
    limit = None
    offset = None
    pagination_class = StandardResultsPagination

    def _ensure_limit_offset_params(self):
        if self.limit and self.offset:
            self.pagination_class.limit = limit
            self.pagination_class.offset = offset

    def _generate_date_params(self, delta: int) -> tuple:
        date_to = datetime.today().strftime('%Y-%m-%d')
        date_from = (datetime.today() - timedelta(days=delta)).strftime('%Y-%m-%d')
        return date_from, date_to

    def _get_params(self):
        admin = self.get_check_admin(self.request)
        if not admin:
            raise PermissionDenied({"status": "error", "message": "this method for admin"})

        self._ensure_limit_offset_params()
        self.integration_id = self.request.GET.get("integration_id")
        last_week = self.request.GET.get("last_week", "")
        last_3_days = self.request.GET.get("last_3_days", "")
        date_from = self.request.GET.get("date_from", "")
        date_to = self.request.GET.get("date_to", "")

        if not self.integration_id:
            raise NotAcceptable({"status": "error", "message": "miss integration_id"})

        if last_week == "true":
            date_from, date_to = self._generate_date_params(7)
        elif last_3_days == "true":
            date_from, date_to = self._generate_date_params(3)

        if not date_from and not date_to:
            raise NotAcceptable({"status": "error", "message": "miss date params"})
        self.date_from = date_from
        self.date_to = date_to

    def get_calculation(self) -> dict:
        return {}

    def get_fields(self) -> list:
        return []

    def list(self, request, format=None):
        self._get_params()
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={"calculation": self.get_calculation(),
                                                                       "response_fields": self.get_fields()})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(
            queryset,
            many=True,
            context={"calculation": self.get_calculation(), "response_fields": self.get_fields()}
        )

        return Response(serializer.data)
