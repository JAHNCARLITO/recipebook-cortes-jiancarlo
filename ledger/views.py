from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Centralized data to mimic a database for now

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_details.html', {'recipe': recipe})