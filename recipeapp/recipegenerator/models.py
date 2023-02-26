from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=600)
    proteinLevel = models.CharField(max_length=255)
    fatLevel = models.CharField(max_length=255)

    class Meta:
          verbose_name_plural = "recipies"

    def __str__(self):
        return self.name