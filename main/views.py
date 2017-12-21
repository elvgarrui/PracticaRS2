#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.forms import SearchForm
from main.models import *
from populate import populateBBDD


def inicio(request):
    return render_to_response('inicio.html')

def populateDB(request):
    populateBBDD()
    return render_to_response('populate.html')

# Create your views here.
def buscarPorUsuario(request):
    if request.method == 'POST':
        formulario = SearchForm(request.POST)
        if formulario.is_valid():
            usuarioArtista = UsuarioArtista.objects.filter(usuarioId=formulario.cleaned_data['usuarioId'])
            return render_to_response('lista_artistas.html',{'artistas':usuarioArtista})
    else:
        formulario = SearchForm()
    return render_to_response('search.html',{'formulario':formulario}, context_instance=RequestContext(request))

# def masEscuchas(request):
#     