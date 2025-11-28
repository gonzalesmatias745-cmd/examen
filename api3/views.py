from django.shortcuts import render, redirect
from .models import producto

def listar_productos(request):
    productos = producto.objects.all()
    return render(request, 'producto/listar.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        producto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            activo=request.POST['activo'] == 'True'
        )
        return redirect('producto-listar')

    return render(request, 'producto/crear.html')

