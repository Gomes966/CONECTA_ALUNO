from django.shortcuts import render, get_object_or_404, redirect
from .models import Servico
from .forms import ServicoForm
from django.contrib.auth.decorators import login_required


def home(request):

    pesquisa = request.GET.get('q')
    categoria = request.GET.get('categoria')

    servicos = Servico.objects.all()

    if pesquisa:
        servicos = servicos.filter(
            titulo__icontains=pesquisa
        )

    if categoria:
        servicos = servicos.filter(
            categoria=categoria
        )

    contexto = {
        'servicos': servicos,
        'total_servicos': servicos.count()
    }

    return render(request, 'core/home.html', contexto)


def detalhe_servico(request, servico_id):

    servico = get_object_or_404(Servico, id=servico_id)

    contexto = {
        'servico': servico
    }

    return render(request, 'core/detalhe_servico.html', contexto)


def sobre(request):
    return render(request, 'core/sobre.html')


def contato(request):
    return render(request, 'core/contato.html')

@login_required
def cadastrar_servico(request):

    if request.method == 'POST':

        form = ServicoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = ServicoForm()

    contexto = {
        'form': form
    }

    return render(
        request,
        'core/cadastrar_servico.html',
        contexto
    )