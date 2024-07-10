from django.contrib.auth.models import User
from main.models import *
from django.db.utils import IntegrityError
#funciones de usuario

def crear_inmueble(nombre,descripcion, direccion, comuna, mts_cuadrados, mts_totales, precio_mensual, cant_estacionamientos, cant_habitaciones, cant_banos, disponible, eliminado, arrendatario_rut):
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion, 
        direccion=direccion, 
        comuna=comuna,
        mts_cuadrados=mts_cuadrados,
        mts_totales=mts_totales, 
        precio_mensual=precio_mensual, 
        cant_estacionamientos=cant_estacionamientos, 
        cant_habitaciones=cant_habitaciones, 
        cant_banos=cant_banos, 
        eliminado=eliminado, 
        arrendatario=arrendatario_rut 
        )

    inmueble.save()
    return inmueble

def actualizar_inmueble(inmueble_id, nombre,descripcion, direccion, comuna, mts_cuadrados, mts_totales, precio_mensual, cant_estacionamientos, cant_habitaciones, cant_banos, disponible, eliminado):
    inmu = Inmueble.objects(id=inmueble_id)
    inmu.nombre=nombre,
    inmu.descripcion=descripcion, 
    inmu.direccion=direccion, 
    inmu.comuna=comuna,
    inmu.mts_cuadrados=mts_cuadrados,
    inmu.mts_totales=mts_totales, 
    inmu.precio_mensual=precio_mensual, 
    inmu.cant_estacionamientos=cant_estacionamientos, 
    inmu.cant_habitaciones=cant_habitaciones, 
    inmu.cant_banos=cant_banos, 
    inmu.disponible=disponible, 
    inmu.eliminado=eliminado
    
    inmu.save()
    return inmu

def eliminar_inmueble(inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.eliminado = True
    inmueble.save()

def crear_user(username, first_name, last_name, email,password, pass_confirm, direccion,telefono=None ):
    if password != pass_confirm:
        return False, 'Las contraseñas no coinciden'
    try:
        user = User.objects.create_user(username, email, password, first_name=first_name,last_name =last_name)
    except IntegrityError:
        return False, 'RUT duplicado'
    
    UserProfile.objects.create(
        user = user,
        direccion = direccion,
        telefono = telefono        
    )
    return True
    

def editar_user(username, first_name, last_name, email,password, direccion,telefono=None):
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    user.save()
    
    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.save()

