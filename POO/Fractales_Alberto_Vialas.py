import turtle
import time

#grados = 0
#turtle.speed(15)
#for i in range(1, 40):
#    for x in range(0, 4):
#        turtle.forward(50)
#        turtle.left(150)
#        turtle.left(grados+5)

longitud_minima = 1
def Arbol(a, longitud, ordenado, angulo):
    if longitud >= longitud_minima:
        a.forward(longitud)
        longitud_nueva = longitud - ordenado
        a.left(angulo)
        Arbol(a, longitud_nueva, ordenado, angulo)
        a.right(angulo * 2)
        Arbol(a, longitud_nueva, ordenado, angulo)
        a.left(angulo)
        a.backward(longitud)


arbol = turtle.Turtle()
arbol.hideturtle
arbol.setheading(90)
arbol.color('blue')

Arbol(arbol, 50, 3, 30)
turtle.done()