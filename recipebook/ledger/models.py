from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def link(self):
        return reverse("ledger:recipe_list")

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def link(self):
        return reverse("ledger:recipe", args=[str(self.id)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")