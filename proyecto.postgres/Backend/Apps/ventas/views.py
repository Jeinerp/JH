from rest_framework import viewsets
from .models import Venta
from .serializers import VentasSerializer


class VentasViewSet (viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentasSerializer