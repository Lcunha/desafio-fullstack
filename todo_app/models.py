from django.utils import timezone

from django.db import models
from django.urls import reverse


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    realizado = models.BooleanField()
    prioridade = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)

    #Método que retorna o URL do objeto específico 
    def get_absolute_url(self):
        return reverse(
            "tarefa-update", args=[str(self.id)]
        )
    
    #Método usado para retornar uma representação de string de um objeto
    def __str__(self):
        return f"{self.nome}:  {self.data_criacao}"
    
    #Definindo a ordem do retorno das tarefas
    class Meta:
        ordering = ["prioridade"]


