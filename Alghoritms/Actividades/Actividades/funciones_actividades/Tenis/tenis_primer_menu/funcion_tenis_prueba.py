import random
import time

from tkinter import *
#from tkinter.ttk import *
#from time import strftime
import tkinter as tk

# random.randint(1, 8) del 1 al 8
# random.uniform(0, 2) del 0.0 al 2.0
# random.choice([6, 10]) el 6 o el 10


def volver_menu_anterior_tenis():
    global volver_menu
    volver_menu = True


def cambiar_pausar_tenis():
    global pausar_tenis
    if pausar_tenis is True:
        pausar_tenis = False
    elif pausar_tenis is False:
        pausar_tenis = True


def funcion_tenis_tk():
    #app.destroy()
    app.withdraw()
    menu_tenis = tk.Toplevel(app)
    menu_tenis.title("Tenis")
    menu_tenis.geometry("800x800")
    menu_tenis.config(bg='black')

    boton_pulsado = tk.BooleanVar()
    boton_pulsado.set(False)

    boton_inicio_tenis = tk.Button(menu_tenis, text="^",
                                   font=("digitalk", 12), borderwidth=8, command=lambda: boton_pulsado.set(True))
    boton_inicio_tenis.place(x=760, y=100)

    menu_tenis.wait_variable(boton_pulsado)
    boton_inicio_tenis.place_forget()
    menu_tenis.config(bg='white')

    # BOTONES RELOJ
    global volver_menu, pausar_tenis
    volver_menu = False
    boton_5_tenis = tk.Button(menu_tenis, text="BACK",
                              font=("digitalk", 12), borderwidth=8, command=volver_menu_anterior_tenis)
    boton_5_tenis.place(x=720, y=700)

    pausar_tenis = False
    boton_4_tenis = tk.Button(menu_tenis, text="^", font=("digitalk", 12), borderwidth=8, command=cambiar_pausar_tenis)
    boton_4_tenis.place(x=760, y=100)

    def luz_tenis():
        def cambiar_color():
            menu_tenis.config(bg='white')

        # Cambiamos a azul claro
        menu_tenis.config(bg='light blue')

        # Indicamos tiempo de espera
        app.after(3000, cambiar_color)
    boton_luz_tenis = tk.Button(menu_tenis, text="Light", font=("digitalk", 12), borderwidth=8, command=luz_tenis)
    boton_luz_tenis.place(x=10, y=100)

    boton_2_tenis = tk.Button(menu_tenis, text="Up", font=("digitalk", 12), borderwidth=8, command=luz_tenis)
    boton_2_tenis.place(x=10, y=400)

    boton_3_tenis = tk.Button(menu_tenis, text="Down", font=("digitalk", 12), borderwidth=8, command=luz_tenis)
    boton_3_tenis.place(x=10, y=700)

    # Imagenes
    latidos_corazon_prueba = True

    imagen_tenista_raqueta = PhotoImage(file="jugador-de-tenis-con-raqueta_2.png")
    imagen_tenista_raqueta_label = Label(menu_tenis, image=imagen_tenista_raqueta, background="white")
    imagen_tenista_raqueta_label.place(x=80, y=50)

    imagen_zapato = PhotoImage(file="zapato_128x128.png")
    imagen_zapato_label = Label(menu_tenis, image=imagen_zapato, background="white")
    imagen_zapato_label.place(x=300, y=50)

    imagen_reloj = PhotoImage(file="icono_reloj_128x128.png")
    imagen_reloj_label = Label(menu_tenis, image=imagen_reloj, background="white")
    imagen_reloj_label.place(x=300, y=250)


    imagen_fuego = PhotoImage(file="fuego_128x128.png")
    imagen_fuego_label = Label(menu_tenis, image=imagen_fuego, background="white")
    imagen_fuego_label.place(x=300, y=650)



    # VARIABLE DE TENIS

    # -Variables generales
    contador_segundos = 0  # "contador_segundos" Se va a encargar de contar los segundos que pasan en el partido
    tiempo_descansos = 0  # "tiempo_descansos" Se va a encargar de contar los segundos que pasa en reposo
    #metros_segundo = random.uniform(0, 2.5)  # Posibles metros recorridos en un segundo
    metros_segundo = 0  # Posibles metros recorridos en un segundo

    # -Variables mientras se esta jugando
    contador_punto = 0
    duracion_punto = random.randint(4, 20)  # La posible duracion de un punto
    estado_punto = True  # Si es True significa que esta jugando un punto, False esta entre punto y punto

    # -Variables mientras se esta jugando un game/juego
    contador_juego_puntos = 0
    duracion_juego_puntos = random.randint(4, 10)  # Los posibles puntos que hay en un game

    # -Variables mientras se esta descansando despues de un game/juego
    contador_juego_descanso = 0
    duracion_juego_descanso = random.randint(60, 120)  # Los posibles segundos en el descanso
    estado_juego = True  # Si es True significa que esta jugando un juego, False esta entre juego y juego

    # -Variables mientras se esta jugando un set
    contador_todo_juegos = 0
    todo_juegos = random.randint(6, 13)  # Todos los posibles games que hay en un set

    # -Variables mientras se esta descansando despues de un set
    contador_set_descanso = 0
    duracion_set_descanso = random.randint(60, 120)  # Los posibles segundos en el descanso entre set y set
    estado_set = True  # Si es True significa que esta jugando un juego, False esta entre juego y juego

    contador_set = 0
    sets = random.randint(3, 5)

    # Variables frecuencia cardiaca
    frecuencia_reposo = random.randint(40, 100)  # "frecuencia_reposo" es la frecuencia en reposo del usuario
    edad = 30  # CAMBIAR
    frecuencia_cardiaca_maxima = 220 - edad
    frecuencia = frecuencia_reposo
    lista_frecuencias = []

    # Variables calorias
    contador_calorias = 0
    peso = random.randint(60, 100)  # CAMBIAR
    calorias_hora = peso / 0.16
    calorias_segundo = round(calorias_hora / 3600, 2)
    posibles_calorias = calorias_segundo + 0.15

    while True:
        # Si pausar_tenis is True significa que esta pausada la actividad
        if pausar_tenis:
            if volver_menu:
                menu_tenis.destroy()  # destruir la ventana actual (tenis)
                app.deiconify()  # volver a mostrar la ventana anterior (app)
                volver_menu = False
                break
            menu_tenis.update()

        else:
            if contador_set == sets:
                break

            # Si estan jugando un set o descanso
            if estado_set is True:
                if contador_todo_juegos == todo_juegos:
                    contador_set += 1

                    contador_todo_juegos = 0
                    contador_juego_descanso = 0
                    duracion_juego_descanso = random.randint(60, 120)  # Los posibles segundos en el descanso
                    todo_juegos = random.randint(6, 13)  # Todos los posibles games que hay en un set
                    estado_set = False  # Se pasa de estar jugando un set a estar descansando

                # Si estan jugando un game o descanso
                if estado_juego is True:
                    if contador_juego_puntos >= duracion_juego_puntos:
                        contador_todo_juegos += 1

                        contador_juego_puntos = 0
                        duracion_juego_puntos = random.randint(4, 10)  # Los posibles puntos que hay en un game

                        estado_juego = False  # Se pasa de estar jugando a un game a estar descansando
                        continue

                    # Si estan jugando un punto o sacando
                    if estado_punto is True:
                        if contador_punto >= duracion_punto:
                            contador_juego_puntos += 1

                            duracion_punto = random.randint(5, 20)  # Los posibles segundos mientras se saca
                            contador_punto = 0
                            estado_punto = False  # Se pasa de estar jugando a estar sacando
                            continue
                        if contador_segundos != 0:
                            metros_segundo += random.uniform(0, 2.5)  # Posibles metros recorridos en un segundo

                    else:
                        tiempo_descansos = tiempo_descansos + 1
                        if contador_punto >= duracion_punto:
                            duracion_punto = random.randint(4, 20)  # La posible duracion de un punto
                            contador_punto = 0
                            estado_punto = True  # Se pasa de estar sacando a estar jugando

                        metros_segundo += random.uniform(0, 0.3)  # Posibles metros recorridos en un segundo

                    contador_punto += 1

                else:
                    tiempo_descansos = tiempo_descansos + 1
                    contador_juego_descanso = contador_juego_descanso + 1
                    if contador_juego_descanso >= duracion_juego_descanso:
                        estado_juego = True  # Se pasa de estar descansando a estar jugando un game
                        contador_juego_descanso = 0
                        duracion_juego_descanso = random.randint(60, 120)  # Los posibles segundos en el descanso

            else:
                tiempo_descansos = tiempo_descansos + 1
                contador_set_descanso = contador_set_descanso + 1
                if contador_set_descanso >= duracion_set_descanso:
                    estado_set = True  # Se pasa de estar descansando a estar jugando un set
                    duracion_set_descanso = random.randint(60, 120)  # Los posibles segundos en el descanso entre set y set
                    contador_set_descanso = 0

            if estado_set is True and estado_juego is True and estado_punto is True:
                # frecuencia = frecuencia + (frecuencia * 0.009)
                if frecuencia >= frecuencia_cardiaca_maxima:
                    frecuencia = frecuencia + random.randint(-2, 1)
                elif frecuencia <= frecuencia_reposo:
                    frecuencia = frecuencia + random.randint(1, 5)
                else:
                    frecuencia = frecuencia + random.randint(1, 2)

            elif estado_set is True and estado_juego is True and estado_punto is False:
                if frecuencia >= frecuencia_cardiaca_maxima:
                    frecuencia = frecuencia + random.randint(-2, 1)
                elif frecuencia <= frecuencia_reposo:
                    frecuencia = frecuencia + 2
                else:
                    frecuencia = frecuencia - random.randint(0, 1)
            elif estado_set is True and estado_juego is False:
                if frecuencia >= frecuencia_cardiaca_maxima:
                    frecuencia = frecuencia + random.randint(-2, 1)
                elif frecuencia <= frecuencia_reposo:
                    frecuencia = frecuencia + 2
                else:
                    frecuencia = frecuencia - random.randint(0, 1)
            elif estado_set is False:
                if frecuencia >= frecuencia_cardiaca_maxima:
                    frecuencia = frecuencia + random.randint(-2, 1)
                elif frecuencia <= frecuencia_reposo:
                    frecuencia = frecuencia + 2
                else:
                    frecuencia = frecuencia - random.randint(0, 1)
            lista_frecuencias.append(frecuencia)
            print()

            # Apartir de aqui se carga todos los datos que se muestran al usuario

            metros_label = tk.Label(menu_tenis, text=f"{metros_segundo:.2f} m", font=("Arial", 24))
            metros_label.place(x=450, y=50)

            tiempo = time.gmtime(contador_segundos)
            tiempo_formateado = time.strftime('%H:%M:%S', tiempo)
            tiempo_label = tk.Label(menu_tenis, text=f"{tiempo_formateado}", font=("Arial", 24))
            tiempo_label.place(x=450, y=250)

            frecuencia_label = tk.Label(menu_tenis, text=f"{frecuencia}", font=("Arial", 24))
            frecuencia_label.place(x=450, y=450)

            calorias_label = tk.Label(menu_tenis, text=f"{contador_calorias:.2f} Kcal", font=("Arial", 24))
            calorias_label.place(x=450, y=650)

            if latidos_corazon_prueba is True:
                imagen_corazon = PhotoImage(file="corazon_prueba.png")
                corazon_prueba = Label(menu_tenis, image=imagen_corazon, background="white")
                corazon_prueba.place(x=300, y=450)
                latidos_corazon_prueba = False
            else:
                corazon_prueba.destroy()
                imagen_corazon_2 = PhotoImage(file="corazon_prueba_2.png")
                corazon_prueba_2 = Label(menu_tenis, image=imagen_corazon_2, background="white")
                corazon_prueba_2.place(x=300, y=450)
                latidos_corazon_prueba = True

            if volver_menu:
                menu_tenis.destroy()  # destruir la ventana actual (tenis)
                app.deiconify()  # volver a mostrar la ventana anterior (app)
                volver_menu = False
                break

            menu_tenis.update()
            time.sleep(1)
            contador_segundos += 1
            contador_calorias += random.uniform(0, posibles_calorias)  # Posibles calorias quemadas

    menu_tenis.mainloop()


app = Tk()

# Titulo
app.title('Reloj digital')

# Modificar si es ecalable
app.resizable(False, False)

# Fondo
app.config(bg='black')

app.geometry('800x800')

# Boton ^
boton_4 = tk.Button(app, text="^", font=("digitalk", 12), borderwidth=8, command=funcion_tenis_tk)
boton_4.place(x=760, y=100)


app.mainloop()