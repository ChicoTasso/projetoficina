from django.urls import path

app_name = 'geral'

from . import views

urlpatterns = [

    path('nova-oficina/', views.novaOficina, name='novaOficina'),
    path('oficinas/', views.listaOficina, name='listaOficina'),
    path('', views.home, name='home'),

]