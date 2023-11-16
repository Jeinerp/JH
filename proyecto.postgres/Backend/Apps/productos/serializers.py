from rest_framework import serializers
from .models import Producto
from .models import TipoProducto

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer): 

    class Meta:
        model = TipoProducto
        fields = '__all__'