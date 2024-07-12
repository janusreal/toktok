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
                    
        inmuebles = get_inmuebles_comunas(filtro)

        archivo = open('data/resultados.txt','w', encoding='utf-8')
        for inmueble in inmuebles:
            linea = f'{inmueble.nombre}\t{inmueble. descripcion}\t{inmueble.comuna.nombre}\n'
            archivo.write(linea)
