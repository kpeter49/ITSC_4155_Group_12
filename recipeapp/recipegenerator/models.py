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
    id = models.AutoField(primary_key=True)
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
    
class Recipes(models.Model):
    id = models.IntegerField(blank=True, null=True)
    recipename = models.TextField(db_column='RecipeName', blank=True, null=True)  # Field name made lowercase.
    preptime = models.TextField(db_column='PrepTime', blank=True, null=True)  # Field name made lowercase.
    cooktime = models.TextField(db_column='CookTime', blank=True, null=True)  # Field name made lowercase.
    totaltime = models.TextField(db_column='TotalTime', blank=True, null=True)  # Field name made lowercase.
    servings = models.IntegerField(db_column='Servings', blank=True, null=True)  # Field name made lowercase.
    yeild = models.TextField(db_column='Yeild', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.TextField(db_column='Ingredients', blank=True, null=True)  # Field name made lowercase.
    directions = models.TextField(db_column='Directions', blank=True, null=True)  # Field name made lowercase.
    rating = models.FloatField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase.
    cuisinetype = models.TextField(db_column='CuisineType', blank=True, null=True)  # Field name made lowercase.
    nutrition = models.TextField(db_column='Nutrition', blank=True, null=True)  # Field name made lowercase.
    timing = models.TextField(db_column='Timing', blank=True, null=True)  # Field name made lowercase.
    img = models.TextField(db_column='Img', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recipes'