from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ledger"


urlpatterns = [
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe, name='recipe'),
    path('accounts/login/', views.custom_login, name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/add_image/', views.add_recipe_image, name='add_recipe_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   