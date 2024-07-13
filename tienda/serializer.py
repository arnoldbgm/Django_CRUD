from rest_framework import serializers
from .models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoriaId = CategoriaSerializer()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descripcion', 'categoriaId']
