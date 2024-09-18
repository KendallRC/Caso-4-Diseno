# myapp/views.py
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from random import sample

class Productos(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):

        # Contar el núACmero total de registros
        total_products = Product.objects.count()
        
        # Calcular el número de registros a retornar (0.35% del total)
        num_to_return = max(1, int(total_products * 0.35))  # Asegura que al menos un registro sea retornado
        
        # Obtener todos los registros
        all_products = list(Product.objects.all())
        
        # Seleccionar un subconjunto aleatorio de registros
        selected_products = sample(all_products, num_to_return)
        
        # Retornar el queryset de los productos seleccionados
        return Product.objects.filter(id__in=[product.id for product in selected_products])

