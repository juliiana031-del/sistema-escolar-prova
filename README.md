# Descrição do projeto:

Foi desenvolvido um Projeto de um Sistema Escolar para cadastro de informações de Professores, Alunos e Aulas.

# O cadastro do Professor deve conter as seguintes informações: 
1. Nome
2. Sobrenome
3. Email
4. Data da criação do cadastro
5. Registro do professor
6. Disciplina que o professor oferece
7. Atividade - se o professor está ativo ou não no sistema
8. Observação - campo opcional para escrita de uma observação
9. Imagem - campo opcional para inserção de imagem do professor no sistema

# O cadastro do Aluno deve conter as seguintes informações: 
1. Nome
2. Sobrenome
3. Email
4. Telefone
5. Matrícula 
6. Data de criação do cadastro
7. Observação - campo opcional para escrita de uma observação
8. Atividade - se o aluno está ativo ou não no sistema
9. Imagem - campo opcional para inserção de imagem do aluno no sistema

# O cadastro das Aulas deve conter as seguintes informações: 
1. 
2.
3.
4.
5.

# ERROS

# --> Arquivo: models.py (02 erros)

O arquivo models.py geralmente contem: 

- As ferramentas importadas do Django que são uteis para o nosso projeto - "os imports"
- As classes com atributos e seus tipos
- Os métodos (ações) 

# ERRO (01): 
Linha 04 -  Ausência da importação da ferramenta que fornece data/ hora com fuso horário correto. 
# CORREÇÃO (01): 
from django.utils import timezone 
((Sem essa parte do código, o Python não vai saber interpretar a instrução presente no campo "criação_data"))

# ERRO (02): 
Linha 15: - registro = models.CharField(max_length=10)
Linha 31 - matricula = models.IntegerField()
# CORREÇÃO (02): 
Linha 15 - registro = models.CharField(max_length=10, unique=True)
Linha 31 - matricula = models.IntegerField(unique=True)
((Para garantir que não existam registros duplicados, os atributos "matrícula" (na classe Aluno) e "registro" (na classe professor) devem possuir regra de restrição.))

# ERRO : 
O campo "imagem" (linhas 21 e 39) depende da instalação da biblioteca Pillow no computador. Se a biblioteca Pillow não estiver instalada, aparece uma mensagem de erro no terminal e o sistema trava. 
# CORREÇÃO:  
Antes de rodar o servidor, devemos instalar a biblioteca Pillow
escrevendo no terminal o comando: pip install django Pillow
-------------------------------------------------------------

# --> Arquivo: admin.py (01 erro)

O Django vem com um painel administrativo pronto. Para que os nossos models apareçam la precisamos importar o módulo pronto do Django, importar os models e registrá-los no arquivo.

# ERRO (03): 
Linha 8 - list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',) - Não existe o campo "especialidade", dentro da Classe Professor, no arquivo models.py. Se deixar assim, o Django vai procurar por "especialidade" e vai apresentar uma mensagem de erro no servidor. 

# CORREÇÃO (03): 
list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',) - O "list display" define quais colunas devem aparecer no nosso Portal Administrativo. Todos os campos, atributos ou métodos listados devem existir no models.py. Por isso, trocamos o campo "especialidade" pelo campo "disciplina" que está presente dentro da Classe Professor.

-------------------------------------------------------------

# --> Arquivo: settings.py (01 erro)

O arquivo settings.py é o arquivo de configurações do Django. 
Nele definimos os apps instalados, onde ficam os templates, como funciona o banco de dados, idioma, fuso horário e etc. 

# ERRO (04): 
Ausência do app "portal" na lista de apps instalados. Sem ela escrita nessa lista, para o Django, é como se essa pasta ficasse invisível para o sistema. É uma espécie de registro do app. 

# CORREÇÃO (04): 
'portal', 
Embora a pasta portal exista fisicamente, você precisa dizer ao Django que ela está habilitada e que ele deve consultá-la colocando ela na lista de apps instalados.   

--------------------------------------------------------------------

# --> Arquivo: views.py (01 erro)
A view é um arquivo que contém uma função ou classe Python responsável por executar uma ação. 
Ela recebe uma solicitação -> consulta infos/prepara uma página html -> devolve uma resposta

# ERRO (05): 
def index(request):
    return render(
        request,
        'templates/portal/index.html'
    )

O segundo argumento na função index está errado.

# CORREÇÃO (05): 
def index(request):
    return render(request,'portal/index.html')

Com o app devidamente registrado na lista de apps, o Django já procura e entra automaticamente dentro das pasta templates para procurar por um arquivo html. Por isso, não precisamos escrever essa pasta novamente no caminho da nossa request. 


# --> Arquivo : 

 



