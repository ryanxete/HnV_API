from django.db import models

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=300)
    alter_ego = models.CharField(max_length=300)
    primary_ability = models.CharField(max_length=300)
    secondry_primary = models.CharField(max_length=300)
    catchphrase = models.CharField(max_length=300)
    # super_type = ForeignKey
