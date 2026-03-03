# <appname>/urls.py

from django.urls import path
from .views import recipe_list, recipe_detail
from . import views

urlpatterns = [
    path('', views.recipe_list, name='home'),
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
]