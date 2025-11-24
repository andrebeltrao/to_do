from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from main.models import Task # importar a tabela que vamos usar!


class HomeView(TemplateView):
    template_name = 'home.html'


class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tarefas'

    # views - url - template
    
def task_list(request):
    tarefas = Task.objects.all() #trazendo tudo da tabala task
    context = {
        "tarefas":tarefas,
        "titulo_pagina": 'Minhas Tarefas'            
    }
    return render(request, 'tasks/task_list.html', context)


def task_concluido(request):
    
    tarefas = Task.objects.filter(concluida=1)  #trazendo tudo da tabela task
    context = {
        "tarefas":tarefas,
        "titulo_pagina": 'Minhas Tarefas Concluidas'
    }
    return render(request, 'tasks/teste.html', context)

def task_pendente(request):
    
    tarefas = Task.objects.filter(concluida=0)  #trazendo tudo da tabela task
    context = {
        "tarefas":tarefas,
        "titulo_pagina": 'Minhas Tarefas Pendentes'
    }
    return render(request, 'tasks/teste2.html', context)   