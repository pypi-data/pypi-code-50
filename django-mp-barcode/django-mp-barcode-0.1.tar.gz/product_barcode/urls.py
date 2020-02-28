
from django.urls import path

from product_barcode import views


app_name = 'barcode'


urlpatterns = [

    path('<int:code>/', views.get_code, name='get'),

    path('print/', views.print_codes, name='print')

]
