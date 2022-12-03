from email.policy import default
from statistics import mode
from django.db import models
from authentication.models import User
from daftarwilayah.models import Wilayah

class Pendaftaran(models.Model):
    wilayah = models.ForeignKey(Wilayah, on_delete=models.CASCADE,null=True)
    relawan = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    keahlian = models.CharField(max_length=50)
    mulai_periode = models.DateTimeField()
    akhir_periode = models.DateTimeField()
