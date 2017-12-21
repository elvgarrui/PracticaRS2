from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Artista(models.Model):
    idArtista = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(null=True, blank=True)
    url = models.URLField(validators=[URLValidator()], null=True, blank=True)
    pictureUrl = models.URLField(validators=[URLValidator()], null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    
class Etiqueta():
    idTag = models.IntegerField(null=True, blank=True)
    tagValue = models.CharField(null=True, blank=True)
    def __unicode__(self):
        return self.tagValue
    