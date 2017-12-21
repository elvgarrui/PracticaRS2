import csv
from datetime import time
import datetime

from django.core.management import call_command

from main.models import Artista


artistF = "carga/artists.dat"
tagF = "carga/tags.dat"
usartF = "carga/user_artists.dat"
UsfriF = "carga/user_friends.dat"
UstagF = "carga/user_taggedartists.dat"


def principal():

#    call_command('flush',interactive=False)
#    call_command('syncdb',interactive=False)

    with open(artistF) as f:
        reader = csv.reader(f,delimiter="|")
        for row in reader:
            print Artista.objects.get_or_create(idArtista=row[0],nombre=row[1],
                                          url=row[2], pictureUrl=row[3])
        

    
       
if __name__ == '__main__':
    principal()