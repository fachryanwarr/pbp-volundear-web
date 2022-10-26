from django.urls import path
from daftarwilayah.views import get_wilayah, show_wilayah

app_name = 'daftarwilayah'

urlpatterns = [
    path("", show_wilayah, name='show_wilayah'),
    path("json", get_wilayah, name='get_wilayah'),
]
