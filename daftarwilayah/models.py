from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Wilayah(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    kota = models.CharField(max_length=20)
    kebutuhan = models.TextField(default="")
    address = models.TextField()
    kuota_max = models.IntegerField()
    kuota_terisi = models.IntegerField(default = 0)
    description = models.TextField()
    jangka_waktu = models.CharField(max_length=30, default="")
