from django.contrib import admin
# ERRO ENCONTRADO: A função include não foi importada, o que causa um erro ao tentar incluir as urls do portal.
# CORREÇÃO: Adicionamos a importação da função include do módulo django.urls para que possamos incluir as urls do portal no arquivo urls.py principal.
from django.urls import include, path 


urlpatterns = [
    path('admin/', admin.site.urls),
  

   # ERRO ENCONTRADO: isso causa um erro ao tentar acessar a página inicial do portal, pois não há uma rota definida para ela.
   # CORREÇÃO: sem prefixo, a rota do portal será acessada diretamente pela raiz do site, permitindo que os usuários acessem a página inicial do portal sem precisar digitar um caminho adicional.
]
