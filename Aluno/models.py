from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
