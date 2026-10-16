from django.shortcuts import render

def index(request):
# ERRO ENCONTRADO: def index(request): return render( request, 'templates/portal/index.html') - caminho do arquivo html está incorreto. Django não consegue localizar o arquivo e retorna uma mensagem de erro no terminal.
# CORREÇÃO: O caminho do arquivo HTML foi corrigido para que o sistema consiga localizar o arquivo corretamente. O caminho correto é: 'portal/index.html' 
    return render(request,'portal/index.html')

def cadastro(request):
    return render(request,'portal/cadastro.html')       
