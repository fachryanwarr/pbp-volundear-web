from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DaftarRelawan(models.Model):
    keahlian = models.CharField(max_length=50)
    tanggal = models.DateTimeField()
    jam = models.TimeField()
