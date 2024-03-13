from django.db import models
from geral.models import Oficina

# Create your models here.

class Servico(models.Model):
    models.ForeignKey(Oficina, verbose_name = 'Oficina', on_delete=models.CASCADE, null=True )
    nome = models.CharField(verbose_name='Nome', max_length=70)
    descrucao = models.TextField(verbose_name='Descrição', blank = True, null=True)
    valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
    comissao=models.DecimalField(verbose_name='Comissão R$', max_digits=19, decimal_places=2)
    
    def __str__ (self) -> str:
        return self.nome
    
    class Meta:
        verbose_name='Servico'
        verbose_name_plural='Servicos'
        ordering = ['nome']
