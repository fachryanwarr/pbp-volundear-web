from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_relawan = models.BooleanField(default = False)
    is_PJ = models.BooleanField(default = False)
    

