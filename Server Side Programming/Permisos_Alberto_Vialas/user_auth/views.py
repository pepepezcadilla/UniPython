# user_auth/views.py

from django.shortcuts import render, redirect
from .models import UserProfile, Actor
from .forms import PeliculaForm, ActorForm
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = UserProfile.objects.get(nombre=username, passw=password)
            request.session['user_id'] = user.id
            request.session['user_type'] = user.tipo
            
            return render(request, 'actoresypelis.html', {'user_type': user.tipo})
        except UserProfile.DoesNotExist:
            return render(request, 'index.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'index.html')

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            # Guardar la película en la base de datos
            form.save()
            return render(request, 'actoresypelis.html', {'user_type': 'admin'})
    else:
        form = PeliculaForm()

    return render(request, 'crearPelicula.html', {'form': form})

def crear_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'actoresypelis.html', {'user_type': 'admin'})
    else:
        form = ActorForm()

    return render(request, 'crearActor.html', {'form': form})

def actoresypelis(request):
    print("kasjhgdkjashdkjashd")
    actores = Actor.objects.all()
    print(actores)
    print(request.user)
    return render(request, 'actoresypelis.html', {'user_type': request.user.tipo, 'actores': actores})
