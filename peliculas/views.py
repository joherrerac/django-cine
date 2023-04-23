from django.shortcuts import render
from .models import Pelicula

# Create your views here.

def home(request):
    peliculas = Pelicula.objects.all()
    return render(request, "gestionpeliculas.html", {"peliculas":peliculas})