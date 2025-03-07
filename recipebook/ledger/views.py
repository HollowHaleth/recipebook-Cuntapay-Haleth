from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe(request, id):
    recipe = Recipe.objects.get(id=id) 
    return render(request, 'recipes.html', {'recipe': recipe})