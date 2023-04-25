import turtle
import tkinter as tk

class Fractal:
    def __init__(self,turtle, longitud, factor, angulo, caso_base):
        self.turtle = turtle
        self.longitud = longitud
        self.factor = factor
        self. angulo = angulo
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
    def __init__(self, turtle, longitud, factor, angulo, caso_base):
        super().__init__(turtle, longitud, factor, angulo, caso_base)

    def Arbol(self):
        if self.longitud >= 1:
            self.turtle.forward(self.longitud)
            longitud_nueva = self.longitud - self.factor
            self.turtle.left(self.angulo)
            Arbol(self.turtle, longitud_nueva, self.factor, self.angulo)
            self.turtle.right(self.angulo * 2)
            Arbol(self.turtle, longitud_nueva, self.factor, self.angulo)
            self.turtle.left(self.angulo)
            self.turtle.backward(self.longitud)

#ME HE QUEDADO AQUI <-----------------------------------------------------------------------------------
def Curva_Kotch(t, iteraciones, longitud, factor, angulo):
    if iteraciones == 0: 
        t.forward(longitud)
    else: 
        iteraciones = iteraciones-1
        longitud = longitud/factor
        Curva_Kotch(t, iteraciones, longitud, factor, angulo)
        t.left(angulo)
        Curva_Kotch(t, iteraciones, longitud, factor, angulo)
        t.right(angulo*2)
        Curva_Kotch(t, iteraciones, longitud, factor, angulo)
        t.left(angulo)
        Curva_Kotch(t, iteraciones, longitud, factor, angulo)

# Clase para pintar el árbol y el koch
class Pinta(Arbol, Curva_Kotch):
    def arbol(self, mostrar_puntero, color, longitud, ordenado, angulo):
        # Lógica para pintar el árbol
        pass
    
    def koch(self, mostrar_puntero, color, iteraciones, longitud, factor, angulo):
        # Lógica para pintar el koch
        pass

# Clase para el menú
class MenuGrafico:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menú Gráfico")
        self.pinta = Pinta()
        self.create_menu()

    def create_menu(self):
        # Botones del menú
        arbol_button = tk.Button(text="Árbol", command=self.opciones_arbol)
        arbol_button.pack()
        koch_button = tk.Button(text="Koch", command=self.opciones_koch)
        koch_button.pack()
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
        pintar_button = tk.Button(opciones_arbol_window, text="Pintar", command=lambda: self.pinta.arbol(
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
        pintar_button = tk.Button(opciones_koch_window, text="Pintar", command=lambda: self.pinta.koch(
            mostrar_puntero_entry.get(), color_entry.get(), iteraciones_entry.get(), longitud_entry.get(),
            factor_entry.get(), angulo_entry.get()))
        pintar_button.pack()

        # Botón de volver
        volver_button = tk.Button(opciones_koch_window, text="Volver", command=opciones_koch_window.destroy)
        volver_button.pack()

    def limpiar(self):
        # Lógica para limpiar el lienzo
        pass

    def salir(self):
        self.window.destroy()

menu_grafico = MenuGrafico()
menu_grafico.window.mainloop()