from django.shortcuts import render, redirect
from rest_framework import generics
from api6.models import DetallePedido
from api5.models import pedido
from api3.models import producto
from api6.serialeizers import DetallePedidoSerializer


# =========================
#      VISTAS HTML
# =========================

def listar_detalles(request):
    detalles = DetallePedido.objects.all()
    return render(request, 'detalles/listar.html', {'detalles': detalles})


def crear_detalle(request):
    pedidos = pedido.objects.all()
    productos = producto.objects.all()

    if request.method == "POST":
        p = request.POST.get("pedido")
        prod = request.POST.get("producto")
        cant = int(request.POST.get("cantidad"))
        precio = float(request.POST.get("precio_unitario"))

        subtotal = cant * precio

        DetallePedido.objects.create(
            pedido_id=p,
            producto_id=prod,
            cantidad=cant,
            precio_unitario=precio,
            subtotal=subtotal
        )

        return redirect('detalle-listar')

    return render(request, 'detalles/crear.html', {
        'pedidos': pedidos,
        'productos': productos
    })


# =========================
#       API JSON
# =========================

class DetallePedidoListCreateView(generics.ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class DetallePedidoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

