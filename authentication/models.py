from django.db import models
from django.contrib.auth.models import AbstractUser

class VolundearUser(AbstractUser):
    is_relawan = False
    is_PJ = False
    

