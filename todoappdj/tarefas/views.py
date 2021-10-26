from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tarefa
# Create your views here.
def index (request):
    tarefa=Tarefa.objects.all()
    if request.POST:
        tarefa=request.POST.get('conteudo')
        tarefa=Tarefa(conteudo=tarefa)
        tarefa.save()
        return redirect('index')
    context={
        'tarefa':tarefa,
    }
    return render(request, 'tarefa/index.html', context)
def excluir_tarefa(request, id):
    tarefa=Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('index')