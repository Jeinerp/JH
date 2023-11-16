from rest_framework import viewsets
from .models import Producto
from .serializers import ProductosSerializer
from .models import TipoProducto
from .serializers import TipoProductoSerializer


class ProductosViewSet (viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class TipoProductoViewSet (viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
