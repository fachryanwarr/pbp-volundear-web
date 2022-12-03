from django.urls import path
from profiles.views import show_profile, profile_relawan, show_edit, edit, get_detail, profile_PJ

app_name = "profiles"

urlpatterns = [
    path("", show_profile, name='show_profile'),
    path("show_edit/", show_edit, name="show_edit"),
    path("profile_relawan/", profile_relawan, name='profile_relawan'),
    path("profile_PJ/", profile_PJ, name='profile_PJ'),
    path("edit/", edit, name="edit"),
    path("get_detail/", get_detail, name='get_detail'),
]