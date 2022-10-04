from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return render(request, 'recipes/pages/home.html', context={
        'nome': 'Vitor Hirt',
    })


def Recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'nome': 'Vitor Hirt',
    })
