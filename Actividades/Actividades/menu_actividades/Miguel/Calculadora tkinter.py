#https://www.w3schools.com/python/python_try_except.asp

#CALCULADORA

from tkinter import *

root = Tk()
root.title("Calculadora básica")


icono = PhotoImage(file="img/calculator.png")
root.iconphoto(False, icono)

#!!!!
#No puedo usar esto ya que no es compatible con Linux, con Windows si qur lo es
#root.iconbitmap("img/calculator.ico")


#Para evitar que el usuario redimensione el tamaño de la ventana
#              x   y
root.resizable(0, 0) #Si pones uno esa coordenada si que se podra redimensionar

#Para dar dimensiones independientemente del contenido del programa
#pixeles x pixeles
root.geometry("400x370")


def enviar(valor):

    #Numero anterior
    anterior = pantalla.get()

    #Para que elimine lo que hay en la pantalla
    #     (posicion en widget, constante que busca el fin del string)
    pantalla.delete(0, END)
    pantalla.insert(0, str(anterior) + str(valor))

def igual():
    #intenta esto y sino inserta un error//// para mas info link de w3c en la linea 1
    try:
        global num2
        num2 = pantalla.get()
        pantalla.delete(0, END)
        if operacion == "+":
            pantalla.insert(0, float(num1) + float(num2))
        elif operacion == "-":
            pantalla.insert(0, float(num1) - float(num2))
        elif operacion == "*":
            pantalla.insert(0, float(num1) * float(num2))
        elif operacion == "/":
            pantalla.insert(0, float(num1) / float(num2))
    except NameError:
        pantalla.insert(0, "Error")


def suma():
    global num1
    global operacion
    num1 = pantalla.get()
    #Transformamos a un valor numerico, int o float
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "+"

def resta():
    global num1
    global operacion
    num1 = pantalla.get()
    #Transformamos a un valor numerico, int o float
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "-"

def multiplicacion():
    global num1
    global operacion
    num1 = pantalla.get()
    #Transformamos a un valor numerico, int o float
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "*"

def division():
    global num1
    global operacion
    num1 = pantalla.get()
    #Transformamos a un valor numerico, int o float
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = "/"

def limpiar():
    pantalla.delete(0, END)

pantalla = Entry(root,
                 width=22,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 font=('montserrat', 18, 'bold'))

pantalla.grid(row=0, padx=2, pady=2, columnspan=4)

boton1 = Button(root, text="1",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                #Para cambiar el cursor cuando pasemos por encima
                cursor="hand2",
                command=lambda : enviar(1)).grid(row=3, column=0, padx=1, pady=1)

boton2 = Button(root, text="2",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(2)).grid(row=3, column=1, padx=1, pady=1)

boton3 = Button(root, text="3",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(3)).grid(row=3, column=2, padx=1, pady=1)

boton4 = Button(root, text="4",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(4)).grid(row=2, column=0, padx=1, pady=1)

boton5 = Button(root, text="5",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(5)).grid(row=2, column=1, padx=1, pady=1)

boton6 = Button(root, text="6",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(6)).grid(row=2, column=2, padx=1, pady=1)

boton7 = Button(root, text="7",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(7)).grid(row=1, column=0, padx=1, pady=1)

boton8 = Button(root, text="8",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(8)).grid(row=1, column=1, padx=1, pady=1)

boton9 = Button(root, text="9",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(9)).grid(row=1, column=2, padx=1, pady=1)

boton0 = Button(root, text="0",
                width=9,
                height=3,
                bg="white",
                fg="red",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(0)).grid(row=4, column=1, padx=1, pady=1)

boton_igual = Button(root, text="=",
                width=9,
                height=3,
                bg="red",
                fg="white",
                borderwidth=0,
                cursor="hand2",
                command=igual).grid(row=4, column=0, padx=1, pady=1)

boton_punto = Button(root, text=".",
                width=9,
                height=3,
                bg="spring green",
                fg="black",
                borderwidth=0,
                cursor="hand2",
                command=lambda : enviar(".")).grid(row=4, column=2, padx=1, pady=1)

boton_suma = Button(root, text="+",
                width=9,
                height=3,
                bg="deep sky blue",
                fg="black",
                borderwidth=0,
                cursor="hand2",
                command=suma).grid(row=1, column=3, padx=1, pady=1)

boton_resta = Button(root, text="-",
                width=9,
                height=3,
                bg="deep sky blue",
                fg="black",
                borderwidth=0,
                cursor="hand2",
                command=resta).grid(row=2, column=3, padx=1, pady=1)

boton_mult = Button(root, text="*",
                width=9,
                height=3,
                bg="deep sky blue",
                fg="black",
                borderwidth=0,
                cursor="hand2",
                command=multiplicacion).grid(row=3, column=3, padx=1, pady=1)

boton_div = Button(root, text="/",
                width=9,
                height=3,
                bg="deep sky blue",
                fg="black",
                borderwidth=0,
                cursor="hand2",
                command=division).grid(row=4, column=3, padx=1, pady=1)

boton_limpiar = Button(root, text="CLEAR",
                       width=40,
                       height=3,
                       bg="deep sky blue",
                       fg="black",
                       borderwidth=0,
                       cursor="hand2",
                       command=limpiar).grid(row=5, column=0, columnspan=4, padx=1, pady=1)
mainloop()