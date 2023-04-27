from django.shortcuts import render, redirect
from .models import Pelicula

# Create your views here.

def home(request):
    peliculas = Pelicula.objects.all()
    return render(request, "gestionpeliculas.html", {"peliculas":peliculas})

def registrarPelicula(request):
    id=request.POST['txtId']
    nombre=request.POST['txtNombre']
    duracion=request.POST['txtDuracion']
    productora=request.POST['txtProductora']
    fecha_estreno=request.POST['txtDate']
    
    pelicula=Pelicula.objects.create(
        id=id, nombre=nombre, duracion=duracion, productora=productora, fecha_estreno=fecha_estreno)
    return redirect('/')