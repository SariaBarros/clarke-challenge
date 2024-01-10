from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    estado_origem = models.CharField(max_length=50)
    custo_por_kwh = models.DecimalField(max_digits=5, decimal_places=2)
    limite_minimo_kwh = models.PositiveIntegerField()
    numero_total_clientes = models.PositiveIntegerField()
    avaliacao_media_clientes = models.DecimalField(max_digits=3, decimal_places=2)
    