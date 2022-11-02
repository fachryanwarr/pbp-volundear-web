from django.contrib import admin
from django.urls import path, include
from landingpage.views import show_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artikel/', include('artikel.urls')),
    path('daftarrelawan/', include('daftarrelawan.urls')),
    path('daftarwilayah/', include('daftarwilayah.urls')),
    path('donasi/', include('donasi.urls')),
    path('auth/', include('authentication.urls')),
    path('', include('landingpage.urls')),
    path('profile/', include('profiles.urls')),
]
