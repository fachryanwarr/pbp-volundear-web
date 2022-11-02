from django.db import models

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Feedback(models.Model):
    nama = models.TextField(blank=False, null=True)
    pesan_feedback = models.TextField(blank=False, null=True)




# Create your models here.
