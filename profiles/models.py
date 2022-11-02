from django.db import models
from authentication.models import User

class DetailedUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default="-")
    phone_number = models.IntegerField(default="")
    pekerjaan = models.CharField(max_length=30, default="")
    alamat = models.TextField(default="")
    tanggal_lahir = models.CharField(max_length=30, default="-")