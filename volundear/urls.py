from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('daftarwilayah/', include('daftarwilayah.urls')),
    path('', include('home.urls')),
    path('artikel/', include('artikel.urls')),
    path('donasi/', include('donasi.urls')),
    path('profile/', include('profile.urls')),
    path('relawan/', include('daftarrelawan.urls')),
]
