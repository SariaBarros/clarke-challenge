from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    #comentado para teste
    #logo = models.ImageField(upload_to='logos/', default=None)
    logo = models.CharField(max_length=100)
    estado_origem = models.CharField(max_length=50, default=None)
    custo_por_kwh = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    limite_minimo_kwh = models.PositiveIntegerField()
    numero_total_clientes = models.PositiveIntegerField()
    avaliacao_media_clientes = models.DecimalField(max_digits=3, decimal_places=2)
    