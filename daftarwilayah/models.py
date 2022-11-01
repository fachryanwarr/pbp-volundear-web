from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from authentication.models import VolundearUser

class Wilayah(models.Model):
    user = models.ForeignKey(VolundearUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    kota = models.CharField(max_length=20)
    kebutuhan = models.TextField(default="")
    address = models.TextField()
    kuota_max = models.IntegerField()
    kuota_terisi = models.IntegerField(default = 0)
    description = models.TextField()
    jangka_waktu = models.CharField(max_length=30, default="")
