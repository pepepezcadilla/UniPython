"""
	Descipcion del programa: Opcion de -caminar- del reloj deportivo
Autor: Oscar Fabris Ruiz
Version 1.0

Ultiima modificacion: ####
"""

# LIBRERIAS, VARIABLES Y DEFINICIONES: ───────────────────────────────────────────────────────────

# ------------------------------------ Librerías de Esteban:
from tkinter import *
from tkinter.ttk import *
from time import sleep, strftime		# Para implementar el rejoj
import tkinter as tk


def btn_caminador():
	est = estado.get()
	# El usuario esta en movimiento
	if est == False:
		label_estado.config(image=caminando)
		boton_estado.config(bg='red', text='Stop')
		est = True

	# El usuario se ha detenido
	elif est == True:
		label_estado.config(image=parado)
		boton_estado.config(bg='green2', text='Start')
		est = False

	estado.set(est)


def cambia_variables():
	est = estado.get()
	tie = tiempo_n.get()
	pas = pasos_n.get()

	# Activado
	if est == True:
		tiempo_n.set(tie + 1)
		pasos_n.set(pas + 2 )
		num_tiempo.config(text=f'{tiempo_n.get()}')			
		num_pasos.config(text=f'{pasos_n.get()}')

	# Desactivado
	elif est == False:
		tiempo_n.set(0)
		pasos_n.set(0)
		num_tiempo.config(text=f'{tiempo_n.get()}')
		num_pasos.config(text=f'{pasos_n.get()}')

	raiz_correr.after(1000, cambia_variables)


# CODIGO PRINCIPAL: ──────────────────────────────────────────────────────────────────────────────
raiz_correr = Tk()


# ---------------------------------------------------- Variables dentro de tkinter:
# asigno la variable para saber si está en movimiento
estado = BooleanVar(name='bool_e' )
estado.set(False)
# Creo las variables para los widgets
tiempo_n = IntVar(name='int_t')
tiempo_n.set(0)
pasos_n = IntVar(name='int_p')
pasos_n.set(0)

# ---------------------------------------------------- Main:

raiz_correr.title('- - - Modo Caminata - - -')
raiz_correr.geometry('800x800')
raiz_correr.resizable(False, False)
# Cambio el fondo
frame_global = Frame(raiz_correr)
frame_global.place(width=800, height=800)

imgfondo = PhotoImage(file='fondo_bosque.png')
fondo = Label(frame_global, image=imgfondo)
fondo.place(relheight=1, relwidth=1)
# Icono de la ventana
icono_reloj = tk.PhotoImage(file='icono_reloj.png')
raiz_correr.iconphoto(False, icono_reloj)


# ---- Creo el menu de parte superior
menu_opciones = Menu(frame_global)
raiz_correr.config(menu=menu_opciones)

opc_volver = Menu(menu_opciones, tearoff=0)
opc_volver.add_command(label='Actividades')
opc_volver.add_command(label='Menu')
opc_volver.add_separator()
opc_volver.add_command(label='Salir', command=raiz_correr.quit)

opc_favoritos = Menu(menu_opciones, tearoff=0)
opc_favoritos.add_command(label='Lista')
opc_favoritos.add_command(label='Agregar')
opc_favoritos.add_command(label='Quitar')

menu_opciones.add_cascade(label='Archivo', menu=opc_volver)
menu_opciones.add_cascade(label='Lista de Favoritos', menu=opc_favoritos)


# ---- Hora y batería del reloj



# ---- Imagen central y boton de accion
# frame que contiene elementos centrales
frame_centro = Frame(frame_global)
frame_centro.place(x=350, y=250)
# Asigno imagenes
parado = PhotoImage(file='parado.png')
caminando = PhotoImage(file='caminando.png')

label_estado = Label(frame_centro, image=parado)
label_estado.config(background='olive drab')
label_estado.pack()

boton_estado = tk.Button(frame_centro, text='Start', command=btn_caminador, bg='green2')
boton_estado.config(activebackground='turquoise1')
boton_estado.pack()


# ---- Podometro y tiempo:
frame_pasos = Frame(frame_global)
frame_pasos.place(y=700, width=200, height=100)
frame_pasos_superior = Frame(frame_pasos)
frame_pasos_superior.place(width=200, x=0, y=0)

tiempo = Label(frame_pasos_superior, text='Tiempo', font=('digitalk', 15))
tiempo.pack(side=LEFT)
pasos = Label(frame_pasos_superior, text='Pasos ', font=('digitalk', 15))
pasos.pack(side=RIGHT, )

num_tiempo = Label(frame_pasos, text=0, font=('digitalk', 15))
num_tiempo.pack(side=LEFT)
num_pasos = Label(frame_pasos, text=0, font=('digitalk', 15))
num_pasos.pack(side=RIGHT)

cambia_variables()

raiz_correr.mainloop()
