from django import http
from django.urls import path

from django_early_return import EarlyReturn

def raise_forbidden(request):
    raise EarlyReturn(http.HttpResponseForbidden('access denied'))

urlpatterns = [
    path('raise_forbidden/', raise_forbidden),
]