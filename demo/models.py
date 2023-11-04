from django.db import models

# Create your models here.


class shoes(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    description = models.CharField(max_length=255) 
    price = models.FloatField(null = True)
    color = models.CharField(max_length=10)
