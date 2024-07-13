import csv
import os
from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        #positional arguments
        parser.add_argument('-f', '--f', type=str, nargs='+',)        

    def handle(self, *args, **kwargs):
        
        filtro = None
        if 'f' in kwargs.keys() and kwargs['f'] is not None:
            filtro = kwargs['f'][0]
                    
        inmuebles = get_inmuebles_regiones(filtro)

        archivo = open('data/results_regiones.txt','w', encoding='utf-8')
        for inmueble in inmuebles:
            linea = f'{inmueble[0]}\t{inmueble[1]}\t{inmueble[2]}\n'
            archivo.write(linea)
            
            '''
            region_nombre = getattr(inmueble, 'region_nombre','Nombre de region no disponible')
            linea = f'{inmueble.nombre}\t{inmueble.descripcion}\t{region_nombre}\n'
            archivo.write(linea+"\n")
        archivo.close()
'''