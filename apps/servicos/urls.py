from django.urls import path

app_name = 'servicos'

from . import views

urlpatterns = [

    path('novo-servico/', views.novoServico, name='novoServico'),
    path('servicos/', views.listaServico, name='listaServico'),
    path('deletar/<int:pk>/',views.deletarServico, name='deletarServico'),
    path('editar/<int:pk>/', views.editarServico, name='editarServico'),
    path('', views.home, name='home'),
]