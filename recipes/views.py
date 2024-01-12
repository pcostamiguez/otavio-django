from django.shortcuts import render, get_list_or_404
from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True,
    #     ).order_by('-id')
    recipes = get_list_or_404(Recipe, 
                              category__id=category_id,
                              is_published=True)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category'
    })


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-detail.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
