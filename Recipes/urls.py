from django.urls import path
from Recipes.views import Home


urlpatterns = [
    path('', Home),
]
