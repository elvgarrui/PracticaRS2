#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.forms import SearchForm
from main.models import *
from populate import populateBBDD

import operator

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

def masEscuchas(request):
    escuchas={} #Reproducciones de artistas
    ua = UsuarioArtista.objects.all()
    for row in ua:
        artista = int(row.artista.id)
        weight = row.tiempoEscucha
        if artista in escuchas:
            aux=escuchas[artista]
            escuchas[artista] = weight+aux
        else:  
            escuchas[artista] = weight
    
    artistas=[]
#     print sorted(escuchas.values())
    for i in range(3):
        masE= max(escuchas.iteritems(), key=operator.itemgetter(1))[0]
        artistas.append(Artista.objects.get(idArtista=masE))
        del escuchas[masE]
#     artistas = Artista.objects.all()
    
    return render_to_response('mas_escuchados.html',{'artistas':artistas})
