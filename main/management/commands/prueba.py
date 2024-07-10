from typing import Any
from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        '''
        crear_user('8888-1','Alejandro','Martinez','email@email.com','milenio','milenio','calle larga 1', '23561882')
        
      
        crear_inmueble('Casa en Las Condes','Espaciosa casa con patio trasero','Pocuro 123','Las Condes','60','240','500000','2','5','2','')  '''
        
        editar_user('8888-1','Ale','Martinez','emilio@email.com','sigiloso','calle larga 250', '23561882')