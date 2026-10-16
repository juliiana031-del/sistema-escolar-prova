from django.contrib import admin
<<<<<<< HEAD
# ERRO ENCONTRADO: A função include não foi importada, o que causa um erro ao tentar incluir as urls do portal.
# CORREÇÃO: Adicionamos a importação da função include do módulo django.urls para que possamos incluir as urls do portal no arquivo urls.py principal.
from django.urls import include, path 


urlpatterns = [
    path('admin/', admin.site.urls),
  

   # ERRO ENCONTRADO: isso causa um erro ao tentar acessar a página inicial do portal, pois não há uma rota definida para ela.
   # CORREÇÃO: sem prefixo, a rota do portal será acessada diretamente pela raiz do site, permitindo que os usuários acessem a página inicial do portal sem precisar digitar um caminho adicional.
=======
# ERRO ENCONTRADO: (from django.urls import path). O arquivo 'sistema/urls.py' não possui a importação da função 'include'. A função 'include' é necessária para que o sistema consiga se conectar com o app portal
# CORREÇÃO: Adicionamos a importação da função 'include' para que o sistema consiga se conectar com o app portal
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
# ERRO ENCONTRADO: path('cadastro'/, preciso mostrar a pagina cadastro.html). Isso causa um erro ao tentar acessar a página inicial do portal. Pois não há uma rota definida para a página inicial do portal.    
# CORREÇÃO: Sem prefixo, as urls do app ficam na raiz do site. Com prefixo, as urls do app ficam dentro de uma pasta com o nome do app.
    path('', include('portal.urls')),
>>>>>>> 785616806fcbf81d28d3a1b8482457554fbe3eea
]
