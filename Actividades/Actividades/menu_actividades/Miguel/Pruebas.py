
from tkinter import *
from tkinter.ttk import *
root = Tk()

root.title("Reloj Deportivo")
icono = PhotoImage(file="img/reloj.png")
root.iconphoto(False, icono)

#CALCULADORA
caja1 = LabelFrame(root, text="Calculadora")
caja1.grid(row=0, column=0, padx=20, pady=20)

foto1 = PhotoImage(file='img/calculator.png')
foto1_1 = foto1.subsample(10, 10)

boton1 = Button(caja1, text="Calculadora", image=foto1_1).pack()

#BICICLETA
caja2 = LabelFrame(root, text="Bicicleta")
caja2.grid(row=2, column=0, padx=20, pady=20)

foto2 = PhotoImage(file='img/bici.png')
foto2_1 = foto2.subsample(10, 10)

boton2 = Button(caja2, text="Bicicleta", image=foto2_1).pack()

#HORA
hora = Label(root, text="Horaaa")
hora.grid(row=1, column=1, columnspan=3, padx=20, pady=20)


#CALORIAS
caja3 = LabelFrame(root, text="Calorias")
caja3.grid(row=0, column=4, padx=20, pady=20)

foto3 = PhotoImage(file='img/calorias.png')
foto3_1 = foto3.subsample(10, 10)

boton3 = Button(caja3, text="Bicicleta", image=foto3_1).pack()


#SUB-MENU
caja4 = LabelFrame(root, text="Menu")
caja4.grid(row=2, column=4, padx=20, pady=20)

foto4 = PhotoImage(file='img/menu.png')
foto4_1 = foto4.subsample(10, 10)

boton4 = Button(caja4, text="Menu", image=foto4_1).pack()

mainloop()