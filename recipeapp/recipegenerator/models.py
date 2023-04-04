from django.db import models
import uuid
import json

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
    
    def get_ingredients(self):
        return json.loads(self.ingredients)
    
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
    
    def get_calories_per_gram(self):
        return self.calories / self.amount
    
    def get_protein_per_gram(self):
        return self.protein / self.amount
    
    def get_fat_per_gram(self):
        return self.fat / self.amount
    
    def get_carbs_per_gram(self):
        return self.carbs / self.amount
    
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