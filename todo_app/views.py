rom typing import Any
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
    


