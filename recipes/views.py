from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe
from django.core.paginator import Paginator


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    paginator = Paginator(recipes, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/pages/home.html', context={
        "page_obj": page_obj,
    })


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        title__icontains=search_term,
        is_published=True).order_by('title')

    paginator = Paginator(recipes, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/pages/search_results.html',
                  context={
                      'page_obj': page_obj,
                      'search_term': search_term,
                  })


def category(request, category_id):
    qset_recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
        ).order_by('-id')

    recipes = get_list_or_404(qset_recipes)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{qset_recipes.first().category.name} - Category'
    })


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published=True,
    )

    return render(request, 'recipes/pages/recipe-detail.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
