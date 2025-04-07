from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory, inlineformset_factory


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


@login_required
def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('ledger:recipe_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ledger:recipe_list')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('ledger:login')


@login_required
def add_recipe(request):
    recipes = Recipe.objects.all()  
    ingredients = Ingredient.objects.all()  

    if request.method == 'POST':
        
        if 'create_recipe' in request.POST:
            recipe_name = request.POST.get('recipe_name')
            recipe = Recipe.objects.create(name=recipe_name, author=request.user)

        
        if 'create_ingredient' in request.POST:
            ingredient_name = request.POST.get('ingredient_name')
            ingredient = Ingredient.objects.create(name=ingredient_name)

        
        if 'create_recipe_ingredient' in request.POST:
            quantity = request.POST.get('quantity')
            ingredient_id = request.POST.get('ingredient')
            recipe_id = request.POST.get('recipe')

            
            ingredient = Ingredient.objects.get(id=ingredient_id)
            recipe = Recipe.objects.get(id=recipe_id)

            
            RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                quantity=quantity
            )

            return redirect('ledger:recipe_list')  

    return render(request, 'add_recipe.html', {
        'recipes': recipes,
        'ingredients': ingredients
    })


@login_required
def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    RecipeImageForm = modelform_factory(RecipeImage, fields=['image', 'description'])

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('ledger:recipe', pk=recipe.pk)
    else:
        form = RecipeImageForm()

    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})