from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Aluno

def home_aluno(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        return render(request, 'home_aluno.html', {'alunos': alunos})
    elif request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')

        aluno = Aluno(
            nome=nome,
            email=email
        )

        aluno.save()
        return redirect('home_aluno')
    
def deletar_aluno(request, id):
    # aluno = Aluno.objects.get(id = id)
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('home_aluno')

def editar_aluno(request, id):

    nome_editado = request.POST.get('nome')
    email_editado = request.POST.get('email')

    aluno_banco = get_object_or_404(Aluno, id=id)
    aluno_banco.nome = nome_editado
    aluno_banco.email = email_editado
    aluno_banco.save()
    return redirect('home_aluno')

