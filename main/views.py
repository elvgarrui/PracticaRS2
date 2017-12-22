#encoding:utf-8
import shelve
from django.shortcuts import render_to_response
from django.template import RequestContext

from main.forms import SearchForm
from main.models import *
from populate import populateBBDD

import operator
from pattern.text.en.wordnet.pywordnet.wordnet import Dictionary

Caract={}   # matriz de usuarios y puntuaciones a cada a items
Tpa = {}   

ItemsPrefs={}   # matriz de items y puntuaciones de cada usuario. Inversa de Prefs
SimItems=[]  # matriz de similitudes entre los items

def loadDict():
    loadCaract()
    loadPrefs()


def frequentTags(user):    
    print "foo"



def loadPrefs():
    shelf = shelve.open("dataRS.dat")
    shelf.close()    


def loadCaract():
    shelf = shelve.open("dataRS.dat")
    ueas = UsuarioEtiquetaArtista.objects.all()
    for uea in ueas:
        artist = int(uea.artista.idArtista)
        if artist not in Caract:
            Caract.setdefault(artist, {})

        tag = int(uea.tag.idTag)
        if tag not in Caract[artist]:
            Caract[artist][tag] = 1
        else:
            Caract[artist][tag]+= 1
            
    print Caract
    for artist in Caract:
        tags= Caract.get(artist)
        sortedtag = sorted(tags, key=tags.get, reverse=True)
        top = sortedtag[0:4]
        Tpa[artist]=top
#         print top
#         for tag in top:
#             print tags[tag]
    
    print Tpa
    shelf['Tpa'] = Tpa            
    shelf.close()

def inicio(request):
    return render_to_response('inicio.html')


def populateDB(request):
    populateBBDD()
    return render_to_response('populate.html')


def loadRS(request):
    loadDict()
    return render_to_response('loadRS.html')


def descubre(request):
    return render_to_response('descubre.html')


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


if __name__ == '__main__':
    loadDict()
