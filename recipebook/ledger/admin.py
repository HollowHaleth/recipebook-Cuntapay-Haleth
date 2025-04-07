from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("name",)
    search_fields = ("name",)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("name", "author", "created_on", "updated_on")
    search_fields = ("name", "author__username")
    list_filter = ("author", "created_on")
    inlines = [RecipeIngredientInline, RecipeImageInline]  

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ("recipe", "ingredient", "quantity",)
    list_filter = ("recipe", "ingredient",)
    search_fields = ("recipe__name", "ingredient__name",)

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ("recipe", "description", "image")
    search_fields = ("recipe__name", "description")

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)

