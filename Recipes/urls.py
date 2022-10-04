from django.urls import path
from . import views  # abreviação de importação 


urlpatterns = [
    path('', views.Home),
    path('recipes/<int:id>/', views.Recipe),  # tornar as urls mais seguras 
]
