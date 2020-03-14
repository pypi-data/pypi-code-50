from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="indexHome"),
    path('saveme', views.sendData, name='saveme'),
    path('delete', views.deleteData, name='deleteme')
]