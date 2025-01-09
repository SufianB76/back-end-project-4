from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    directions = models.TextField()
    cooktime = models.CharField(max_length=25)
    