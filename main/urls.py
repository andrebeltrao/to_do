from django.urls import path
from main.views import TaskList
from . import views

urlpatterns = [
    path("", TaskList.as_view(), name='task_list'),   
    path('funcao/', views.task_list, name='task_list_funcao'),
    path('concluidas/', views.task_concluido, name='task_concluido_funcao'),
    path('pendentes/', views.task_pendente, name='task_pendente_funcao')  
]