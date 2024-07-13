from django.urls import path
from .views import ProductoListCreate, ProductoDetail, CategoriaListCreate, CategoriaDetail

urlpatterns = [
    path('productos/', ProductoListCreate.as_view(), name='producto_list_create'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='producto_detail'),
    path('categorias/', CategoriaListCreate.as_view(), name='categoria_list_create'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria_detail'),
]
