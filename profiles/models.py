from django.db import models
from authentication.models import User

class DetailedUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone_number = models.IntegerField()