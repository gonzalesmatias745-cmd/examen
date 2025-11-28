from django.shortcuts import render, redirect
from .models import Categoria

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        Categoria.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST.get('descripcion', '')
        )
        return redirect('categoria-listar')
    return render(request, 'categorias/crear.html')
