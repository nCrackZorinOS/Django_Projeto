from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return render(request, 'recipes/pages/home.html', context={
        'nome': 'Vitor Hirt',
    })


def Sobre(request):
    return HttpResponse('Sobre')


def Contato(request):
    return HttpResponse('Contato')
