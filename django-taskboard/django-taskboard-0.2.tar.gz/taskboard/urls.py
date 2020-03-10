from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('performance/<component>/', views.performance, name='performance'),
    path('system/<component>/', views.system, name='system'),
    path('performance/cpu/<metric>/', views.cpu, name='cpu'),
    path('performance/memory/<metric>/', views.memory, name='memory'),
    path('performance/disk/<metric>/', views.disk, name='disk'),
    path('performance/disk/<metric>/<device>/', views.disk, name='disk-usage'),
    path('performance/network/<metric>/', views.network, name='network'),
    path('system/processes/<metric>/', views.processes, name='system'),
    path('system/processes/<metric>/<int:pid>', views.processes, name='system-pid'),
    path('system/services/<metric>/', views.services, name='services'),
]
