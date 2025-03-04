from django.shortcuts import render

recipes_data = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"},
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2cup"},
                {"name": "water", "quantity": "1 cup"},
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"},
            ],
            "link": "/recipe/2"
        }
    ]
}

def recipe_list(request):
    return render(request, 'recipe_list.html', recipes_data)

def recipe_1(request):
    recipe = recipes_data["recipes"][0]
    return render(request, 'recipes.html', {"recipe": recipe})

def recipe_2(request):
    recipe = recipes_data["recipes"][1]
    return render(request, 'recipes.html', {"recipe": recipe})