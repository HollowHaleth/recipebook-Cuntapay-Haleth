from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def link(self):
        return reverse("ledger:recipe_list")


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name


    def link(self):
        return reverse("ledger:recipe", args=[self.pk])


class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/')
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image for {self.recipe.name} - {self.description[:20]}"
    

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")