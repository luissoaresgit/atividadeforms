from django.urls import path
from .views import home, cadastrar_aluno, listar_alunos

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('cadastro/', cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', listar_alunos, name='listar_alunos'),
]

