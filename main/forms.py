from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from main.models import Inmueble



class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        exclude = []

        