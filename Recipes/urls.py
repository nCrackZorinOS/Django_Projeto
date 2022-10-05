from django.urls import path
from . import views  # abreviação de importação 

app_name = 'recipes'

urlpatterns = [
    path('', views.Home, name="home"),  # Forma antiga recipes-home tudo na mesma linha
    path('recipes/<int:id>/', views.Recipe, name="recipe"),  # tornar as urls mais seguras 
]
