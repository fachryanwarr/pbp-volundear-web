from django.urls import path
from landingpage.views import show_landingpage

app_name = 'landingpage'

urlpatterns = [
    path('', show_landingpage, name='show_landingpage'),
]