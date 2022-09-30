from django.urls import path
from Recipes.views import Home, Sobre, Contato


urlpatterns = [
    path('', Home),
    path('Sobre/', Sobre),
    path('Contato/', Contato),
]
