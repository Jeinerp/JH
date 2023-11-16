from rest_framework import viewsets
from .models import Cliente
from .serializers import ClientesSerializer


class ClientesViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer