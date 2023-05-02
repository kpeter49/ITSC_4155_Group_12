from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Recipe, Ingredient, Restriction, Recipes

import re


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Recipes
    template_name = 'search_results.html'
    def get_queryset(self): #
        query = self.request.GET.get('food_search')
        filtersQ = Q(recipename__icontains=query) | Q(ingredients__icontains=query)
        selectedIds = Restriction.objects.filter(userName = self.request.user.username)
        selectedIngredients = []
        for item in selectedIds:
            selectedIngredients.append(Ingredient.objects.get(id=item.ingredientId).name)
        for restriction in selectedIngredients:
            filtersQ = filtersQ & ~Q(ingredients__icontains=restriction)
        return Recipes.objects.filter(
            filtersQ
        )

class ProfileView(TemplateView):
    template_name = 'profile.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def restrictionsview(request):
    if request.method == 'POST':
        if request.POST.get('ingredientadd'):
            Restriction.objects.create(ingredientId=request.POST.get('ingredientadd'), userName=request.user.username)
        if request.POST.get('ingredientremove'):
            Restriction.objects.get(ingredientId=request.POST.get('ingredientremove')).delete()
    
    selectedIds = Restriction.objects.filter(userName = request.user.username)
    selectedIngredients = []
    for item in selectedIds:
        selectedIngredients.append({'ingredientId':item.ingredientId, 'ingredientName':Ingredient.objects.get(id=item.ingredientId).name})
    return render(request, 'restrictions.html', {'all_ingredients' : Ingredient.objects.all(), 'selected_ingredients': selectedIngredients})

def __countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
                      for sub in [lst1, lst2]]

def recipeview(request):
    servingMultiplier = 1
    if request.method == 'POST':
        if request.POST.get('multiplier'):
            servingMultiplier = int(request.POST.get('multiplier'))

    ingredients = Recipes.objects.get(id=request.GET.get('id')).ingredients.split(',')
    for j, fact in enumerate(ingredients):
        nums = re.findall(r'\d+', fact)
        if nums:
            nums[0] = str(int(nums[0]) * servingMultiplier)
        segments = re.sub(r'\d+', '~', fact).split('~')
        fact = ''.join(__countList(segments, nums))
        ingredients[j] = fact + segments[-1]

    nutritionfacts = Recipes.objects.get(id=request.GET.get('id')).nutrition.split(',')
    for j, fact in enumerate(nutritionfacts):
        nums = re.findall(r'\d+', fact)
        for i, num in enumerate(nums):
            nums[i] = str(int(num) * servingMultiplier)
        segments = re.sub(r'\d+', '~', fact).split('~')
        fact = ''.join(__countList(segments, nums))
        nutritionfacts[j] = fact + '%'

    instructions = Recipes.objects.get(id=request.GET.get('id')).directions.split('.')
    return render(request, 'recipe.html', {'id' : request.GET.get('id'),
                                           'recipe': Recipes.objects.get(id=request.GET.get('id')),
                                           'ingredients': ingredients,
                                           'nutritionfacts': nutritionfacts,
                                           'instructions': instructions,
                                           'multiplier': servingMultiplier})

