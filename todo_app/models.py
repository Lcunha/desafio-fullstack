from django.utils import timezone

from django.db import models
from django.urls import reverse


class Tarefa(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True, max_length=100)
    realizado = models.BooleanField()

    PRIORIDADE_CHOICES = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    prioridade = models.IntegerField(choices=PRIORIDADE_CHOICES)
    data_criacao = models.DateField(auto_now_add=True)
    ordem = models.PositiveIntegerField(default=1, editable=False)

    def save(self, *args, **kwargs):
        # Verificando se a tarefa é nova (ainda não tem uma ordem atribuída)
        if not self.ordem:
            # Encontrando a ordem máxima atual e adicione 1
            max_ordem = Tarefa.objects.aggregate(models.Max('ordem'))['ordem__max']
            if max_ordem is not None:
                self.ordem = max_ordem + 1
            else:
                self.ordem = 1
        super(Tarefa, self).save(*args, **kwargs)

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
        ordering = ["ordem"]


