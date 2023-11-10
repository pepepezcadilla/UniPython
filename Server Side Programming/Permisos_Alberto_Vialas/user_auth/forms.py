# user_auth/forms.py

from django import forms
from .models import Pelicula, Actor

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'año']

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombre', 'peliculas']
        widgets = {
            'peliculas': forms.CheckboxSelectMultiple,
        }