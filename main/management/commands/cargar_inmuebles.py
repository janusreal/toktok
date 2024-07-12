from django.core.management.base import BaseCommand
import csv
from main.services import crear_inmueble
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        archivo = open('data/inmuebles.csv',encoding="utf-8")
        reader = csv.reader(archivo,delimiter=';')
        next(reader)

        for fila in reader:
            try:
                crear_inmueble(
                    nombre=fila[0],
                    descripcion=fila[1],
                    direccion=fila[2],
                    mts_cons=fila[3],
                    mts_ttls=fila[4],
                    num_estacionamientos= fila[5],
                    num_banos=fila[6],
                    tipo_inmueble=fila[7],
                    precio_mensual=fila[8],
                    precio_ufs=fila[9],
                    comuna_cod=fila[10],
                    username=fila[11]
                    )
            except User.DoesNotExist:
                print('Falló usuario '.fila[11])