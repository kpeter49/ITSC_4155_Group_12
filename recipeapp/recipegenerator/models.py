from django.db import models

# Create your models here.

class Recipe():
    def __init__(self, name = "", servings = 0, ingredients = []):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients

    def getName(self):
        return self.name