from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.services import editar_user_sin_password
from django.contrib.auth import authenticate, login
from main.forms import FormularioAutenticacionPersonalizado
from main.services import cambiar_password


# Create your views here.

@login_required
def home(req):
    return render(req, 'home.html')


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
            req.POST['telefono']
        )
    else:
        editar_user_sin_password(
            current_user.username,
            req.POST['first_name'],
            req.POST['last_name'],
            req.POST['email'],
            req.POST['direccion']
        )
        messages.success(req, 'Ha actualizado sus datos con éxito')
        return redirect('/')
        
        
def change_password(req):
    password = req.POST['password']
    repeat_password = req.POST['password_repeat']
    cambiar_password(req,password,repeat_password)
    return redirect('/accounts/profile')

#req es el objeto que representa la solicitud

def solo_arrendadores(req):
    return HttpResponse('Sólo arrendadores')

def solo_arrendatarios(req):
    return HttpResponse('Sólo arrendatarios')

