from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import login
from main.forms import FormularioAutenticacionPersonalizado
from main.models import Inmueble, Region, Comuna
from main.services import editar_user_sin_password, cambiar_password, crear_inmueble as crear_inmueble_service


@login_required
def home(req):
    return render(req, 'home.html')

def formInmueble():
    pass

def login_view(req):
    if req.method == 'POST':
        form = FormularioAutenticacionPersonalizado(req,data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            return redirect('/')
    else:
        form = FormularioAutenticacionPersonalizado()
        
    return render(req,'login.html',{'form':form})


#funcion profile para autentificados
@login_required
def profile(req):
    return render(req, 'profile.html')

@login_required
def edit_user(req):
    current_user = req.user
    if req.POST['telefono'] != '':
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['telefono'],
            req.POST['rol']
        )
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion'],
            req.POST['rol']
        )
    messages.success(req, 'Ha actualizado sus datos con éxito')
    return redirect('/accounts/profile')
        
        
def change_password(req):
    password = req.POST['password']
    repeat_password = req.POST['password_repeat']
    cambiar_password(req,password,repeat_password)
    return redirect('/accounts/profile')


@login_required
def create_inmueble(req):
    
    if req.method == 'POST':
        nombre=req.POST.get('nombre')
        descripcion=req.POST.get('descripcion')
        direccion=req.POST.get('direccion')
        mts_cons=req.POST.get('mts_cons')
        mts_ttls=req.POST.get('mts_ttls')
        num_estacionamientos=req.POST.get('num_estacionamientos')
        num_habitaciones=req.POST.get('num_habitaciones')
        num_banos=req.POST.get('num_banos')
        tipo_inmueble=req.POST.get('tipo_inmueble')
        precio_mensual=req.POST.get('precio_mensual')
        precio_ufs=req.POST.get('precio_ufs')
        comuna_cod=req.POST.get('comuna')
        propietario=req.POST.get('propietario')
        
        inmueble = Inmueble(
            nombre=nombre,
            descripcion=descripcion,
            direccion=direccion,
            mts_cons=mts_cons,
            mts_ttls=mts_ttls,
            num_estacionamientos=num_estacionamientos,
            num_habitaciones=num_habitaciones,
            num_banos=num_banos,
            tipo_inmueble=tipo_inmueble,
            precio_mensual=precio_mensual,
            precio_ufs=precio_ufs,
            comuna=comuna_cod,
            propietario=propietario)
        inmueble.save()
        return redirect('profile')
    return render(req,'crear_inmueble.html')


#req es el objeto que representa la solicitud

def solo_arrendadores(req):
    return HttpResponse('Sólo arrendadores')

def solo_arrendatarios(req):
    return HttpResponse('Sólo arrendatarios')

def filtrar_arrendador(user):
    if user.usuario.rol == 'arrendador' or user.is_staff == True:
        return True
    else:
        return False

@user_passes_test(filtrar_arrendador)
def nuevo_inmueble(req):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    #Inmueble refiere al modelo que tiene tipos de inmueble
    context = {
        'tipos_inmueble': Inmueble.tipos,
        'regiones':regiones,
        'comunas':comunas
    }
    return render(req,'nuevo_inmueble.html',context)



@user_passes_test(solo_arrendadores)
def crear_inmueble(req):
    #obtenemos el rut del logueado
    propietario_rut = req.user.username
    crear_inmueble_service(
            req.POST['nombre'],
            req.POST['descripcion'],
            req.POST['direccion'],
            int(req.POST['mts_cons']),
            int(req.POST['mts_ttls']),
            int(req.POST['num_estacionamientos']),
            int(req.POST['num_habitaciones']),
            int(req.POST['num_banos']),
            req.POST['tipo_inmueble'],
            int(req.POST['precio_mensual']),
            int(req.POST['precio_ufs']),
            req.POST['comuna_cod'],
            propietario_rut
            )
    messages.success(req, 'Nuevo inmueble agregado')
    return redirect('/accounts/profile')


