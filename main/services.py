from django.contrib.auth.models import User
from main.models import User, UserProfile, Inmueble, Comuna
from django.db.utils import IntegrityError
from django.db.models import Q
from django.db import connection
from django.contrib import messages

#funciones de usuario

def crear_inmueble_service(nombre, descripcion, direccion, mts_cons, mts_ttls, num_estacionamientos, num_banos, tipo_inmueble, precio_mensual, precio_ufs, comuna_cod, username):
    comuna = Comuna.objects.get(cod=comuna_cod)
    propietario = User.objects.get(username=username)
    
    inmueble = Inmueble(
        nombre=nombre,
        descripcion=descripcion,
        direccion=direccion,
        mts_cons=mts_cons,
        mts_ttls=mts_ttls,
        num_estacionamientos=num_estacionamientos,
        num_banos=num_banos,
        tipo_inmueble=tipo_inmueble,
        precio_mensual=precio_mensual,
        precio_ufs=precio_ufs,
        comuna=comuna,
        propietario=propietario
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

def crear_user(username,first_name,last_name, email, password,pass_confirm, direccion,telefono=None):
    
    if password != pass_confirm:
        return False, 'Las contraseñas no coinciden'
    
    try:
        user = User.objects.create_user(
            username, 
            email, 
            password, 
            first_name=first_name,
            last_name =last_name
            )
        
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

def get_inmuebles_comunas(filtro):
    if filtro is None:
        return Inmueble.objects.all().order_by('comuna')
    
    #return Inmueble.objects.filter(nombre__icontains=filtro).order_by('comuna')
    return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q(nombre__icontains=filtro)).order_by('comuna')


def get_inmuebles_regiones(filtro):

    query = "SELECT main_inmueble.nombre as nombre_inmueble,main_inmueble.nombre as descripcion_inmueble, main_region.nombre as region_nombre FROM main_inmueble JOIN main_comuna ON main_inmueble.comuna_id = main_comuna.cod JOIN main_region ON main_comuna.region_id = main_region.cod ORDER BY main_region.cod"
    
    if filtro is not None:
        query = f"SELECT main_inmueble.nombre as nombre_inmueble, main_inmueble.nombre as descripcion_inmueble,main_region.nombre as region_nombre FROM main_inmueble JOIN main_comuna ON main_inmueble.comuna_id = main_comuna.cod JOIN main_region ON main_comuna.region_id = main_region.cod where main_inmueble.nombre like '%{filtro}%' or main_inmueble.descripcion like '%{filtro}%' ORDER BY main_region.cod"
        
    cursor = connection.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    return registros

    #return Inmueble.objects.filter(nombre__icontains=filtro).order_by('region')
    
def editar_user_sin_password(username, first_name, last_name, email, direccion,rol,telefono=None):
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()
    
    user_profile = UserProfile.objects.get(user=user)
    user_profile.direccion = direccion
    user_profile.telefono = telefono
    user_profile.rol = rol
    user_profile.save()
    
def cambiar_password(req, password, repeat_password):
    if password != repeat_password:
        messages.error(req, 'No coinciden ambas contraseñas')
        return
    req.user.set_password(password)
    req.user.save()
    messages.success(req,'La contraseña ha sido actualizada')

