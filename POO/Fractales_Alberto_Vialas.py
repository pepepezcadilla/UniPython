import turtle
import tkinter as tk


class Fractal:
    def __init__(self, longitud, factor, angulo, caso_base):
        self.longitud = int(longitud)
        self.factor = int(factor)
        self. angulo = int(angulo)
        self.caso_base = caso_base
        
    def dame_longitud(self):
        return self.longitud
    
    def dame_factor(self):
        return self.factor
    
    def dame_angulo(self):
        return self.angulo
    
    def dame_caso_base(self):
        return self.caso_base

class Arbol(Fractal):
    def __init__(self, longitud, factor, angulo, caso_base):
        super().__init__(longitud, factor, angulo, caso_base)

    def arbol(self):
        if int(self.longitud) >= 1:
            print(self.longitud)
            t.forward(self.longitud)
            longitud_vieja = self.longitud
            self.longitud = self.longitud - self.factor
            t.left(self.angulo)
            arbol_izquierdo = Arbol(self.longitud, self.factor, self.angulo, self.caso_base)
            arbol_izquierdo.arbol()
            t.right(self.angulo * 2)
            arbol_derecho = Arbol(self.longitud, self.factor, self.angulo, self.caso_base)
            arbol_derecho.arbol()
            t.left(self.angulo)
            t.backward(longitud_vieja)

class Curva_Koch(Fractal):
    def __init__(self, iteraciones, longitud, factor, angulo, caso_base):
        super().__init__(longitud, factor, angulo, caso_base)
        self.iteraciones = int(iteraciones)
        
    def dibujar(self):
        self.curva_koch(self.iteraciones, self.longitud)

    def curva_koch(self, n, l):
        if n == 0:
            t.forward(self.longitud)
            return
        for angle in [self.angulo, -2 * self.angulo, self.angulo, 0]:
            self.curva_koch(n-1, l*self.factor)
            t.left(angle)

# Clase para pintar el árbol y el koch
class Pinta():
    def __init__(self, hide, color, arbolito, frackoch):
        self.hide = hide
        self.color = color
        self.arbolito = arbolito
        self.frackoch = frackoch

        if(hide=="no"):
            t.hideturtle()
        t.color(color)
    
    def dame_oculta(self):
        return self.hide
    
    def dame_color(self):
        return self.color
    
    def arbol(self):
        if(self.arbolito != None):
            self.arbolito.arbol()
    
    def koch(self):
        if(self.frackoch != None):
            self.frackoch.dibujar()

#Función para crear un árbol y pintarlo
def pintararbol(hide, color, longitud, factor, angulo):
    caso_base = "arbol"
    arbol = Arbol(longitud, factor, angulo, caso_base)
    pintar = Pinta(hide, color, arbol, None)
    pintar.arbol()

#Función para crear una curva de koch y pintarlo
def pintarkoch(hide, color, iteraciones, longitud, factor, angulo):
    caso_base = "Koch"
    koch = Curva_Koch(iteraciones, longitud, factor, angulo, caso_base)
    pintar = Pinta(hide, color, None, koch)
    pintar.koch()
    t.right(120)

def inicio():
    t.up()
    t.goto(-200, 0)
    t.down()

# Clase para el menú
class MenuGrafico:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menú Gráfico")
        self.create_menu()
     

    def create_menu(self):
        # Botones del menú
        arbol_button = tk.Button(text="Árbol", command=self.opciones_arbol)
        arbol_button.pack()
        koch_button = tk.Button(text="Koch", command=self.opciones_koch)
        koch_button.pack()
        cero_button = tk.Button(text="Volver al inicio", command=lambda: inicio())
        cero_button.pack()
        limpiar_button = tk.Button(text="Limpiar", command=self.limpiar)
        limpiar_button.pack()
        salir_button = tk.Button(text="Salir", command=self.salir)
        salir_button.pack()

    def opciones_arbol(self):
        # Ventana de opciones para Árbol
        opciones_arbol_window = tk.Toplevel(self.window)
        opciones_arbol_window.title("Opciones Árbol")

        # Agregar inputs y botón de pintar
        # Input: Mostrar puntero
        mostrar_puntero_label = tk.Label(opciones_arbol_window, text="Mostrar puntero (si o no):")
        mostrar_puntero_label.pack()
        mostrar_puntero_entry = tk.Entry(opciones_arbol_window)
        mostrar_puntero_entry.pack()

        # Input: Color
        color_label = tk.Label(opciones_arbol_window, text="Color:")
        color_label.pack()
        color_entry = tk.Entry(opciones_arbol_window)
        color_entry.pack()

        # Input: Longitud
        longitud_label = tk.Label(opciones_arbol_window, text="Longitud:")
        longitud_label.pack()
        longitud_entry = tk.Entry(opciones_arbol_window)
        longitud_entry.pack()

        # Input: Ordenado
        ordenado_label = tk.Label(opciones_arbol_window, text="Ordenado:")
        ordenado_label.pack()
        ordenado_entry = tk.Entry(opciones_arbol_window)
        ordenado_entry.pack()

        # Input: Angulo
        angulo_label = tk.Label(opciones_arbol_window, text="Ángulo:")
        angulo_label.pack()
        angulo_entry = tk.Entry(opciones_arbol_window)
        angulo_entry.pack()

        # Botón de pintar
        pintar_button = tk.Button(opciones_arbol_window, text="Pintar", command=lambda: pintararbol(
            mostrar_puntero_entry.get(), color_entry.get(), longitud_entry.get(), ordenado_entry.get(),
            angulo_entry.get()))
        pintar_button.pack()

        # Botón de volver
        volver_button = tk.Button(opciones_arbol_window, text="Volver", command=opciones_arbol_window.destroy)
        volver_button.pack()

    def opciones_koch(self):
        # Ventana de opciones para Koch
        opciones_koch_window = tk.Toplevel(self.window)
        opciones_koch_window.title("Opciones Koch")
        # Agregar inputs y botón de pintar
        # Input: Mostrar puntero
        mostrar_puntero_label = tk.Label(opciones_koch_window, text="Mostrar puntero (si o no):")
        mostrar_puntero_label.pack()
        mostrar_puntero_entry = tk.Entry(opciones_koch_window)
        mostrar_puntero_entry.pack()

        # Input: Color
        color_label = tk.Label(opciones_koch_window, text="Color:")
        color_label.pack()
        color_entry = tk.Entry(opciones_koch_window)
        color_entry.pack()

        # Input: Iteraciones
        iteraciones_label = tk.Label(opciones_koch_window, text="Iteraciones:")
        iteraciones_label.pack()
        iteraciones_entry = tk.Entry(opciones_koch_window)
        iteraciones_entry.pack()

        # Input: Longitud
        longitud_label = tk.Label(opciones_koch_window, text="Longitud:")
        longitud_label.pack()
        longitud_entry = tk.Entry(opciones_koch_window)
        longitud_entry.pack()

        # Input: Factor
        factor_label = tk.Label(opciones_koch_window, text="Factor:")
        factor_label.pack()
        factor_entry = tk.Entry(opciones_koch_window)
        factor_entry.pack()

        # Input: Ángulo
        angulo_label = tk.Label(opciones_koch_window, text="Ángulo:")
        angulo_label.pack()
        angulo_entry = tk.Entry(opciones_koch_window)
        angulo_entry.pack()

        # Botón de pintar
        pintar_button = tk.Button(opciones_koch_window, text="Pintar", command=lambda: pintarkoch(
            mostrar_puntero_entry.get(), color_entry.get(), iteraciones_entry.get(), longitud_entry.get(),
            factor_entry.get(), angulo_entry.get()))
        pintar_button.pack()

        # Botón de volver
        volver_button = tk.Button(opciones_koch_window, text="Volver", command=opciones_koch_window.destroy)
        volver_button.pack()

    def limpiar(self):
        t.clear

    def salir(self):
        exit()

t = turtle.Turtle()
menu_grafico = MenuGrafico()
menu_grafico.window.mainloop()





def curva_koch(self):
    print(self.longitud)
    if self.iteraciones == 0: 
        t.forward(self.longitud)
    else: 
        self.iteraciones = self.iteraciones-1
        self.longitud = self.longitud/self.factor
        self.curva_koch()
        t.forward(self.longitud)
        t.left(self.angulo)
        self.curva_koch()
        t.forward(self.longitud)
        t.right(self.angulo*2)
        self.curva_koch()
        t.forward(self.longitud)
        t.left(self.angulo)
        self.curva_koch()
        t.forward(self.longitud)