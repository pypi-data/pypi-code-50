from django.urls import include, path
from rest_framework import routers
from .edition.viewset import EditionViewset

app_name = "api"

router = routers.DefaultRouter()
router.register(r"edition", EditionViewset, base_name="edition")

urlpatterns = [path("", include(router.urls))]
