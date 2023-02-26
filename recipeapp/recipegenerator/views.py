from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Recipe


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