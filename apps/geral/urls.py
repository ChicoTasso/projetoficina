from django.urls import path

app_name = 'geral'

from . import views

urlpatterns = [

    path('nova-oficina/', views.novaOficina, name='novaOficina'),
    path('oficinas/', views.listaOficina, name='listaOficina'),
    path('deletar/<int:pk>',views.deletarOficina, name='deletarOficina'),
    path('editar/<int:pk>', views.editarOficina, name='editarOficina'),
    path('novo-mecanico/', views.novaOficina, name='novoMecanico'),
    path('mecanicos/', views.listaMecanico, name='listaMecanico'),
    path('deletar/<int:pk>',views.deletarMecanico, name='deletarMecanico'),
    path('editar/<int:pk>', views.editarMecanico, name='editarMecanico'),
    path('', views.home, name='home'),

]