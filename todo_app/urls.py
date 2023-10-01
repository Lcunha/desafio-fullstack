from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListarTarefasView.as_view(), name="index"),
    path("tarefa/add", views.TarefaCreate.as_view(), name="tarefa-add"),
    path("tarefa/<int:pk>/", views.TarefaUpdate.as_view(), name="tarefa-update"),
    path("tarefa/<int:pk>/delete/", views.TarefaDelete.as_view(), name="tarefa-delete"),
    path("reordenar_tarefas/", views.reordenar_tarefas, name='reordenar_tarefas'),    
]