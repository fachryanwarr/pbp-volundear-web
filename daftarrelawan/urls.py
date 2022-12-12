from django.urls import path
from .views import *

appname = 'daftarrelawan'

urlpatterns = [
    path('<int:id>', daftar_relawan, name='daftar_relawan'),
    path('make_data/', make_data, name='make_data'),
    path('json/', get_pendaftaran, name="get_pendaftaran"),
    path('daftar_flutter', daftar_relawan_from_flutter, name="daftar_flutter"),
    ]
