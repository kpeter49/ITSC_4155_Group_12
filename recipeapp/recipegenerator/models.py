from django.db import models
import uuid

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
    
class Ingredient(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    calories = models.IntegerField()

    class Meta:
        verbose_name_plural = "ingredients"

    def __str__(self):
        return self.name
    
class Restriction(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4().hex[:5].upper())
    ingredientId = models.IntegerField()
    userName = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Restrictions"

    def __str__(self):
        return self.id
    
class RestrictionPreset(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "RestrictionPresets"

    def __str__(self):
        return self.name
    
class SelectedRestrictionPreset(models.Model):
    id = models.IntegerField(primary_key=True)
    presetid = models.IntegerField()
    userName = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "SelectedRestrictionPresets"

    def __str__(self):
        return self.name
    
class RestrictionPresetIngredient(models.Model):
    id = models.IntegerField(primary_key=True)
    presetid = models.IntegerField()
    ingredientId = models.IntegerField()

    class Meta:
        verbose_name_plural = "RestrictionPresetIngredients"

    def __str__(self):
        return self.name