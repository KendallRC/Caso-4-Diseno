# myapp/views.py
import random
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
from .cnxMySQL import fetch_products_from_db
from django.core.cache import cache


class registersResponse:
    def get_random_sample(self, queryset, percentage=0.35):
        total_count = queryset.count()
        sample_size = int(total_count * percentage)
        return random.sample(list(queryset), sample_size) if total_count > 0 else []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        porcentaje = 0.35
        sampled_queryset = self.get_random_sample(queryset, porcentaje)
        serializer = self.get_serializer(sampled_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductViewSet(registersResponse, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet2(registersResponse, viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        # Usar el pool de conexiones para consultar los productos
        query = "SELECT * FROM products WHERE id = 2"  # Consulta SQL personalizada
        products = fetch_products_from_db(query)

        # Convertir el resultado a un formato compatible con el serializador
        # Suponemos que 'products' es una lista de diccionarios que coinciden con el modelo Product
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProductViewSet3(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        
        from django.core.cache import cache

        cache.set('mi_clave', 'mi_valor', timeout=300)  # Expira en 300 segundos

        valor = cache.get('mi_clave')
        if valor is None:
            # Si no hay valor en caché, realiza alguna acción
            # Usar el pool de conexiones para consultar los productos
            query = "SELECT * FROM products WHERE id = 2"  # Consulta SQL personalizada
            products = fetch_products_from_db(query)

        # Convertir el resultado a un formato compatible con el serializador
        # Suponemos que 'products' es una lista de diccionarios que coinciden con el modelo Product
        serializer = self.get_serializer(products, many=True)

        print(serializer)

      #  set_cache_response(cache_key, serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)
    



