from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Recipe, Ingredient, Restriction


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Recipe
    template_name = 'search_results.html'
    def get_queryset(self): #
        query = self.request.GET.get('food_search')
        return Recipe.objects.filter(
            Q(name__icontains=query) | Q(ingredients__icontains=query) | Q(proteinLevel__icontains = query) | Q(fatLevel__icontains = query)
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