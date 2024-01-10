from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fornecedor
from .serializers import FornecedorSerializer
from rest_framework import status


class Fornecedores_por_consumo(APIView):
    def get(self, request, consumo, format=None): 
        if consumo is None:
           return Response({"detail": "Consumo é um parâmetro obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        fornecedores = Fornecedor.objects.filter(limite_minimo_kwh__lte=consumo)
        serializacao = FornecedorSerializer(fornecedores, many=True)
        return Response(serializacao.data, status=status.HTTP_302_FOUND)
        
    
class Criando_Fornecedores(APIView):
    def post(self, request, format=None):
        serializacao = FornecedorSerializer(data=request.data)
        if serializacao.is_valid():
            serializacao.save()
            return Response(serializacao.data, status=status.HTTP_201_CREATED)
        return Response(serializacao.errors, status=status.HTTP_400_BAD_REQUEST)