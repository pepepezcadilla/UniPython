from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Procesar el inicio de sesión si es válido
            # Por ejemplo, redirigir a una página de éxito
        #else:
            # Si hay errores en el formulario, renderizar la plantilla con el formulario y los mensajes de error
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

