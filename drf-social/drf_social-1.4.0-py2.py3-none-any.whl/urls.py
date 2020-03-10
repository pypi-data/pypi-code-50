from django.urls import path
from drf_social.view import SocialLoginView

urlpatterns = [
    path('social/login', SocialLoginView.as_view())
]