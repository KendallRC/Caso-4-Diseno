# myapp/views.py
import random
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
from django.core.cache import cache
    
# Obtener el 35% de los registros
def obtener_porcentaje_registros(queryset, porcentaje):
        total_registros = queryset.count()
        cantidad_a_consultar = int(total_registros * porcentaje)
        return queryset.all()[:cantidad_a_consultar]

# Endpoint con el 35% de los registros
class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Este es el queryset normal
    serializer_class = ProductSerializer  # Asegúrate de tener un serializer definido

    def list(self, request, *args, **kwargs):
        # Endpoint para obtener el 35% de registros usando la conexión normal
        productos = obtener_porcentaje_registros(self.queryset, 0.35)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)

# Endpoint con el 35% de los registros y el pool connection
class ProductosViewSet2(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Este es el queryset normal
    serializer_class = ProductSerializer  # Asegúrate de tener un serializer definido

    def list(self, request, *args, **kwargs):
        # Endpoint para obtener el 35% de registros usando la conexión con pool
        productos_pool = obtener_porcentaje_registros(Product.objects.using('pool'), 0.35)
        serializer = self.get_serializer(productos_pool, many=True)
        return Response(serializer.data)

# Endpoint con el 35% de los registros, el pool connection y la caché de redis
class ProductosViewSet3(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Este es el queryset normal
    serializer_class = ProductSerializer  # Asegúrate de tener un serializer definido

    def list(self, request, *args, **kwargs):

        valor = cache.get('mi_clave')
        if valor is None:
            # Endpoint para obtener el 50% de registros usando la conexión normal
            productos_pool = obtener_porcentaje_registros(Product.objects.using('pool'), 0.35)
            serializer = self.get_serializer(productos_pool, many=True)
            cache.set('mi_clave', serializer.data, timeout=300)  # Expira en 300 segundos
        else:
            return Response(valor)
        return Response(serializer.data)