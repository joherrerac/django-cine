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
    fecha_estreno=request.POST['txtFecha']
    
    pelicula=Pelicula.objects.create(
        id=id, nombre=nombre, duracion=duracion, productora=productora, fecha_estreno=fecha_estreno)
    
    return redirect('/')

def edicionPelicula(request, id):
    pelicula=Pelicula.objects.get(id=id)
    
    return render(request, "edicionPelicula.html", {"pelicula": pelicula})

def editarPelicula(request):
    id=request.POST['txtId']
    nombre=request.POST['txtNombre']
    duracion=request.POST['txtDuracion']
    productora=request.POST['txtProductora']
    fecha_estreno=request.POST['txtFecha']
    
    pelicula=Pelicula.objects.get(id=id)
    pelicula.nombre = nombre
    pelicula.duracion = duracion
    pelicula.productora = productora
    pelicula.fecha_estreno = fecha_estreno
    pelicula.save()
    
    return redirect('/')


def eliminarPelicula(request, id):
    pelicula=Pelicula.objects.get(id=id)
    pelicula.delete()
    
    return redirect('/')