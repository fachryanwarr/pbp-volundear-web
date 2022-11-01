from django.urls import path
from landingpage.views import show_landingpage, get_faq

app_name = 'landingpage'

urlpatterns = [
    path('', show_landingpage, name='show_landingpage'),
    path('json/', get_faq, name='get_faq')
]