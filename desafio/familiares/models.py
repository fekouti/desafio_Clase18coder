from django.db import models

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthday = models.CharField(max_length=10)

