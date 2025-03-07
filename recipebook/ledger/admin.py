from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):  
    model = RecipeIngredient  

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient  
    list_display = ("name",) 
    search_fields = ("name",) 

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe  
    list_display = ("name",) 
    search_fields = ("name",) 
    inlines = [RecipeIngredientInline] 

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ("recipe", "ingredient", "quantity",)
    list_filter = ("recipe", "ingredient",)
    search_fields = ("recipe__name", "ingredient__name",)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)