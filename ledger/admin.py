from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage

admin.site.register(Profile)


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInLine]
    list_display = ('name', 'author', 'created_on', 'updated_on')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)

# Register your models here.
