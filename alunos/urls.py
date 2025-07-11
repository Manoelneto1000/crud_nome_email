from django.urls import path
from . import views

urlpatterns = [
    path('home_aluno/', views.home_aluno, name='home_aluno'),
    path('deletar_aluno/<int:id>', views.deletar_aluno, name='deletar_aluno'),
    path('editar_aluno/<int:id>', views.editar_aluno, name='editar_aluno'),
]