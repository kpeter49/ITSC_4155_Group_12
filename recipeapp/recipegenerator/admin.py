from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "ingredients","proteinLevel","fatLevel")

admin.site.register(Recipe, RecipeAdmin)
