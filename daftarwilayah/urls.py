from django.urls import path
from daftarwilayah.views import get_wilayah, show_wilayah, add_wilayah, get_wilayah_detail, get_daftar_kota

app_name = 'daftarwilayah'

urlpatterns = [
    path("", show_wilayah, name='show_wilayah'),
    path("json", get_wilayah, name='get_wilayah'),
    path("add_new/", add_wilayah, name='add_new'),
    path('get-detail/<int:id>', get_wilayah_detail, name='get-wilayah'),
    path('get-daftar-kota/', get_daftar_kota, name='daftar-kota'),
]
