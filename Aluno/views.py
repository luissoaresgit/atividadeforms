from django.shortcuts import render, redirect
from .models import Alunos
from .forms import AlunoForm

def home (request):
    return render(request, 'home.html')

def cadastrar_aluno (request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})

def listar_alunos (request):
    alunos = Alunos.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})
