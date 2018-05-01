from django.db import models

# Create your models here.
class DadosCOSERN(models.Model):
    tarifa = models.FloatField()
    importe = models.FloatField()
    valor_fatura = models.FloatField()
    injetado_fv = models.FloatField()
    tributo_federal = models.FloatField()
    consumo_energia_ativa_na_ponta_qtd = models.FloatField()
    consumo_energia_ativa_na_ponta_valor = models.FloatField()
    consumo_energia_ativa_fora_ponta_qtd = models.FloatField()
    consumo_energia_ativa_fora_ponta_valor = models.FloatField()

class ProducaoUsina(models.Model):
    hora = models.TimeField()
    valor = models.FloatField()