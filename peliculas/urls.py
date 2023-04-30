from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarPelicula/', views.registrarPelicula),
    path('edicionPelicula/<id>', views.edicionPelicula),
    path('editarPelicula/', views.editarPelicula),
    path('eliminarPelicula/<id>', views.eliminarPelicula)
    
]
