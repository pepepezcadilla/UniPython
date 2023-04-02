"""
Descripcion del programa:
	Aplicacion hecha para el reloj deportivo, contiene distintos apartados
	con grupos de musculos y un acceso directo a una página web que indica
	distintos ejercicios...

Autor: Oscar Fabris Ruiz
"""

import tkinter as tk
from tkinter import *
from tkinter.ttk import *


def link_pecho():
	phone = tk.Toplevel()
	phone.geometry("250x480")
	phone.configure(bg="white")
	phone.title("Iphone")
	phone.iconbitmap("logo_apple.ico")

	imagen_iphone = PhotoImage(file="iphone_8_recortado.png")
	label_imagen_iphone = Label(phone, image=imagen_iphone, background="white")
	label_imagen_iphone.place(x=0, y=0)

	frame_phone = tk.Frame(phone)
	frame_phone.place(x=30, y=62)
	frame_phone.config(bg="black")
	frame_phone.config(width=200, height=357)

	nombre_label = tk.Label(frame_phone, text="Rutina:", bg="black", foreground="white")
	nombre_label.place(x=40, y=0)

	ejercicio_label = tk.Label(frame_phone, text="Barbell Bench Press", bg="black", foreground="white")
	ejercicio_label.place(x=40, y=20)

	repeticiones_label = tk.Label(frame_phone, text="3 x 15", bg="black", foreground="white")
	repeticiones_label.place(x=40, y=40)
	
	phone.mainloop()

def link_brazo():
	phone = tk.Toplevel()
	phone.geometry("250x480")
	phone.configure(bg="white")
	phone.title("Iphone")
	phone.iconbitmap("logo_apple.ico")

	imagen_iphone = PhotoImage(file="iphone_8_recortado.png")
	label_imagen_iphone = Label(phone, image=imagen_iphone, background="white")
	label_imagen_iphone.place(x=0, y=0)

	frame_phone = tk.Frame(phone)
	frame_phone.place(x=30, y=62)
	frame_phone.config(bg="black")
	frame_phone.config(width=200, height=357)

	nombre_label = tk.Label(frame_phone, text="Rutina:", bg="black", foreground="white")
	nombre_label.place(x=40, y=0)

	ejercicio_label = tk.Label(frame_phone, text="Barbell Curl", bg="black", foreground="white")
	ejercicio_label.place(x=40, y=20)

	repeticiones_label = tk.Label(frame_phone, text="3 x 15", bg="black", foreground="white")
	repeticiones_label.place(x=40, y=40)

	# espacio
	espacio_label = tk.Label(frame_phone, text="", bg="black", foreground="black")
	espacio_label.place(x=40, y=60)
	
	ejercicio2_label = tk.Label(frame_phone, text="Cable pushdowns:", bg="black", foreground="white")
	ejercicio2_label.place(x=40, y=80)

	repeticiones_label = tk.Label(frame_phone, text="3 x 15", bg="black", foreground="white")
	repeticiones_label.place(x=40, y=100)

	phone.mainloop()
	
def link_espalda():
	phone = tk.Toplevel()
	phone.geometry("250x480")
	phone.configure(bg="white")
	phone.title("Iphone")
	phone.iconbitmap("logo_apple.ico")

	imagen_iphone = PhotoImage(file="iphone_8_recortado.png")
	label_imagen_iphone = Label(phone, image=imagen_iphone, background="white")
	label_imagen_iphone.place(x=0, y=0)

	frame_phone = tk.Frame(phone)
	frame_phone.place(x=30, y=62)
	frame_phone.config(bg="black")
	frame_phone.config(width=200, height=357)

	nombre_label = tk.Label(frame_phone, text="Rutina:", bg="black", foreground="white")
	nombre_label.place(x=40, y=0)

	ejercicio_label = tk.Label(frame_phone, text="Pullups / Machine Pulldown", bg="black", foreground="white")
	ejercicio_label.place(x=40, y=20)

	repeticiones_label = tk.Label(frame_phone, text="3 x 15", bg="black", foreground="white")
	repeticiones_label.place(x=40, y=40)
	
	phone.mainloop()
	
def link_pierna():
	phone = tk.Toplevel()
	phone.geometry("250x480")
	phone.configure(bg="white")
	phone.title("Iphone")
	phone.iconbitmap("logo_apple.ico")

	imagen_iphone = PhotoImage(file="iphone_8_recortado.png")
	label_imagen_iphone = Label(phone, image=imagen_iphone, background="white")
	label_imagen_iphone.place(x=0, y=0)

	frame_phone = tk.Frame(phone)
	frame_phone.place(x=30, y=62)
	frame_phone.config(bg="black")
	frame_phone.config(width=200, height=357)

	nombre_label = tk.Label(frame_phone, text="Rutina:", bg="black", foreground="white")
	nombre_label.place(x=40, y=0)

	ejercicio_label = tk.Label(frame_phone, text="Barbell Squat", bg="black", foreground="white")
	ejercicio_label.place(x=40, y=20)

	repeticiones_label = tk.Label(frame_phone, text="3 x 15", bg="black", foreground="white")
	repeticiones_label.place(x=40, y=40)
	
	phone.mainloop()

# -------------------------------------------------------------- Main:

root = Tk()

root.title("Modo gym")
icono = PhotoImage(file="img/pesas.png")
root.iconphoto(False, icono)

#CALCULADORA
caja1 = LabelFrame(root, text="Pecho")
caja1.grid(row=0, column=0, padx=20, pady=20)

foto1 = PhotoImage(file='img/pesas.png')
foto1_1 = foto1.subsample(10, 10)

boton1 = Button(caja1, command=link_pecho, image=foto1_1).pack()

#BICICLETA
caja2 = LabelFrame(root, text="Brazo")
caja2.grid(row=2, column=0, padx=20, pady=20)

foto2 = PhotoImage(file='img/pesas.png')
foto2_1 = foto2.subsample(10, 10)

boton2 = Button(caja2, command=link_brazo, image=foto2_1).pack()

#HORA
hora = Label(root, text="Time to train !!!")
hora.grid(row=1, column=1, columnspan=3, padx=20, pady=20)


#CALORIAS
caja3 = LabelFrame(root, text="Espalda")
caja3.grid(row=0, column=4, padx=20, pady=20)

foto3 = PhotoImage(file='img/pesas.png')
foto3_1 = foto3.subsample(10, 10)

boton3 = Button(caja3, command=link_espalda, image=foto3_1).pack()


#SUB-MENU
caja4 = LabelFrame(root, text="Pierna")
caja4.grid(row=2, column=4, padx=20, pady=20)

foto4 = PhotoImage(file='img/pesas.png')
foto4_1 = foto4.subsample(10, 10)

boton4 = Button(caja4, command=link_pierna, image=foto4_1).pack()

mainloop()
