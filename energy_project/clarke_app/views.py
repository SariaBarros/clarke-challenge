from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fornecedor
from .serializers import FornecedorSerializer

class Fornecedores_por_consumo(APIView):
    def get(self, request, consumo, format=None):
        fornecedores = Fornecedor.objects.filter(limite_minimo_kwh__lte=consumo)
        serializacao = FornecedorSerializer(fornecedores, many=True)
        return Response(serializacao.data)
    