from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OficinaForm
from .models import Oficina


def home (request):
    template_name = 'geral/home.html'
    context = {}
    return render(request,template_name, context)
    


@login_required
def novaOficina(request):
    template_name = 'geral/nova_oficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.sucess(request, 'Oficina cadastrada com sucesso.')
            return redirect('geral:listaOficina')
    form = OficinaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def listaOficina(request):
    template_name = 'geral/listaOficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user) # select from oficina where usuario = usuario_da_sessao
    context = {
        'oficinas':oficinas,
    }
    return render(request, template_name, context)

