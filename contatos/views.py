from django.shortcuts import render, get_object_or_404
from .models import contato
from django.http import Http404
from django.core.paginator  import Paginator
from django.db.models import Q,Value
from django.db.models.functions import Concat
# Create your views here.

def index(resquest):
    contatos = contato.objects.order_by('-id')
    paginator = Paginator(contatos, 2) # Show 25 contacts per page.

    page = resquest.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(resquest, 'contatos/index.html',{
        'contatos':contatos
    })
    
def ver_contato(request,contato_id):
    # contato1 = contato.objects.get(id=contato_id)
    contato1 = get_object_or_404(contato,id=contato_id)
    
    if not contato.mostra:
        raise Http404()
    return render(request, 'contatos/ver_contatos.html',{
    'contato':contato1
    })

# def ver_contato(request,contato_id):
#     try:
#         contato1 = contato.objects.get(id=contato_id)
#         return render(request, 'contatos/ver_contatos.html',{
#         'contato':contato1
#         })
#     except contato.DoesNotExist as e:
#         raise Http404()


def busca(resquest):

    termo = resquest.GET.get('termo')
    if termo is None or not  termo:
        raise Http404()    
    campos = Concat('nome',Value(' '),'sobrenome')
    contatos = contato.objects.annotate(
        nome_completo = campos
        ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo)
    )
        
    
    paginator = Paginator(contatos, 2) # Show 25 contacts per page.

    page = resquest.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(resquest, 'contatos/busca.html',{
        'contatos':contatos
    })