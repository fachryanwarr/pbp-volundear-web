from email.policy import default
from multiprocessing import dummy
from statistics import mode
from django.db import models
from authentication.models import User
from daftarwilayah.models import Wilayah

# Create your models here.


class DaftarRelawan(models.Model):
    Wilayah = models.ForeignKey(Wilayah, on_delete=models.CASCADE,null=True)
    Relawan = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    keahlian = models.CharField(max_length=50)
    mulai_periode = models.DateTimeField()
    akhir_periode = models.DateTimeField()
