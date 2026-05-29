from django.db import models


class Servico(models.Model):
    """Tipos de serviço que a barbearia oferece, tipo cabelo, barba, sobrancelha"""
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, null=True, decimal_places=2)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    """Um agendamento para barbearia marcado pelo cliente"""
    cliente_nome = models.CharField(max_length=100, null=True, blank=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True)

    data_agendada = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        nome_servico = self.servico.nome if self.servico else "Sem serviço" #tudo na mesma linha
        return f"{self.cliente_nome or 'Anônimo - {nome_servico}'}"

       
                                
                                
                                