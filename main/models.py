from django.core.validators import URLValidator
from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Artista(models.Model):
    idArtista = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(null=True, blank=True, max_length=50)
    url = models.URLField(validators=[URLValidator()], null=True, blank=True)
    pictureUrl = models.URLField(validators=[URLValidator()], null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    
    def reproducciones(self):
        res = 0
        ua = UsuarioArtista.objects.all()
        for row in ua:
            artista = int(row.artista.id)
            weight = row.tiempoEscucha
            if artista==self.idArtista:
                res += weight
        return res
    
    reproducciones = property(reproducciones)
    
class Etiqueta(models.Model):
    idTag = models.IntegerField(null=True, blank=True)
    tagValue = models.CharField(null=True, blank=True, max_length=50)
    def __unicode__(self):
        return self.tagValue

class UsuarioArtista(models.Model):
    usuarioId = models.IntegerField(null=False, blank=False)
    artista = models.ForeignKey(Artista)
    tiempoEscucha = models.IntegerField(null=False, blank=False)
    def __unicode__(self):
        return self.tiempoEscucha

class UsuarioEtiquetaArtista(models.Model):
    usuarioId = models.IntegerField(null=False, blank=False)
    artista = models.ForeignKey(Artista)
    tag = models.ForeignKey(Etiqueta)
    fecha = models.DateField(null=False, blank=False)
    def __unicode__(self):
        return self.usuarioId

class UsuarioAmigo(models.Model):
    usuarioId = models.IntegerField(null=False, blank=False)
    amigoId = models.IntegerField(null=False, blank=False)
    def __unicode__(self):
        return self.usuarioId
    