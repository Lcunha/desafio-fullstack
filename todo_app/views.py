from typing import Any
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Tarefa

class ListarTarefasView(ListView):
    model = Tarefa
    template_name = "todo_app/index.html"

class TarefaCreate(CreateView):
    model = Tarefa
    template_name = "todo_app/tarefa_form.html"
    fields = [
        "nome",
        "descricao",
        "realizado",
        "prioridade",       
    ]
    
    def get_context_data(self):
        context = super(TarefaCreate, self).get_context_data()
        context["titulo"] = "Nova Tarefa"
        context["update"] = False
        return context
    
    def get_success_url(self):
        return reverse("index")
    
class TarefaUpdate(UpdateView):
    model = Tarefa
    fields = [
        "nome",
        "descricao",
        "realizado",
        "prioridade",
    ]

    def get_context_data(self):
        context = super(TarefaUpdate, self).get_context_data()
        context["titulo"] = "Editar Tarefa"
        context["update"] =  True
        return context
    
    def get_success_url(self):
        return reverse("index")
    
class TarefaDelete(DeleteView):
    model = Tarefa

    def get_success_url(self):
        return reverse_lazy("index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

