from django.db import models
# ERRO ENCONTRADO: ausência do "import "timezone
# CORREÇÃO: Adicionar a ferramenta de ajuste de fuso horário para que o sistema gere corretamente a data/hora de criação dos registros.
from django.utils import timezone


class Professor(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=15)
# ERRO ENCONTRADO: registro = models.CharField(max_length=10) - ausência da regra de restrição para impedir registros duplicados.
# CORREÇÃO: Adicionar a regra de restrição para impedir que o sistema aceite registros duplicados.
    registro = models.CharField(max_length=10, unique=True)
    disciplina = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(blank=True)
# ERRO ENCONTRADO: O campo "imagem" depende da instalação da biblioteca Pillow no computador. Se a biblioteca Pillow não estiver instalada, aparece uma mensagem de erro no terminal e o sistema trava.
# CORREÇÃO: pip install django pillow (antes de rodar o servidor)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
# ERRO ENCONTRADO: matricula = models.IntegerField() - ausência da regra de para impedir registros duplicados.
# CORREÇÃO: Adicionar a regra de restrição para impedir que o sistema aceite registros duplicados.
    matricula = models.IntegerField(unique=True)
    criacao_data = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
# ERRO ENCONTRADO: O campo "imagem" depende da instalação da biblioteca Pillow no computador. Se a biblioteca Pillow não estiver instalada, aparece uma mensagem de erro no terminal e o sistema trava.
# CORREÇÃO: pip install django pillow (antes de rodar o servidor)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aula(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    horario = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada')
        )
    )

    def __str__(self):
        return f'Aula {self.status} com sucesso.'
