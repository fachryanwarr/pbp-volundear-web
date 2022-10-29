from django.urls import path
from .views import *

appname = 'daftarrelawan'

urlpatterns = [
    path('', daftar_relawan, name='show_relawan'),
    ]
