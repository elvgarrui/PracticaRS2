import csv
from datetime import time
import datetime

from django.core.management import call_command



def principal():

    call_command('flush',interactive=False)
    call_command('syncdb',interactive=False)

    with open(pathM) as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
               
    
       
if __name__ == '__main__':
    principal()