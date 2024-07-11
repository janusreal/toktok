from django.contrib.auth.models import User
from main.models import *
from django.db.utils import IntegrityError

#funciones de usuario

def crear_inmueble(nombre,descripcion, direccion,  mts_cons, mts_ttls,  num_estacionamientos,num_banos,tipo_inmueble,precio_mensual, precio_ufs,comuna_cod, username):
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion, 
        direccion=direccion, 
        mts_cons=mts_cons,
        mts_ttls=mts_ttls, 
        num_estacionamientos=num_estacionamientos,
        num_banos = num_banos,
        tipo_inmueble = tipo_inmueble,
        precio_mensual=precio_mensual, 
        precio_ufs = precio_ufs,
        comuna=Comuna.objects.get(cod=comuna_cod),
        propietario = User.objects.get(username=username)
        )

    inmueble.save()
    return inmueble

def actualizar_inmueble(inmueble_id, nombre,descripcion, direccion,  mts_cons, mts_ttls,  num_estacionamientos,num_banos,tipo_inmueble,precio_mensual, precio_ufs,comuna):
    inmu = Inmueble.objects.get(id=inmueble_id)
    comuna = Comuna.objects.get(nombre=comuna)
    inmu.nombre=nombre
    inmu.descripcion=descripcion 
    inmu.direccion=direccion 
    inmu.mts_cons=mts_cons
    inmu.mts_ttls=mts_ttls 
    inmu.num_estacionamientos=num_estacionamientos 
    inmu.num_banos=num_banos 
    inmu.tipo_inmueble = tipo_inmueble
    inmu.precio_mensual=precio_mensual
    inmu.precio_ufs=precio_ufs
    inmu.comuna = comuna
    
    inmu.save()
    return inmu

def eliminar_inmueble(inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.delete()

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

