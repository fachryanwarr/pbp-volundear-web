from django.urls import path
from profiles.views import show_profile, profile_relawan

app_name = "profiles"

urlpatterns = [
    path("", show_profile, name='show_profile'),
    path("profile_relawan", profile_relawan, name='profile_relawan'),
    
]