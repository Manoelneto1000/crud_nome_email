from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
