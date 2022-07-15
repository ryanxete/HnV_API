from django.db import models

# Create your models here.
class SuperType(models.Model):
    hero = models.CharField(max_length=100)
    villain = models.CharField(max_length=100)