from django.db import models

# Create your models here.

class Coder(models.Model):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
