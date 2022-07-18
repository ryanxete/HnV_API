from django.db import models
from supers.models import Super

# Create your models here.
class SuperType(models.Model):
    type = models.CharField(max_length=100)
    super = models.ForeignKey(Super, on_delete=models.CASCADE, null=True)