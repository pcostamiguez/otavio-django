from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'param': 'Daileon 2',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-detail.html', context={
        'param': id,
    })
