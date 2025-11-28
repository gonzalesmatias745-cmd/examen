from django.shortcuts import render, redirect
from rest_framework import generics
from api5.models import pedido
from api1.models import Usuario
from api5.serializers import PedidoSerializer


# ============================
#     VISTAS HTML
# ============================

def listar_pedidos(request):
    pedidos = pedido.objects.all()
    return render(request, 'pedidos/listar.html', {'pedidos': pedidos})


def crear_pedido(request):
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        usuario_id = request.POST.get("usuario")
        estado = request.POST.get("estado")
        total = request.POST.get("total")
        direccion = request.POST.get("direccion_envio")

        pedido.objects.create(
            usuario_id=usuario_id,
            estado=estado,
            total=total,
            direccion_envio=direccion
        )
        return redirect('pedido-listar')

    return render(request, 'pedidos/crear.html', {'usuarios': usuarios})


# ============================
#     API JSON
# ============================

class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer


