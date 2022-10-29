from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artikel/', include('artikel.urls')),
    path('', include('daftarwilayah.urls')),
    path('daftarrelawan/', include('daftarrelawan.urls')),
]
