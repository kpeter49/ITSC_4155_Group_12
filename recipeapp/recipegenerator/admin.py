from django.contrib import admin

# Register your models here.

from .models import Recipe, Ingredient, Restriction

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "ingredients","proteinLevel","fatLevel")

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Ingredient)

admin.site.register(Restriction)