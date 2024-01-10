from django.urls import path
from .views import Fornecedores_por_consumo

urlpatterns = [
    path('fornecedores_por_consumo/<int:consumo>/', Fornecedores_por_consumo.as_view(), name='fornecedores_por_consumo'),
]