from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile

admin.site.register(Profile)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('name', 'author', 'created_on', 'updated_on')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)

# Register your models here.
