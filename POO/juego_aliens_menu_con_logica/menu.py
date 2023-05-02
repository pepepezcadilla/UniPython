import pygame, botones, sys, time, juego

pygame.mixer.init()
blanco = ("#231D3A")
salir = False
armas = []
arma1 = int()
arma2 = int()
pygame.mixer.music.load('musica_menu.mp3')
pygame.mixer.music.play(-1)

def imprimirArmas():
    global armas
    pistola_solo = pygame.image.load('pistola_solo.png').convert_alpha()
    metralleta_solo = pygame.image.load('metralleta_solo.png').convert_alpha()
    escopeta_solo = pygame.image.load('escopeta_solo.png').convert_alpha()
    cuchillo_solo = pygame.image.load('cuchillo_solo.png').convert_alpha()
    granada_solo = pygame.image.load('granada_solo.png').convert_alpha()
    lanzallamas_solo = pygame.image.load('lanzallamas_solo.png').convert_alpha()
    if len(armas) == 1:
        if armas[-1] == 1:
            imagen_arma1 = botones.boton(770, 665, pistola_solo, 1)
            return imagen_arma1
        elif armas[-1] == 2:
            imagen_arma1 = botones.boton(745, 630, metralleta_solo, 1)
            return imagen_arma1
        elif armas[-1] == 3:
            imagen_arma1 = botones.boton(760, 655, escopeta_solo, 1)
            return imagen_arma1
        elif armas[-1] == 4:
            imagen_arma1 = botones.boton(745, 645, cuchillo_solo, 1)
            return imagen_arma1
        elif armas[-1] == 5:
            imagen_arma1 = botones.boton(750, 655, granada_solo, 1)
            return imagen_arma1
        else:
            imagen_arma1 = botones.boton(740, 645, lanzallamas_solo, 1)
            return imagen_arma1
    else:
        if armas[-1] == 1:
            imagen_arma2 = botones.boton(890, 665, pistola_solo, 1)
            return imagen_arma2
        elif armas[-1] == 2:
            imagen_arma2 = botones.boton(875, 630, metralleta_solo, 1)
            return imagen_arma2
        elif armas[-1] == 3:
            imagen_arma2 = botones.boton(875, 655, escopeta_solo, 1)
            return imagen_arma2
        elif armas[-1] == 4:
            imagen_arma2 = botones.boton(875, 645, cuchillo_solo, 1)
            return imagen_arma2
        elif armas[-1] == 5:
            imagen_arma2 = botones.boton(875, 655, granada_solo, 1)
            return imagen_arma2
        else:
            imagen_arma2 = botones.boton(875, 645, lanzallamas_solo, 1)
            return imagen_arma2

def inicio():
    global salir
    screen = pygame.display.set_mode((1280, 832))
    print("osdodmjflsaidjc,f")
    # IMÁGENES
    inicio_imagen = pygame.image.load("inicio.png").convert()
    screen.fill(blanco)
    salir_bucle = time.time() + 4
    while time.time() < salir_bucle:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.blit(inicio_imagen, [0, 0])
    menu()

def sobreNosotros():
    global salir
    screen3 = pygame.display.set_mode((1280, 832))
    about_imagen = pygame.image.load("about_fondo.png").convert()
    volver_menu = pygame.image.load('volver_menu.png').convert_alpha()
    screen3.fill(blanco)
    boton_volver = botones.boton(444, 621, volver_menu, 1)

    while not salir:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen3.blit(about_imagen, [0, 0])
            if boton_volver.draw(screen3): # VOLVER AL MENÚ
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

def reglas_juego():
    global salir
    screen4 = pygame.display.set_mode((1280, 832))
    about_imagen = pygame.image.load("reglas_juego.png").convert()
    volver_menu = pygame.image.load('volver_menu.png').convert_alpha()
    screen4.fill(blanco)
    boton_volver = botones.boton(444, 647, volver_menu, 1)

    while not salir:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen4.blit(about_imagen, [0, 0])
            # EMPEZAR
            if boton_volver.draw(screen4):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu()

def menu():
    global salir
    screen1 = pygame.display.set_mode((1280, 832))
    # IMÁGENES
    menu_imagen = pygame.image.load("menu.png").convert()
    imagen_reglas = pygame.image.load("reglas.png").convert_alpha()
    imagen_elegir = pygame.image.load("elegir_armas (1).png").convert_alpha()
    imagen_salir = pygame.image.load("salir (1) (1).png").convert_alpha()
    imagen_about = pygame.image.load('about.png').convert_alpha()
    imagen_sonido_on = pygame.image.load('sonido_on.png').convert_alpha()
    imagen_sonido_off = pygame.image.load('sonido_off.png').convert_alpha()
    screen1.fill(blanco)
    # BOTONES
    boton_reglas = botones.boton(597, 159, imagen_reglas, 1)
    boton_elegir = botones.boton(597, 354, imagen_elegir, 1)
    boton_salir = botones.boton(597, 548, imagen_salir, 1)
    boton_about = botones.boton(995, 43, imagen_about, 1)
    boton_sonido_on = botones.boton(899, 52, imagen_sonido_on, 1)
    boton_sonido_off = botones.boton(949, 52, imagen_sonido_off, 1)

    while not salir:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen1.blit(menu_imagen, [0, 0])
            if boton_sonido_on.draw(screen1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.unpause()
            if boton_sonido_off.draw(screen1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.pause()
            if boton_reglas.draw(screen1): # MOSTRAR PANTALLA DE REGLAS JUEGO
                if event.type == pygame.MOUSEBUTTONDOWN:
                    reglas_juego()
            if boton_elegir.draw(screen1): # ELEGIR ARMAS
                if event.type == pygame.MOUSEBUTTONDOWN:
                    elegir_armas()
            if boton_about.draw(screen1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sobreNosotros()
            if boton_salir.draw(screen1): # SALIR DEL JUEGO
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()

def elegir_armas():
    global salir, armas, arma1, arma2
    screen2 = pygame.display.set_mode((1280, 832))
    # IMÁGENES
    armas_imagen = pygame.image.load("armas_imagen.png").convert()
    añadir = pygame.image.load('añadir.png').convert_alpha()
    jugar = pygame.image.load('jugar.png').convert_alpha()
    personaje = pygame.image.load('personaje.png').convert_alpha()
    pistola1 = pygame.image.load('pistola1.png').convert_alpha()
    pistola2 = pygame.image.load('pistola2.png').convert_alpha()
    pistola3 = pygame.image.load('pistola3.png').convert_alpha()
    metralleta1 = pygame.image.load('metralleta1.png').convert_alpha()
    metralleta2 = pygame.image.load('metralleta2.png').convert_alpha()
    metralleta3 = pygame.image.load('metralleta3.png').convert_alpha()
    escopeta1 = pygame.image.load('escopeta1.png').convert_alpha()
    escopeta2 = pygame.image.load('escopeta2.png').convert_alpha()
    escopeta3 = pygame.image.load('escopeta3.png').convert_alpha()
    cuchillo1 = pygame.image.load('cuchillo1.png').convert_alpha()
    cuchillo2 = pygame.image.load('cuchillo2.png').convert_alpha()
    cuchillo3 = pygame.image.load('cuchillo3.png').convert_alpha()
    granada1 = pygame.image.load('granada1.png').convert_alpha()
    granada2 = pygame.image.load('granada2.png').convert_alpha()
    granada3 = pygame.image.load('granada3.png').convert_alpha()
    lanzallamas1 = pygame.image.load('lanzallamas1.png').convert_alpha()
    lanzallamas2 = pygame.image.load('lanzallamas2.png').convert_alpha()
    lanzallamas3 = pygame.image.load('lanzallamas3.png').convert_alpha()
    arma_imagen1 = pygame.image.load('vacio.png').convert_alpha()
    arma_imagen2 = pygame.image.load('vacio.png').convert_alpha()
    volver_menu = pygame.image.load('volver_menu2.png').convert_alpha()
    screen2.fill(blanco)
    # BOTONES
    boton_annadir = botones.boton(115, 708, añadir, 1)
    boton_jugar = botones.boton(957, 40, jugar, 1)
    boton_personaje = botones.boton(60, 126, personaje, 1)
    boton_pistola1 = botones.boton(530, 178, pistola1, 1)
    boton_pistola2 = botones.boton(530, 178, pistola2, 1)
    boton_pistola3 = botones.boton(60, 126, pistola3, 1)
    reset_pistola = botones.boton(530, 178, pistola1, 1)
    boton_metralleta1 = botones.boton(778, 178, metralleta1, 1)
    boton_metralleta2 = botones.boton(778, 178, metralleta2, 1)
    boton_metralleta3 = botones.boton(60, 126, metralleta3, 1)
    reset_metralleta = botones.boton(778, 178, metralleta1, 1)
    boton_escopeta1 = botones.boton(1026, 178, escopeta1, 1)
    boton_escopeta2 = botones.boton(1026, 178, escopeta2, 1)
    boton_escopeta3 = botones.boton(60, 126, escopeta3, 1)
    reset_escopeta = botones.boton(1026, 178, escopeta1, 1)
    boton_cuchillo1 = botones.boton(530, 410, cuchillo1, 1)
    boton_cuchillo2 = botones.boton(530, 410, cuchillo2, 1)
    boton_cuchillo3 = botones.boton(60, 126, cuchillo3, 1)
    reset_cuchillo = botones.boton(530, 410, cuchillo1, 1)
    boton_granada1 = botones.boton(778, 410, granada1, 1)
    boton_granada2 = botones.boton(778, 410, granada2, 1)
    boton_granada3 = botones.boton(60, 126, granada3, 1)
    reset_granada = botones.boton(778, 410, granada1, 1)
    boton_lanzallamas1 = botones.boton(1026, 410, lanzallamas1, 1)
    boton_lanzallamas2 = botones.boton(1026, 410, lanzallamas2, 1)
    boton_lanzallamas3 = botones.boton(60, 126, lanzallamas3, 1)
    reset_lanzallamas = botones.boton(1026, 410, lanzallamas1, 1)
    vacio1 = botones.boton(652, 700, arma_imagen1, 1)
    vacio2 = botones.boton(810, 700, arma_imagen2, 1)
    boton_volver_menu = botones.boton(155, 49, volver_menu, 1)

    while not salir:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen2.blit(armas_imagen, [0, 0])
            boton_personaje.draw(screen2)
            vacio1.draw(screen2)
            vacio2.draw(screen2)
            # AÑADIR ARMA
            if boton_annadir.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    armas.append(seleccion)
                    if len(armas) == 1:
                        vacio1 = imprimirArmas()
                    elif len(armas) == 2:
                        vacio2 = imprimirArmas()

            # SELECCION PISTOLA
            if boton_pistola1.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = 1
                    boton_lanzallamas1 = reset_lanzallamas
                    boton_metralleta1 = reset_metralleta
                    boton_escopeta1 = reset_escopeta
                    boton_cuchillo1 = reset_cuchillo
                    boton_granada1 = reset_granada
                    boton_pistola1 = boton_pistola2
                    boton_personaje = boton_pistola3
            # SELECCION METRALLETA
            if boton_metralleta1.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = 2
                    boton_lanzallamas1 = reset_lanzallamas
                    boton_pistola1 = reset_pistola
                    boton_escopeta1 = reset_escopeta
                    boton_cuchillo1 = reset_cuchillo
                    boton_granada1 = reset_granada
                    boton_metralleta1 = boton_metralleta2
                    boton_personaje = boton_metralleta3
            # SELECCION ESCOPETA
            if boton_escopeta1.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = 3
                    boton_lanzallamas1 = reset_lanzallamas
                    boton_pistola1 = reset_pistola
                    boton_metralleta1 = reset_metralleta
                    boton_cuchillo1 = reset_cuchillo
                    boton_granada1 = reset_granada
                    boton_escopeta1 = boton_escopeta2
                    boton_personaje = boton_escopeta3
            # SELECCION CUCHILLO
            if boton_cuchillo1.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = 4
                    boton_lanzallamas1 = reset_lanzallamas
                    boton_pistola1 = reset_pistola
                    boton_metralleta1 = reset_metralleta
                    boton_escopeta1 = reset_escopeta
                    boton_granada1 = reset_granada
                    boton_cuchillo1 = boton_cuchillo2
                    boton_personaje = boton_cuchillo3
            # SELECCION GRANADA
            if boton_granada1.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = 5
                    boton_lanzallamas1 = reset_lanzallamas
                    boton_pistola1 = reset_pistola
                    boton_metralleta1 = reset_metralleta
                    boton_escopeta1 = reset_escopeta
                    boton_cuchillo1 = reset_cuchillo
                    boton_granada1 = boton_granada2
                    boton_personaje = boton_granada3
            # SELECCION LANZALLAMAS
            if boton_lanzallamas1.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = 6
                    boton_pistola1 = reset_pistola
                    boton_metralleta1 = reset_metralleta
                    boton_escopeta1 = reset_escopeta
                    boton_cuchillo1 = reset_cuchillo
                    boton_granada1 = reset_granada
                    boton_lanzallamas1 = boton_lanzallamas2
                    boton_personaje = boton_lanzallamas3
            # VOLVER AL MENÚ
            if boton_volver_menu.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    seleccion = int()
                    armas = []
                    arma1 = int()
                    arma2 = int()
                    menu()
            # EMPEZAR JUEGO
            if boton_jugar.draw(screen2):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if len(armas) > 1:
                        print('JUGANDOO')
                        arma1 = armas[0]
                        arma2 = armas[1]
                        print(arma1, arma2)
                        juego.inicio(armas)

inicio()