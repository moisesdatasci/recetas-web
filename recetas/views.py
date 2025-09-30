from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Receta

# Create your views here.
def inicio(request):
    recetas = Receta.objects.all()[0:6]
    return render(request, 'recetas/inicio.html', {'recetas': recetas})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        if nombre and email and mensaje:
            messages.success(request, '¡Mensaje enviado correctamente!')
            return redirect('confirmacion')
        else:
            messages.warning(request, 'Por favor completa todos los campos.')
    
    return render(request, 'recetas/contacto.html')

def confirmacion(request):
    return render(request, 'recetas/confirmacion.html')