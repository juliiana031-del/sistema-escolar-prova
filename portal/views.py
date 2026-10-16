from django.shortcuts import render

def index(request):
<<<<<<< HEAD
    return render(
        request,
        'templates/portal/index.html'
    )

# ERRO ENCONTRADO: O arquivo 'portal/views.py' não possui a view  'cadastro'. O arquivo 'urls.py' direciona para ela.
# CORREÇÃO: Criamos uma função chamada cadastro que retorna para o usuario a pagina de cadastro.
def cadastro(request):
    return render(request,'templates/portal/cadastro.html')       
=======
    return render(request, 'portal/index.html')

# ERRO ENCONTRADO: O arquivo 'views.py' não possui a views do cadastro. O arquivo 'urls.py' direciona para ela. 
# CORREÇÃO: Criamos uma função chamada 'cadastro' que retorna para o usuário a página de cadastro.
def cadastro(request):
    return render(request, 'portal/cadastro.html')       
>>>>>>> 785616806fcbf81d28d3a1b8482457554fbe3eea
