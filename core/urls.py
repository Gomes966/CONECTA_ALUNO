from django.urls import path
from .views import home, detalhe_servico, sobre, contato, cadastrar_servico

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('servico/<int:servico_id>/', detalhe_servico, name='detalhe_servico'),
    path('cadastrar-servico/', cadastrar_servico, name='cadastrar_servico')
    
]