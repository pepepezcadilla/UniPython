from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Videojuego, Consola, Empresa
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    videojuegos = Videojuego.objects.all().count()
    consolas = Consola.objects.all().count()

    user_can_add_plataforma = request.user.has_perm('main.add_plataforma')
    user_can_add_videojuego = request.user.has_perm('main.add_videojuego')

    context = {
        'cantidad_juegos': videojuegos,
        'cantidad_consolas': consolas,
        'user_can_add_plataforma': user_can_add_plataforma,
        'user_can_add_videojuego': user_can_add_videojuego,
        }

    return render(request, 'index.html', context)

class VideojuegoListView(ListView):
    model = Videojuego
    template_name = 'videojuego_list.html'  # Nombre de la plantilla para los detalles del videojuego
    context_object_name = 'videojuegos'  # Nombre del contexto en la plantilla

class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = 'videojuego_detail.html'  
    context_object_name = 'videojuego'  

class VideojuegoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Videojuego
    fields = '__all__'
    template_name = 'videojuego_form_create.html'
    permission_required = 'main.add_videojuego'

class VideojuegoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Videojuego
    fields = '__all__'
    template_name = 'videojuego_form_update.html'
    permission_required = 'main.change_videojuego'

class VideojuegoDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Videojuego
    success_url = reverse_lazy('videojuegos')
    template_name = 'videojuego_confirm_delete.html'
    permission_required = 'main.delete_videojuego'


def busqueda(request):
    if request.method == 'POST':
        buscado = request.POST.get('buscado')
        bus_videojuegos = Videojuego.objects.filter(titulo__contains = buscado)
        bus_consolas = Consola.objects.filter(nombre__contains = buscado)
        bus_empresas = Empresa.objects.filter(nombre__contains = buscado)

        context = {
            'buscado': buscado,
            'bus_videojuegos': bus_videojuegos,
            'bus_consolas': bus_consolas,
            'bus_empresas': bus_empresas,
            }
        return render(request, 'busqueda.html', context) 

    else:
        return render(request, 'busqueda.html', {}) 
    
