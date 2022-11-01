from django.db import models

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Feedback(models.Model):
    nama = models.TextField()
    feedback = models.TextField()




# Create your models here.
