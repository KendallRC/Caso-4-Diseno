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
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer  

    def list(self, request, *args, **kwargs):
        productos = obtener_porcentaje_registros(self.queryset, 0.35)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)

# Endpoint con el 35% de los registros y el pool connection
class ProductosViewSet2(viewsets.ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer  

    def list(self, request, *args, **kwargs):
        productos_pool = obtener_porcentaje_registros(Product.objects.using('pool'), 0.35)
        serializer = self.get_serializer(productos_pool, many=True)
        return Response(serializer.data)

# Endpoint con el 35% de los registros, el pool connection y la caché de redis
class ProductosViewSet3(viewsets.ModelViewSet):
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer 

    def list(self, request, *args, **kwargs):

        param1 = request.query_params.get('numero_producto')  
        print(param1)
        valor = cache.get(param1)
        valor = None
        if valor is None:
            productos_pool = obtener_porcentaje_registros(Product.objects.using('pool').filter(name__icontains=param1), 0.35)
            serializer = self.get_serializer(productos_pool, many=True)
            cache.set(param1, serializer.data, timeout=300)  
        else:
            return Response(valor)
        return Response(serializer.data)