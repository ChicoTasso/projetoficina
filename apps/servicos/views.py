from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ServicoForm
from .models import Servico, Oficina

    

@login_required
def home (request):
    template_name = 'servicos/home.html'
    context = {}
    return render(request,template_name, context)

@login_required
def novoServico(request):
    template_name = 'servicos/novoServico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        oficina = get_object_or_404(Oficina, usuario=request.user)
        if form.is_valid():
            sf = form.save(commit=False)
            sf.oficina = oficina
            sf.save()
            messages.success(request, 'Serviço adicionado com sucesso')
            return redirect('servicos:listaServicos')    
    form = ServicoForm()
    context['form'] = form
    return render(request, template_name, context)



@login_required
def listaServico(request):
    template_name = 'servicos/listaServico.html'

    oficina = get_object_or_404(usuario = request.user)
    servicos = Servico.objects.filter(oficina = oficina)
    context = {
        'servicos':servicos,
    }
    return render(request, template_name, context)

@login_required
def deletarServico(request, pk):
    oficina = Servico.objects.get(pk=pk)
    oficina.delete()
    messages.info(request, 'Serviço deletado')
    return redirect('servicos:listaServico')

@login_required
def editarServico(request, pk):
    template_name = 'servicos/novoServico.html'
    context = {}
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(data=request.POST, instance=servico)
        form.save()
        messages.success(request, 'Serviço editada com sucesso.')
        return redirect('servicos:listaServico')
    form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)
