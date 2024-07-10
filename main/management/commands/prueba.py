from typing import Any
from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        
        #crear_user('8888-1','Alejandro','Martinez','email@email.com','milenio','milenio','calle larga 1', '23561882')
              
        #crear_inmueble('Casa espaciosa','Hermosa casa con patio', 'Lolco 2367','120','400','5','2','Casa','500000',13.30,'Las Condes','8888-1')
        
        #editar_user('8888-1','Ale','Martinez','emilio@email.com','sigiloso','calle larga 250', '23561882')
        
        #actualizar_inmueble(1,'Casa espaciosa','Hermosa casa con patio', 'Lolco 2367',120,'400','5','2','Casa','500000',13.30,'Huechuraba')
        
        eliminar_inmueble(1)