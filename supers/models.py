from django.db import models

# Create your models here.
class Super:
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=100)
    secondry_primary = models.CharField(max_length=100)
    catchphrase = models.CharField(max_length=100)
    super_type = ForeignKey