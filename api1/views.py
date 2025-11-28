from django.shortcuts import render, redirect
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        Usuario.objects.create(
            nombre=request.POST['nombre'],
            email=request.POST['email'],
            telefono=request.POST.get('telefono', ''),
            activo=True
        )
        return redirect('usuario-listar')
    return render(request, 'usuarios/crear.html')

