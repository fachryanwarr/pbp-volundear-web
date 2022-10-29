from django.db import models
from django.contrib.auth.models import User

class Artikel(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100)
    rilis = models.DateField(auto_now_add=True)
    pembuka = models.TextField(default=None) 
    isi = models.TextField()

    class Meta:
        ordering = ['-pk']