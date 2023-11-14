from .models import Videojuego


def contar_visitas(request):
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1

    context = {
        'num_visitas':num_visitas
    }

    return context

def ultima_pelicula(request):
    ult_juego = Videojuego.objects.all().latest('id')
    pri_juego = Videojuego.objects.all().earliest('id')

    return {
        'ult_juego': ult_juego,
        'pri_juego': pri_juego,
    }