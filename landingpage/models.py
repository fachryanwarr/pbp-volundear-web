from django.db import models

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()


# Create your models here.
