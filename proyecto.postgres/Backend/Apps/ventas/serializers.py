from rest_framework import serializers
from .models import Venta

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'