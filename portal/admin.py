from django.contrib import admin
from portal import models

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
# ERRO ENCONTRADO: list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',) - Não existe o campo "especialidade" no models.py.
# CORREÇÃO: Os campos listados devem existir no models.py. Foi alterado o campo "especialidade" para "disciplina". 
    list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
