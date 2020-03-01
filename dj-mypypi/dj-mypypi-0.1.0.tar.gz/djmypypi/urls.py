# -*- coding: utf-8 -*-
from django.urls import path

from . import views


app_name = 'djmypypi'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('@upload/', views.upload_package, name='upload-package'),
    path('@download/<package_name>', views.download_package, name='download-package'),
    path('<package_name>/', views.PackageView.as_view(), name='package'),
]
