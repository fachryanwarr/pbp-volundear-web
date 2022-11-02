from email.policy import default
from multiprocessing import dummy
from statistics import mode
from django.db import models
from authentication.models import User
import datetime

class Wilayah(models.Model):
    pj = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    kota = models.CharField(max_length=20)
    kebutuhan = models.TextField(default="")
    address = models.TextField()
    kuota_max = models.IntegerField()
    kuota_terisi = models.IntegerField(default = 0)
    description = models.TextField()
    awalPeriode = models.CharField(max_length=30)
    akhirPeriode = models.CharField(max_length=30)
