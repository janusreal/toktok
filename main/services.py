from main.models import *

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
        disponible=disponible, 
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

def crear_user(rut, first_name, last_name, email,password,direccion,telefono ):
    user = User.objects.create_user(
        username = rut,
        first_name = first_name,
        last_name = last_name,
        email = email,
        password=password
    )
    UserProfile.objects.create(
        direccion = direccion,
        telefono = telefono,
        user = user
    )
    

def editar_user(rut, first_name, last_name, email,password,direccion,telefono):
    user = User.objects(user_id=user_id)
    #actualizo cada campo de la instancia
    user.username = rut
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = password
    user.direccion = direccion
    user.telefono = telefono
    
    user.save()
    return user

