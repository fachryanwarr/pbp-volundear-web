from django.urls import path
from profiles.views import show_profile

urlpatterns = [
    path("", show_profile, name='show_profile'),
    
]