from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OficinaForm
from .models import Oficina
from django.views.generic import UpdateView


@login_required
def home (request):
    template_name = 'geral/home.html'
    context = {}
    return render(request,template_name, context)
    


@login_required
def novaOficina(request):
    template_name = 'geral/novaOficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.success(request, 'Oficina cadastrada com sucesso.')
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

@login_required
def deletarOficina(request, pk):
    oficina = Oficina.objects.get(pk=pk)
    oficina.delete()
    messages.info(request, 'Oficina deletada')
    return redirect('geral:listaOficina')

@login_required
def editarOficina(request, pk):
    template_name = 'geral/novaOficina.html'
    context = {}
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=oficina)
        form.save()
        messages.success(request, 'Oficina editada com sucesso.')
        return redirect('geral:listaOficina')
    form = OficinaForm(instance=oficina)
    context['form'] = form
    return render(request, template_name, context)

# def atualizar(request, id):
#     autor = Autor.objects.get(id=id)
#     form = AutorForm(instance=autor)
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES, instance=autor)
#         if form.is_valid():
#             form.save()
#             return redirect("atualizar", id=id)
#         else:
#             return render(request, 'atualizar.html', {'form': form})
#     else:
#          return render(request, 'atualizar.html', {'form': form})

    



