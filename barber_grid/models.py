from django.db import models

class Agendamento(models.Model):
    """Um agendamento para barbearia"""
    servico = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.servico  
    

class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""