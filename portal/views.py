from django.shortcuts import render

def index(request):
    return render(request, 'portal/index.html')

# ERRO ENCONTRADO: O arquivo 'views.py' não possui a views do cadastro. O arquivo 'urls.py' direciona para ela. 
# CORREÇÃO: Criamos uma função chamada 'cadastro' que retorna para o usuário a página de cadastro.
def cadastro(request):
    return render(request, 'portal/cadastro.html')       
