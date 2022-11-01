from django.db import models
from authentication.models import VolundearUser

class Artikel(models.Model):
    penulis = models.ForeignKey(VolundearUser, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100)
    rilis = models.DateField(auto_now_add=True)
    pembuka = models.TextField(default=None) 
    isi = models.TextField()

    class Meta:
        ordering = ['-pk']

class Komentar(models.Model):
    artikel = models.ForeignKey(Artikel,related_name="comments", on_delete=models.CASCADE)
    penulis = models.ForeignKey(VolundearUser, on_delete=models.CASCADE)
    waktu = models.DateField(auto_now_add=True)
    deskripsi = models.TextField()

    class Meta:
        ordering = ['-pk']