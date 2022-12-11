from django.urls import path
from authentication.views import register, register_PJ, register_relawan, login_user, logout_user, login_flutter

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('register-relawan/', register_relawan, name='register-relawan'),
    path('register-PJ/', register_PJ, name='register-PJ'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login-flutter/', login_flutter, name='login_flutter'),
]
