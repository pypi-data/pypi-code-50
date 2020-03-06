from django.urls import include, path, register_converter

from . import views

app_name = "getpaid_paynow"

urlpatterns = [
    path("callback/", views.CallbackView.as_view(), name="callback",),
]
