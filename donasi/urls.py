from django.urls import path
from donasi.views import *

app_name = 'donasi'

urlpatterns = [
    path('', show_donasi, name='show_donasi'),
    path('json/', show_json, name='show_json'),
    path('add/', create_donasi_ajax, name='create_donasi_ajax'),
]