from tkinter import *
from tkinter.ttk import *
from time import strftime
import tkinter as tk
import random
import time
from tkinter import *
from PIL import Image, ImageTk
from time import strftime


# Funcion para la hora del reloj digital
def reloj_digital():
    etiqueta_hm.config(text=strftime("%H:%M"))
    etiqueta_s.config(text=strftime("%S"))
    etiqueta_fecha.config(text=strftime("%A, %d/%m/%Y"))

    if cb[0] == 100:
        boton_cargador.config(fg="yellow")

    cargar_bateria()

    etiqueta_s.after(1000, reloj_digital)


# FUNCION DE BLUETOOTH
def bluetooth():
    contador_blue = [0]

    # Creamos la lista de dispositivos móviles cercanos
    devices = ["iPhone de Esteban", "iPhone de Carolina", "iPhone de Alberto", "iPhone de Luismi"]

    # Creamos la lista de dispositivos cercanos en la interfaz
    listbox = tk.Listbox(frame_raiz, width=30, height=6)
    for device in devices:
        listbox.insert(tk.END, device)
    listbox.place(x=40, y=100)

    # Función que se ejecuta al pulsar el botón "Enlazar"
    def enlazar():
        if contador_blue[0] == 0:
            # Obtenemos el elemento seleccionado de la lista
            seleccionado = listbox.get(tk.ACTIVE)

            mensaje_conectado = Label(app, background="white",
                                      text="Conectado a {} correctamente !!".format(seleccionado))
            mensaje_conectado.place(x=250, y=400)
            contador_blue[0] = 1

            # nuevo boton
            button.destroy()

            def borrarblue():
                listbox.destroy()
                mensaje_conectado.destroy()
                button_continuar.destroy()
                luz()

            button_continuar = tk.Button(app, text="Continuar", command=borrarblue)
            button_continuar.place(x=350, y=450)

    # Configuramos el botón de enlazar
    # button = tk.Button(app, text="Enlazar", command=enlazar)
    boton_pulsado_blue = tk.BooleanVar()
    boton_pulsado_blue.set(False)
    button = tk.Button(frame_raiz, text="Enlazar",
                       font=("Arial", 12), command=lambda: boton_pulsado_blue.set(True))
    button.place(x=40, y=210)
    button.wait_variable(boton_pulsado_blue)

    listbox.destroy()
    button.destroy()


def preguntas():
    phone = tk.Toplevel()
    phone.geometry("250x480")
    phone.configure(bg="white")
    phone.title("Iphone")
    phone.iconbitmap("logo_apple.ico")

    imagen_iphone = PhotoImage(file="iphone_8_recortado.png")
    label_imagen_iphone = Label(phone, image=imagen_iphone, background="white")
    label_imagen_iphone.place(x=0, y=0)

    frame_phone = Frame(phone)
    frame_phone.place(x=30, y=62)
    frame_phone.config(bg="black")
    frame_phone.config(width=200, height=357)

    diccionario_preguntas = {
        "nombre": "A",
        "apellidos": "B",
        "año de nacimiento": "C",
        "altura": "D",
        "peso": "E",
        "localizacion": "F",
        "actividades": "G",
        "deportes": "H"
    }

    def guardar_contenido():
        valido = True
        lista_contenido = ["0", "1", "2", "3", "4", "5", "6", "7"]

        # Nombre
        if nombre_input.get() == "":
            valido_nombre = False
            valido = False
        else:
            valido_nombre = True
            lista_contenido[0] = nombre_input.get()

        # Apellido
        if apellido_input.get() == "":
            valido_apellido = False
            valido = False
        else:
            valido_apellido = True
            lista_contenido[1] = apellido_input.get()

        # Nacimiento
        try:
            if nacimiento_input.get() == "":
                valido_nacimiento = False
                valido = False
            else:
                valido_nacimiento = True
                lista_contenido[2] = int(nacimiento_input.get())
        except ValueError:
            valido_nacimiento = False
            valido = False
        # Altura
        try:
            if altura_input.get() == "":
                valido_altura = False
                valido = False
            else:
                valido_altura = True
                lista_contenido[3] = int(altura_input.get())
        except ValueError:
            valido_altura = False
            valido = False

        # Peso
        try:
            if peso_input.get() == "":
                valido_peso = False
                valido = False
            else:
                valido_peso = True
                lista_contenido[4] = int(peso_input.get())
        except ValueError:
            valido_peso = False
            valido = False

        # Localizacion
        if localizacion_input.get() == "":
            valido_localizacion = False
            valido = False
        else:
            valido_localizacion = True
            lista_contenido[5] = localizacion_input.get()

        # Actividades
        if actividades_input.get() == "":
            valido_actividades = False
            valido = False
        else:
            valido_actividades = True
            lista_contenido[6] = actividades_input.get()

        # Deportes
        if deportes_input.get() == "":
            valido_deportes = False
            valido = False
        else:
            valido_deportes = True
            lista_contenido[7] = deportes_input.get()

        if valido is False:  # Hay una o mas condiciones no validas

            if valido_nombre is True:  # Nombre valido
                nombre_label_1 = tk.Label(frame_phone, text="Nombre:", bg="black", foreground="white")
                nombre_label_1.place(x=40, y=0)
            elif valido_nombre is False:  # Nombre no valido
                nombre_label_1 = tk.Label(frame_phone, text="Nombre:", bg="black", foreground="red")
                nombre_label_1.place(x=40, y=0)

            if valido_apellido is True:  # Apellido valido
                apellido_label_1 = tk.Label(frame_phone, text="Apellidos:", bg="black", foreground="white")
                apellido_label_1.place(x=40, y=40)
            elif valido_apellido is False:  # Apellido no valido
                apellido_label_1 = tk.Label(frame_phone, text="Apellidos:", bg="black", foreground="red")
                apellido_label_1.place(x=40, y=40)

            if valido_nacimiento is True:  # Nacimiento valida
                nacimiento_label_1 = tk.Label(frame_phone, text="Año de nacimiento:", bg="black", foreground="white")
                nacimiento_label_1.place(x=40, y=80)
            elif valido_nacimiento is False:  # Nacimiento no valida
                nacimiento_label_1 = tk.Label(frame_phone, text="Año de nacimiento:", bg="black", foreground="red")
                nacimiento_label_1.place(x=40, y=80)

            if valido_altura is True:  # Altura valida
                altura_label_1 = tk.Label(frame_phone, text="Altura:", bg="black", foreground="white")
                altura_label_1.place(x=40, y=120)
            elif valido_altura is False:  # Altura no valida
                altura_label_1 = tk.Label(frame_phone, text="Altura:", bg="black", foreground="red")
                altura_label_1.place(x=40, y=120)

            if valido_peso is True:  # Peso valido
                peso_label_1 = tk.Label(frame_phone, text="Peso:", bg="black", foreground="white")
                peso_label_1.place(x=40, y=160)
            elif valido_peso is False:  # Peso no valido
                peso_label_1 = tk.Label(frame_phone, text="Peso:", bg="black", foreground="red")
                peso_label_1.place(x=40, y=160)

            if valido_localizacion is True:  # Localizacion valida
                localizacion_label_1 = tk.Label(frame_phone, text="Localización:", bg="black", foreground="white")
                localizacion_label_1.place(x=40, y=200)
            elif valido_localizacion is False:  # Localizacion no valida
                localizacion_label_1 = tk.Label(frame_phone, text="Localización:", bg="black", foreground="red")
                localizacion_label_1.place(x=40, y=200)

            if valido_actividades is True:  # Actividades valida
                actividades_label_1 = tk.Label(frame_phone, text="Nº de actividades semanales:", bg="black",
                                               foreground="white")
                actividades_label_1.place(x=40, y=240)
            elif valido_actividades is False:  # Actividades no valida
                actividades_label_1 = tk.Label(frame_phone, text="Nº de actividades semanales:", bg="black",
                                               foreground="red")
                actividades_label_1.place(x=40, y=240)

            if valido_deportes is True:  # Deportes valido
                deportes_label_1 = tk.Label(frame_phone, text="Deportes favoritos:", bg="black", foreground="white")
                deportes_label_1.place(x=40, y=280)
            elif valido_deportes is False:  # Deportes no valido
                deportes_label_1 = tk.Label(frame_phone, text="Deportes favoritos:", bg="black", foreground="red")
                deportes_label_1.place(x=40, y=280)

        else:  # Ya estan todos los datos introducidos de forma correcta
            phone.destroy()
            contador_for = 0
            # Si quereis poner la base de datos quitar este for y poner lo necesario para que se guarde en la base de datos
            for key in diccionario_preguntas:
                diccionario_preguntas[key] = lista_contenido[contador_for]
                contador_for += 1

    # A continuacion estan las 8 preguntas con sus label e inputs

    nombre_label = tk.Label(frame_phone, text="Nombre:", bg="black", foreground="white")
    nombre_input = tk.Entry(frame_phone)
    nombre_label.place(x=40, y=0)
    nombre_input.place(x=40, y=20)

    apellido_label = tk.Label(frame_phone, text="Apellidos:", bg="black", foreground="white")
    apellido_input = tk.Entry(frame_phone)
    apellido_label.place(x=40, y=40)
    apellido_input.place(x=40, y=60)

    nacimiento_label = tk.Label(frame_phone, text="Año de nacimiento:", bg="black", foreground="white")
    nacimiento_input = tk.Entry(frame_phone)
    nacimiento_label.place(x=40, y=80)
    nacimiento_input.place(x=40, y=100)

    altura_label = tk.Label(frame_phone, text="Altura:", bg="black", foreground="white")
    altura_input = tk.Entry(frame_phone)
    altura_label.place(x=40, y=120)
    altura_input.place(x=40, y=140)

    peso_label = tk.Label(frame_phone, text="Peso:", bg="black", foreground="white")
    peso_input = tk.Entry(frame_phone)
    peso_label.place(x=40, y=160)
    peso_input.place(x=40, y=180)

    localizacion_label = tk.Label(frame_phone, text="Localización:", bg="black", foreground="white")
    localizacion_input = tk.Entry(frame_phone)
    localizacion_label.place(x=40, y=200)
    localizacion_input.place(x=40, y=220)

    actividades_label = tk.Label(frame_phone, text="Nº de actividades semanales:", bg="black", foreground="white")
    actividades_input = tk.Entry(frame_phone)
    actividades_label.place(x=40, y=240)
    actividades_input.place(x=40, y=260)

    deportes_label = tk.Label(frame_phone, text="Deportes favoritos:", bg="black", foreground="white")
    deportes_input = tk.Entry(frame_phone)
    deportes_label.place(x=40, y=280)
    deportes_input.place(x=40, y=300)

    limpiar_btn = tk.Button(frame_phone, text="EMPEZAR", command=guardar_contenido)
    limpiar_btn.place(x=40, y=320)

    phone.mainloop()


# Funcion luz
def luz():
    if cb[0] <= 80:
        """try:
            etiqueta_bateria.destroy()
        except:
            pass"""
        # ENCENDER
        cargar_bateria()

    elif primera_vez[0] is True:

        # grado de encendido
        primera_vez[0] = False
        bluetooth()

        preguntas()

    """else:

        label_imagen_negro.destroy()

        cargar_bateria()

        # HORA
        frame_hora.pack()
        frame_hora.place(relx=0.5, rely=0.5, anchor=CENTER)

        # FECHA
        etiqueta_fecha.pack(anchor="center")

        # Funcion para que cambie a negro
        def cambiar_color_a_negro():
            app.config(bg='black')
            Label_imagen_usb.config(background="black")

        # Cambiamos a azul claro
        app.config(background="light blue")
        Label_imagen_usb.config(background="light blue")

        # Indicamos tiempo de espera
        app.after(5000, cambiar_color_a_negro)"""


# Funcion que cambia la imagen del cargador


def cambiar_imagen_cargador():
    if cargando[0] is False:
        Label_imagen_usb.config(image=imagen_usb_conectado)
        Label_imagen_usb.place(x=183, y=335)
        boton_cargador.config(fg="green")

        cargando[0] = True
        app.after(3000, funcion_cargar)

    elif cargando[0] is True:
        # Crear un widget Label y asignarle la imagen
        label_imagen_negro = Label(app, image=imagen_negro, background="black")
        label_imagen_negro.place(x=180, y=730)

        Label_imagen_usb.config(image=imagen_usb)
        boton_cargador.config(fg="yellow")

        cargando[0] = False


# Funcion cargar


def actualizar_bateria():
    if cargando[0] is True:
        cargar_bateria()
        if cb[0] < 100:
            cb[0] += 5
        app.after(2000, actualizar_bateria)


def funcion_cargar():
    cargar_bateria()

    app.after(500, actualizar_bateria)


# Funcion descargar
def descargar():
    cb[0] = cb[0] - 5

    if cb[0] < 0:
        cb[0] = 0

    cargar_bateria()
    etiqueta_s.after(5000, descargar)


def cargar_bateria():
    global etiqueta_bateria, etiqueta_bateria_1
    if cb[0] > 100:
        cb[0] = 100

    if variable_bateria[0] is True:
        etiqueta_bateria = Label(frame_raiz, font=("digitalk", 15), text=f"{cb[0]}%", bg="black", foreground="white")
        etiqueta_bateria.place(x=255, y=10)
        try:
            etiqueta_bateria_1.destroy()
        except:
            pass

        variable_bateria[0] = False

    elif variable_bateria[0] is False:
        etiqueta_bateria_1 = Label(frame_raiz, font=("digitalk", 15), text=f"{cb[0]}%", bg="black", foreground="white")
        etiqueta_bateria_1.place(x=255, y=10)
        try:
            etiqueta_bateria.destroy()
        except:
            pass

        variable_bateria[0] = True

def llamando_carga_solar():
    carga_solar()

    app.after(3000, llamando_carga_solar)


def carga_solar():
    label_imagen_nube = Label()
    label_imagen_sol = Label()
    label_imagen_negro = Label()

    if cargando[0] is False and primera_vez[0] is False and cb[0] < 100:
        label_imagen_negro.destroy()
        label_imagen_nube.destroy()
        label_imagen_sol.destroy()

        # Esta amaneciendo
        if strftime("%H") == "06" or strftime("%H") == "07" or strftime("%H") == "08":

            luz = "amaneciendo"
            # Crear un widget Label y asignarle la imagen
            label_imagen_sol = Label(app, image=imagen_sol, background="black")
            label_imagen_sol.place(x=195, y=728)

            cb[0] = cb[0] + 1

        # Es de dia
        elif strftime("%H") == "09" or strftime("%H") == "10" or strftime("%H") == "11" or strftime \
                    ("%H") == "12" or strftime("%H") == "13" or strftime("%H") == "14" or strftime("%H") == "15":

            numero_aleatorio = random.randint(0, 1)

            # soleado
            if numero_aleatorio == 0:
                luz = "dia soleado"

                # Crear un widget Label y asignarle la imagen
                label_imagen_sol = Label(app, image=imagen_sol, background="black")
                label_imagen_sol.place(x=195, y=728)

                cb[0] = cb[0] + 3

            # nublado
            elif numero_aleatorio == 1:
                luz = "dia nublado"

                cb[0] = cb[0] + 2

                # Crear un widget Label y asignarle la imagen
                label_imagen_nube = Label(app, image=imagen_nube, background="black")
                label_imagen_nube.place(x=195, y=730)

        elif strftime("%H") == "16" or strftime("%H") == "17" or strftime("%H") == "18" or strftime \
                    ("%H") == "19" or strftime("%H") == "20":

            numero_aleatorio = random.randint(0, 1)

            # soleado
            if numero_aleatorio == 0:
                luz = "tarde soleada"

                cb[0] = cb[0] + 2

                # Crear un widget Label y asignarle la imagen
                label_imagen_sol = Label(app, image=imagen_sol, background="black")
                label_imagen_sol.place(x=195, y=728)

            # nublado
            elif numero_aleatorio == 1:
                luz = "tarde nublada"

                cb[0] = cb[0] + 1

                # Crear un widget Label y asignarle la imagen
                label_imagen_nube = Label(app, image=imagen_nube, background="black")
                label_imagen_nube.place(x=195, y=730)

        else:
            luz = "noche"

        if luz != "noche":
            boton_cargador.config(fg="green")

    else:

        # Crear un widget Label y asignarle la imagen
        label_imagen_negro = Label(app, image=imagen_negro, background="black")
        label_imagen_negro.place(x=180, y=728)


# Titulo
app = Tk()

# VARIABLES

variable_bateria = [True]
cargando = [False]
primera_vez = [True]

# Cargar la imagen
# imagen_sol = PhotoImage(file="sol.png")
imagen_sol = PhotoImage(file="fondo_sin_nada.png")

# imagen_nube = PhotoImage(file="nube.png")
imagen_nube = PhotoImage(file="fondo_sin_nada.png")

# imagen_negro = PhotoImage(file="negro.png")
imagen_negro = PhotoImage(file="fondo_sin_nada.png")
label_imagen_negro = Label(app, image=imagen_negro, background="black")
label_imagen_negro.place(x=180, y=730)

app.title('Reloj digital')

app.title("Reloj deportivo")  # Título de la ventana
app.iconbitmap("icono.ico")  # Ventana logo
app.config(bg="black")  # Color fondo de la ventana
app.state('zoomed')

miImagen = PhotoImage(file="apple3.PNG")  # Importamos imagen
miLabel_image = Label(app, image=miImagen, bg="black")  # Para mostrar la imagen
miLabel_image.place(x=500, y=40)

frame_raiz = Frame(app)
frame_raiz.place(x=550, y=215)
frame_raiz.config(bg="black")
frame_raiz.config(width=310, height=350)

# Frame de la hora y fecha
frame_hora = Frame(app, width="800", height="800")

# Etiqueta horas y minutos
etiqueta_hm = Label(frame_hora, font=("digitalk", 70), text="H:M")
etiqueta_hm.grid(row=0, column=0)

# Etiqueta segundos
etiqueta_s = Label(frame_hora, font=("digitalk", 30), text="s")
etiqueta_s.grid(row=0, column=1, sticky="n")

# Etiqueta fecha
etiqueta_fecha = Label(font=("digitalk", 30), text="dia d/m/aaaa")

# Boton light
boton_luz = tk.Button(app, text="'", font=("digitalk", 12), borderwidth=5, command=luz)
boton_luz.place(x=493, y=290)

# Imagen usb
imagen_usb = PhotoImage(file="fondo_sin_nada.png")
imagen_usb_conectado = PhotoImage(file="cable_1.png")

Label_imagen_usb = Label(app, image=imagen_usb, background="black")
Label_imagen_usb.place(x=280, y=730)

# Boton
boton_cargador = tk.Button(app, text="C", font=("digitalk", 15), command=cambiar_imagen_cargador, fg="yellow"
                           , bg="black", borderwidth=0)
boton_cargador.place(x=490, y=750)

# BATERIA


# carga bateria


cb = [50]

# tiempo de carga
t = 2

# Descargar
app.after(10000, descargar)

reloj_digital()

carga_solar()
llamando_carga_solar()

app.mainloop()
