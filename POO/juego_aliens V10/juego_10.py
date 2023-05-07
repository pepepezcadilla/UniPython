import pygame, botones, sys, time
from pygame import mixer
import random
import json

blanco = ("#231D3A")
salir = False
armas = []
arma1 = int()
arma2 = int()

pygame.mixer.init()
pygame.mixer.music.load('musica_menu.mp3')
pygame.mixer.music.play(-1)


### JUGADOR #################################################
class Jugador:
    def __init__(self, armas):
        super().__init__()
        imagen_jugador = pygame.image.load("personaje/personaje_pistola.png").convert_alpha()
        imagen_jugador = pygame.transform.scale(imagen_jugador, (70, 70)).convert_alpha()
        self.imagen = imagen_jugador
        self.posicion_x = 100
        self.posicion_y = 100

        # ------------------------------
        self.nivel_energia = 10
        self.nivel_energia_total = self.nivel_energia
        self.armas = armas
        self.arma = self.armas[0]

    def cambiar_arma(self, cual_arma):
        if cual_arma == 1:
            self.arma = self.armas[0]
        elif cual_arma == 2:
            self.arma = self.armas[1]

    def disparar(self):
        # CAMBIAR
        global n_balas
        if self.arma.balas > 0:
            if self.arma.nombre == "Pistola":
                disparo_p = mixer.Sound('gun_sounds/shoot_pistol.wav')
                disparo_p.play()
                self.arma.balas -= 1
                n_balas.append(Bala(self.posicion_x + 80, self.posicion_y + 48, self.arma, 0.75, 0, 5000))

            elif self.arma.nombre == "Metralleta":
                disparo_m = mixer.Sound('gun_sounds/shoot_machine_gun.wav')
                disparo_m.play()
                self.arma.balas -= 5
                for i in range(5):
                    n_balas.append(
                        Bala(self.posicion_x + (90 + (30 * i)), self.posicion_y + 41, self.arma, 0.75, 0, 5000))

            elif self.arma.nombre == "Escopeta":
                disparo_e = mixer.Sound('gun_sounds/shoot_shotgun.wav')
                disparo_e.play()
                self.arma.balas -= 1
                n_balas.append(Bala(self.posicion_x + 110, self.posicion_y + 45, self.arma, 0.75, -0.2, 5000))
                n_balas.append(Bala(self.posicion_x + 110, self.posicion_y + 45, self.arma, 0.75, -0.1, 5000))
                n_balas.append(Bala(self.posicion_x + 110, self.posicion_y + 45, self.arma, 0.75, 0, 5000))
                n_balas.append(Bala(self.posicion_x + 110, self.posicion_y + 45, self.arma, 0.75, 0.1, 5000))
                n_balas.append(Bala(self.posicion_x + 110, self.posicion_y + 45, self.arma, 0.75, 0.2, 5000))

            elif self.arma.nombre == "Cuchillo":
                disparo_c = mixer.Sound('gun_sounds/shoot_knife.wav')
                disparo_c.play()
                self.arma.balas -= 1
                n_balas.append(Bala(self.posicion_x + 70, self.posicion_y + 35, self.arma, 0.55, 0, 5000))

            elif self.arma.nombre == "Granada":
                disparo_g = mixer.Sound('gun_sounds/shoot_grenade.wav')
                disparo_g.play()
                self.arma.balas -= 1
                n_balas.append(Bala(self.posicion_x + 70, self.posicion_y + 41, self.arma, 0.55, 0, 5000))

            elif self.arma.nombre == "Lanzallamas":
                disparo_l = mixer.Sound('gun_sounds/shoot_grenade.wav')
                disparo_l.play()
                self.arma.balas -= 1
                n_balas.append(Bala(self.posicion_x + 90, self.posicion_y + 20, self.arma, 0, 0, 5000))

        else:
            if self.arma.nombre == "Cuchillo" or self.arma.nombre == "Granada" or self.arma.nombre == "Lanzallamas":
                pass
            else:
                arma_sin_balas = mixer.Sound('gun_sounds/gun_without_bullets.wav')
                arma_sin_balas.play()
            # print("No quedan balas")
            # return 0

    def recargar(self):
        self.arma.recargar()

    def update(self):
        pass

    def cambiar_posicion(self, nueva_posicion_x, nueva_posicion_y):
        global protagonista
        if protagonista.posicion_x < 0:
            nueva_posicion_x = 0.2

        elif protagonista.posicion_x > 1210:
            nueva_posicion_x = -0.2

        if protagonista.posicion_y < 0:
            nueva_posicion_y = 0.2

        elif protagonista.posicion_y > 715:
            nueva_posicion_y = -0.2
        self.posicion_x += nueva_posicion_x
        self.posicion_y += nueva_posicion_y

    def imprimir_jugador(self):
        global ventana
        hitbox_j = self.colision()
        ventana.blit(self.imagen, hitbox_j)

    def colision(self):
        hitbox_j_c = self.imagen.get_rect()
        hitbox_j_c.x = self.posicion_x
        hitbox_j_c.y = self.posicion_y
        return hitbox_j_c


### ARMAS #################################################
class Arma:
    def __init__(self, nombre, balas, danno, tiempo_entre_disparos, img_bala, img_arma):
        self.nombre = nombre
        self.balas = balas
        self.danno = danno
        self.balas_totales = balas
        self.tiempo_entre_disparos = tiempo_entre_disparos
        self.img_bala = img_bala
        self.img_arma = img_arma

    def recargar(self):
        global cargador
        if cargador[0] > 0:
            cargador[0] -= 1
            self.balas = self.balas_totales // 2
            # Poner sonidos recargando el arma
            if self.nombre == "Pistola":
                recargar_p = mixer.Sound('gun_sounds/reload_pistol.wav')
                recargar_p.play()
            elif self.nombre == "Metralleta":
                recargar_m = mixer.Sound('gun_sounds/reload_machine_gun.wav')
                recargar_m.play()
            elif self.nombre == "Escopeta":
                recargar_e = mixer.Sound('gun_sounds/reload_shotgun.wav')
                recargar_e.play()
            elif self.nombre == "Cuchillo":
                pass
            elif self.nombre == "Granada":
                pass
            elif self.nombre == "Lanzallamas":
                pass

        else:
            pass
            # print("No quedan cargadores")


class Pistola(Arma):
    def __init__(self):
        img_bala_p = pygame.image.load("balas/bala_pistola.png").convert_alpha()
        img_bala_p = pygame.transform.scale(img_bala_p, (10, 7)).convert_alpha()

        img_arma_p = pygame.image.load("balas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_p = pygame.transform.scale(img_arma_p, (50, 50)).convert_alpha()
        super().__init__("Pistola", 15, 0.3, 0.2, img_bala_p, img_arma_p)


class Metralleta(Arma):
    def __init__(self):
        img_bala_m = pygame.image.load("balas/bala_metralleta.png").convert_alpha()
        img_bala_m = pygame.transform.scale(img_bala_m, (24, 10)).convert_alpha()
        # img_bala_m = pygame.image.load("PistolAmmoBig.png").convert_alpha()
        # img_bala_m = pygame.transform.scale(img_bala_m, (20, 20)).convert_alpha()

        img_arma_m = pygame.image.load("balas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_m = pygame.transform.scale(img_arma_m, (50, 50)).convert_alpha()
        super().__init__("Metralleta", 50, 0.2, 0.3, img_bala_m, img_arma_m)


class Escopeta(Arma):
    def __init__(self):
        img_bala_e = pygame.image.load("balas/ficha_blanco_72x72.png").convert_alpha()
        img_bala_e = pygame.transform.scale(img_bala_e, (10, 10)).convert_alpha()

        img_arma_e = pygame.image.load("armas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_e = pygame.transform.scale(img_arma_e, (50, 50)).convert_alpha()
        super().__init__("Escopeta", 5, 0.2, 0.3, img_bala_e, img_arma_e)


class Cuchillo(Arma):
    def __init__(self):
        img_bala_c = pygame.image.load("balas/bala_cuchillo.png").convert_alpha()
        img_bala_c = pygame.transform.scale(img_bala_c, (44, 12)).convert_alpha()

        img_arma_c = pygame.image.load("balas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_c = pygame.transform.scale(img_arma_c, (20, 20)).convert_alpha()
        super().__init__("Cuchillo", 15, 0.1, 0.3, img_bala_c, img_arma_c)


class Granada(Arma):
    def __init__(self):
        img_bala_g = pygame.image.load("balas/bala_granada.png").convert_alpha()
        img_bala_g = pygame.transform.scale(img_bala_g, (20, 26)).convert_alpha()

        img_arma_g = pygame.image.load("armas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_g = pygame.transform.scale(img_arma_g, (50, 50)).convert_alpha()
        super().__init__("Granada", 2, 1.0, 0.5, img_bala_g, img_arma_g)


class Fragmentos(Arma):
    def __init__(self):
        img_bala_p = pygame.image.load("balas/ficha_rojo_72x72.png").convert_alpha()
        img_bala_p = pygame.transform.scale(img_bala_p, (20, 20)).convert_alpha()

        img_arma_p = pygame.image.load("armas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_p = pygame.transform.scale(img_arma_p, (50, 50)).convert_alpha()
        super().__init__("Fragmentos", 15, 0.1, 0.3, img_bala_p, img_arma_p)


class Lanzallamas(Arma):
    def __init__(self):
        img_bala_p = pygame.image.load("balas/bala_lanzallamas.png").convert_alpha()
        img_bala_p = pygame.transform.scale(img_bala_p, (120, 65)).convert_alpha()

        img_arma_p = pygame.image.load("armas/ficha_rojo_72x72.png").convert_alpha()
        img_arma_p = pygame.transform.scale(img_arma_p, (50, 50)).convert_alpha()
        super().__init__("Lanzallamas", 15, 1, 0.3, img_bala_p, img_arma_p)


class Mina(Arma):
    def __init__(self):
        img_mina = pygame.image.load("balas/ficha_rojo_72x72.png").convert_alpha()
        img_mina = pygame.transform.scale(img_mina, (30, 30)).convert_alpha()
        super().__init__("Mina", 5, 1, 0, img_mina, img_mina)


### BALAS #################################################
class Bala:
    def __init__(self, posicion_x, posicion_y, n_arma, cx, cy, t_bala):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.n_arma = n_arma
        self.cx = cx
        self.cy = cy

        self.posicion_x_inicial = posicion_x
        self.posicion_y_inicial = posicion_y
        self.t_bala = t_bala

    def mover_bala(self):
        """if self.n_arma.nombre == "Escopeta":
            print("Esco")
            img_1 = self.imagen_bala
            img_2 = self.imagen_bala
            img_3 = self.imagen_bala
            self.posicion_x += 0.75
            balin_x = self.posicion_x
            balin_y = self.posicion_y
            # Balin 1
            hit_box_bala_1 = img_1.get_rect()
            hit_box_bala_1.x = balin_x
            hit_box_bala_1.y = balin_y - 0.2
            #ventana.blit(img_1, hit_box_bala_1)
            # Balin 2
            hit_box_bala_2 = img_2.get_rect()
            hit_box_bala_2.x = balin_x
            hit_box_bala_2.y = balin_y
            #ventana.blit(img_2, hit_box_bala_2)
            # Balin 3
            hit_box_bala_3 = img_3.get_rect()
            hit_box_bala_3.x = balin_x
            hit_box_bala_3.y = balin_y + 0.2
            ventana.blit(img_3, hit_box_bala_3)
        else:"""
        if self.n_arma.nombre == "Lanzallamas":
            global protagonista
            self.posicion_x = protagonista.posicion_x + 90
            self.posicion_y = protagonista.posicion_y + 20
            hit_box_bala = self.colisiones_bala()
            ventana.blit(self.n_arma.img_bala, hit_box_bala)
        else:
            self.posicion_x += self.cx
            self.posicion_y += self.cy
            if self.posicion_x - self.posicion_x_inicial >= self.t_bala or \
                    self.posicion_x - self.posicion_x_inicial <= -self.t_bala or \
                    self.posicion_y - self.posicion_y_inicial >= self.t_bala or \
                    self.posicion_y - self.posicion_y_inicial <= -self.t_bala:
                self.posicion_x = 2000
                self.posicion_y = 2000

            hit_box_bala = self.colisiones_bala()
            ventana.blit(self.n_arma.img_bala, hit_box_bala)

    def colisiones_bala(self):
        imagen_bala = self.n_arma.img_bala.get_rect()
        imagen_bala.x = self.posicion_x
        imagen_bala.y = self.posicion_y
        return imagen_bala


### ALIENS #################################################
class Alien:
    def __init__(self, energia, danno_lejos, danno_cerca, velocidad, imagen_alien, imagen_alien_2,
                 img_alien_25, img_alien_50, img_alien_100):
        self.energia = energia
        self.energia_total = energia
        self.danno_lejos = danno_lejos
        self.danno_cerca = danno_cerca
        self.velocidad = velocidad
        self.imagen_alien = imagen_alien
        self.imagen_alien_1 = imagen_alien
        self.imagen_alien_2 = imagen_alien_2

        self.img_alien_25 = img_alien_25
        self.img_alien_50 = img_alien_50
        self.img_alien_100 = img_alien_100

        self.posicion_alien_x = -100
        self.posicion_alien_y = -100
        self.imagen_alien = imagen_alien

    def cambiar_imagen(self, n_imagen):
        if n_imagen == 1:
            self.imagen_alien = self.imagen_alien_1
        elif n_imagen == 2:
            self.imagen_alien = self.imagen_alien_2

    def posicionar_alien(self):
        hitbox_a = self.hitbox_alien()
        ventana.blit(self.imagen_alien, hitbox_a)

    def hitbox_alien(self):
        if self.energia <= ((25 * self.energia_total) / 100):
            self.imagen_alien = self.img_alien_25

        elif self.energia <= ((50 * self.energia_total) / 100):
            self.imagen_alien = self.img_alien_50

        elif self.energia == self.energia_total:
            self.imagen_alien = self.img_alien_100

        hitbox_a_c = self.imagen_alien.get_rect()
        hitbox_a_c.x = self.posicion_alien_x
        hitbox_a_c.y = self.posicion_alien_y
        return hitbox_a_c

    def mover_alien(self):
        self.posicion_alien_x += -self.velocidad
        self.posicion_alien_y += 0

        n_random = random.randint(0, 10000)
        if n_random <= 1:
            self.posicion_alien_y += -50

        elif n_random <= 3:
            self.posicion_alien_y += 50

        # Poner limites aliens
        if self.posicion_alien_y <= 0:
            self.posicion_alien_y = 0
        if self.posicion_alien_y >= 721:
            self.posicion_alien_y = 725

    """def mover(self):
        # CAMBIAR
        # Se mueve el alien recto o diagonal
        self.x += self.velocidad
        if random.random() < 0.5:
            self.y += self.velocidad

        if self.y < 0:
            self.y = 0
        elif self.y > 10:
            self.y = 10
        if self.x > 50:
            self.x = 50

    def ataque_mov(self):
        protagonista.nivel_energia -= protagonista.nivel_energia * self.danno_lejos

    def ataque_contacto(self):
        protagonista.nivel_energia -= protagonista.nivel_energia * self.danno_cerca"""


class Alien1(Alien):
    def __init__(self):
        img_alien_1 = pygame.image.load("zombie/zombie1 100_.png").convert_alpha()
        img_alien_1 = pygame.transform.scale(img_alien_1, (70, 70)).convert_alpha()

        img_alien_1_2 = img_alien_1

        img_alien_1_a = pygame.image.load("zombie/zombie1 25_.png").convert_alpha()
        img_alien_1_a = pygame.transform.scale(img_alien_1_a, (70, 70)).convert_alpha()

        img_alien_1_b = pygame.image.load("zombie/zombie1 50_.png").convert_alpha()
        img_alien_1_b = pygame.transform.scale(img_alien_1_b, (70, 70)).convert_alpha()

        img_alien_1_c = pygame.image.load("zombie/zombie1 100_.png").convert_alpha()
        img_alien_1_c = pygame.transform.scale(img_alien_1_c, (70, 70)).convert_alpha()

        super().__init__(40, 0.0, 1.0, 0.1, img_alien_1, img_alien_1_2, img_alien_1_a, img_alien_1_b, img_alien_1_c)


class Alien2(Alien):
    def __init__(self):
        img_alien_2 = pygame.image.load("zombie/zombie2 100_.png").convert_alpha()
        img_alien_2 = pygame.transform.scale(img_alien_2, (70, 70)).convert_alpha()

        img_alien_2_2 = img_alien_2

        img_alien_2_a = pygame.image.load("zombie/zombie2 25_.png").convert_alpha()
        img_alien_2_a = pygame.transform.scale(img_alien_2_a, (70, 70)).convert_alpha()

        img_alien_2_b = pygame.image.load("zombie/zombie2 50_.png").convert_alpha()
        img_alien_2_b = pygame.transform.scale(img_alien_2_b, (70, 70)).convert_alpha()

        img_alien_2_c = pygame.image.load("zombie/zombie2 100_.png").convert_alpha()
        img_alien_2_c = pygame.transform.scale(img_alien_2_c, (70, 70)).convert_alpha()

        super().__init__(20, 0.05, 0.5, 0.05, img_alien_2, img_alien_2_2, img_alien_2_a, img_alien_2_b, img_alien_2_c)


class Alien3(Alien):
    def __init__(self):
        img_alien_3 = pygame.image.load("zombie/zombie3 100_.png").convert_alpha()
        img_alien_3 = pygame.transform.scale(img_alien_3, (70, 70)).convert_alpha()

        img_alien_3_2 = img_alien_3

        img_alien_3_a = pygame.image.load("zombie/zombie3 25_.png").convert_alpha()
        img_alien_3_a = pygame.transform.scale(img_alien_3_a, (70, 70)).convert_alpha()

        img_alien_3_b = pygame.image.load("zombie/zombie3 50_.png").convert_alpha()
        img_alien_3_b = pygame.transform.scale(img_alien_3_b, (70, 70)).convert_alpha()

        img_alien_3_c = pygame.image.load("zombie/zombie3 100_.png").convert_alpha()
        img_alien_3_c = pygame.transform.scale(img_alien_3_c, (70, 70)).convert_alpha()

        super().__init__(30, 0.05, 0.3, 0.2, img_alien_3, img_alien_3_2, img_alien_3_a, img_alien_3_b, img_alien_3_c)


### JUEGO #################################################
def videojuego(arma1, arma2, v_n_aliens, v_t_l_aliens, v_n_cargador, nivel):
    # arma1 = arma numero 1 de la protagonista
    # arma1 = arma numero 2 de la protagonista
    # v_n_aliens = numero de aliens que se van a generar
    # v_t_l_aliens = el tiempo que tardaran los aliens en hacer su daño lejano
    # v_n_cargador = cuantos cargadores abra
    # nivel = nivel actual

    global protagonista, ventana, cargador, n_balas, n_aliens
    pygame.init()
    ancho_ventana = 1280
    alto_ventana = 790
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))

    pygame.display.set_caption("Zombies killer")

    # Fondo del juego
    fondo = pygame.Surface((1280, 790))
    fondo.fill((80, 97, 48))

    # Puntuacion y fonts
    puntuacion = 0
    fuente_puntuacion = pygame.font.Font("public-pixel-font\PublicPixel-z84yD.ttf", 32)

    fuente_puntuacion_maxima = pygame.font.Font("public-pixel-font\PublicPixel-z84yD.ttf", 32)

    game_over = pygame.font.Font("public-pixel-font\PublicPixel-z84yD.ttf", 48)

    jugar_de_nuevo = pygame.font.Font("public-pixel-font\PublicPixel-z84yD.ttf", 24)

    salir = pygame.font.Font("public-pixel-font\PublicPixel-z84yD.ttf", 28)

    fuente_nivel = pygame.font.Font("public-pixel-font\PublicPixel-z84yD.ttf", 28)

    # JUEGO PAUSADO
    fondo_pausa = pygame.image.load("pausa.png").convert()

    # pygame.mixer.music.load('musica_fondo_2.mp3')
    # Reproduce la música
    # pygame.mixer.music.play(-1)

    # Crear protagonista con las armas elegidas
    lista_armas = [0, Pistola(), Metralleta(), Escopeta(), Cuchillo(), Granada(), Lanzallamas()]
    protagonista = Jugador([lista_armas[arma1], lista_armas[arma2]])
    """mi_sprite = Jugador()
    grupo_sprites = pygame.sprite.Group()
    grupo_sprites.add(mi_sprite)"""
    # Sprites Jugador
    """img_jugador = pygame.image.load("ficha_blanco_72x72.png").convert_alpha()
    img_jugador = pygame.transform.scale(img_jugador, (70, 70)).convert_alpha()

    img_jugador_w = pygame.image.load("ficha_amarillo_72x72.png").convert_alpha()
    img_jugador_w = pygame.transform.scale(img_jugador_w, (70, 70)).convert_alpha()

    img_jugador_a = pygame.image.load("ficha_rojo_72x72.png").convert_alpha()
    img_jugador_a = pygame.transform.scale(img_jugador_a, (70, 70)).convert_alpha()

    img_jugador_s = pygame.image.load("ficha_gris_72x72.png").convert_alpha()
    img_jugador_s = pygame.transform.scale(img_jugador_s, (70, 70)).convert_alpha()

    img_jugador_d = pygame.image.load("ficha_azul_72x72.png").convert_alpha()
    img_jugador_d = pygame.transform.scale(img_jugador_d, (70, 70)).convert_alpha()"""

    img_jugador = [0]
    for i in range(2):
        nombre_arma_actual = protagonista.armas[i].nombre
        if nombre_arma_actual == "Pistola":
            img_j = pygame.image.load("personaje/personaje_pistola.png").convert_alpha()
            img_j = pygame.transform.scale(img_j, (70, 80)).convert_alpha()
            img_j = pygame.transform.rotate(img_j, 90).convert_alpha()
            img_jugador.append(img_j)
        elif nombre_arma_actual == "Metralleta":
            img_j = pygame.image.load("personaje/personaje_metralleta.png").convert_alpha()
            img_j = pygame.transform.scale(img_j, (70, 90)).convert_alpha()
            img_j = pygame.transform.rotate(img_j, 90).convert_alpha()
            img_jugador.append(img_j)
        elif nombre_arma_actual == "Escopeta":
            img_j = pygame.image.load("personaje/personaje_escopeta.png").convert_alpha()
            img_j = pygame.transform.scale(img_j, (70, 110)).convert_alpha()
            img_j = pygame.transform.rotate(img_j, 90).convert_alpha()
            img_jugador.append(img_j)
        elif nombre_arma_actual == "Cuchillo":
            img_j = pygame.image.load("personaje/personaje_cuchillo.png").convert_alpha()
            img_j = pygame.transform.scale(img_j, (70, 70)).convert_alpha()
            img_j = pygame.transform.rotate(img_j, 90).convert_alpha()
            img_jugador.append(img_j)
        elif nombre_arma_actual == "Granada":
            img_j = pygame.image.load("personaje/personaje_granada.png").convert_alpha()
            img_j = pygame.transform.scale(img_j, (70, 70)).convert_alpha()
            img_j = pygame.transform.rotate(img_j, 90).convert_alpha()
            img_jugador.append(img_j)
        elif nombre_arma_actual == "Lanzallamas":
            img_j = pygame.image.load("personaje/personaje_lanzallamas.png").convert_alpha()
            img_j = pygame.transform.scale(img_j, (70, 90)).convert_alpha()
            img_j = pygame.transform.rotate(img_j, 90).convert_alpha()
            img_jugador.append(img_j)

    protagonista.imagen = img_jugador[1]
    keys_pressed = set()

    # Configuraciones Aliens
    def generar_aliens(numero_aliens_g):
        for i in range(numero_aliens_g):
            tipo_aliens = [Alien1(), Alien2(), Alien3()]
            n_aliens.append(random.choice(tipo_aliens))

    def meter_aliens(n_meter_a):
        numeros_columna = random.sample(range(1, 5), n_meter_a)
        posicion_columna = [0, [1250, 50], [1250, 200], [1250, 350], [1250, 500], [1250, 700]]
        for i in range(n_meter_a):
            if numero_aliens[0] >= len(n_aliens):
                break
            posicion_final = posicion_columna[numeros_columna[i]]
            n_aliens[numero_aliens[0]].posicion_alien_x = posicion_final[0]
            n_aliens[numero_aliens[0]].posicion_alien_y = posicion_final[1]
            n_aliens_j.append(n_aliens[numero_aliens[0]])

            numero_aliens[0] += 1

    numero_aliens_vivos = [v_n_aliens]
    numero_aliens = [0]
    n_aliens = []
    n_aliens_j = []
    generar_aliens(v_n_aliens)

    # Configuraciones varias
    # clock = pygame.time.Clock()
    cargador = [v_n_cargador]  # Cuantos cargadores hay
    n_balas = []  # Cada vez que se dispara se mete la instancia de la bala en esta lista
    juego_pausado = False  # Si "juego_pausado" es True se ha pausado el juego
    juego_terminado = 0  # Si "juego_terminado" es True se ha terminado el juego
    recargando = False  # Si "recargando" es True se esta recargando un arma impidiendole disparar

    for u in range(nivel + 1):
        n_balas.append(Bala(random.randint(50, 1200), random.randint(50, 750), Mina(), 0, 0, 1000))
    """
    # Configuracion cursor
    pygame.mouse.set_visible(False)
    cursor_imagen = pygame.image.load('cursor.png').convert_alpha()
    cursor_imagen = pygame.transform.scale(cursor_imagen, (20, 20)).convert_alpha()"""
    pygame.mouse.set_visible(False)  # Cursor invisible

    # Contadores
    tiempo_disparo = 0  # Para que tenga que esperar a la hora de disparar
    tiempo_recargando = 0  # Contador para recargar
    tiempo_de_recarga = 0  # Cuanto tiempo va a durar la recarga
    tiempo_meter_aliens = 0  # Contador para ir metiendo aliens
    tiempo_cada_aliens = 4  # Cada cuanto tiempo se va metiendo los aliens
    tiempo_lejano_alien = time.time()  # Contador para "disparo lejano" del alien
    tiempo_lejano_alien_c = v_t_l_aliens  # Cada cuanto tiempo va a "disparar" el alien
    lejano_aliens = True
    tiempo_animacion_alien = 0
    tiempo_animacion_alien_c = 0.7
    animacion_aliens = True
    animacion_imagen = 2

    with open("stats.json", "r+") as f:
        data = json.load(f)

        while True:
            if juego_pausado is False and juego_terminado == 0:

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                    if evento.type == pygame.KEYDOWN:
                        keys_pressed.add(evento.key)
                        if evento.key == pygame.K_ESCAPE:
                            if juego_pausado is False:
                                juego_pausado = True
                                pygame.mouse.set_visible(True)
                            else:
                                juego_pausado = False
                                pygame.mouse.set_visible(False)

                        if evento.key == pygame.K_r:
                            if cargador[0] > 0:
                                recargando = True
                                nombre_arma_recargando = protagonista.arma.nombre
                                protagonista.recargar()
                                tiempo_recargando = time.time()
                                if nombre_arma_recargando == "Pistola":
                                    tiempo_de_recarga = 0.5
                                elif nombre_arma_recargando == "Metralleta":
                                    tiempo_de_recarga = 1.7
                                elif nombre_arma_recargando == "Escopeta":
                                    tiempo_de_recarga = 2
                                elif nombre_arma_recargando == "Cuchillo":
                                    tiempo_de_recarga = 0.5
                                elif nombre_arma_recargando == "Granada":
                                    tiempo_de_recarga = 0.5
                                elif nombre_arma_recargando == "Lanzallamas":
                                    tiempo_de_recarga = 0.5

                        """if evento.key == pygame.K_SPACE:
                            protagonista.disparar()"""

                        if evento.key == pygame.K_1:
                            protagonista.cambiar_arma(1)
                            protagonista.imagen = img_jugador[1]
                        elif evento.key == pygame.K_2:
                            protagonista.cambiar_arma(2)
                            protagonista.imagen = img_jugador[2]
                    if evento.type == pygame.KEYUP:
                        keys_pressed.discard(evento.key)

                if recargando is True:
                    tiempo_actual = time.time()
                    if tiempo_actual - tiempo_recargando > tiempo_de_recarga:
                        recargando = False
                        tiempo_disparo = tiempo_actual
                else:
                    keys_get_pressed = pygame.key.get_pressed()
                    if keys_get_pressed[pygame.K_SPACE]:
                        tiempo_actual = time.time()
                        if tiempo_actual - tiempo_disparo > protagonista.arma.tiempo_entre_disparos:
                            protagonista.disparar()
                            tiempo_disparo = tiempo_actual

                # Se carga el fondo
                ventana.blit(fondo, (0, 0))

                # Movimiento Jugador
                nueva_coor_x = 0
                nueva_coor_y = 0

                protagonista.imagen = protagonista.imagen
                if pygame.K_w in keys_pressed and pygame.K_s not in keys_pressed:
                    nueva_coor_y = -0.5
                    # protagonista.imagen = img_jugador_w
                if pygame.K_a in keys_pressed and pygame.K_d not in keys_pressed:
                    nueva_coor_x = -0.5
                    # protagonista.imagen = img_jugador_a
                if pygame.K_d in keys_pressed and pygame.K_a not in keys_pressed:
                    nueva_coor_x = 0.5
                    # protagonista.imagen = img_jugador_d
                if pygame.K_s in keys_pressed and pygame.K_w not in keys_pressed:
                    nueva_coor_y = 0.5
                    # protagonista.imagen = img_jugador_s
                # Limite del jugador
                if protagonista.posicion_x < 0 or protagonista.posicion_x > 1210:
                    nueva_coor_x = 0
                if protagonista.posicion_y < 0 or protagonista.posicion_y > 715:
                    nueva_coor_y = 0

                # Mover e imprimir al jugador
                protagonista.cambiar_posicion(nueva_coor_x, nueva_coor_y)
                protagonista.imprimir_jugador()

                # Meter aliens
                tiempo_actual = time.time()
                if tiempo_actual - tiempo_meter_aliens > tiempo_cada_aliens:
                    n_random = random.randint(2, 4)
                    meter_aliens(n_random)
                    tiempo_meter_aliens = tiempo_actual

                # Comprobar si se puede hacer el ataque lejano el cual es cada cierto daño
                tiempo_actual = time.time()
                if tiempo_actual - tiempo_lejano_alien > tiempo_lejano_alien_c:
                    lejano_aliens = True
                    tiempo_lejano_alien = tiempo_actual

                if tiempo_actual - tiempo_animacion_alien > tiempo_animacion_alien_c:
                    animacion_aliens = True
                    if animacion_imagen == 1:
                        animacion_imagen = 2
                    elif animacion_imagen == 2:
                        animacion_imagen = 1
                    tiempo_animacion_alien = tiempo_actual

                for alien_actual in n_aliens_j:
                    if animacion_aliens is True:
                        if animacion_imagen == 1:
                            # alien_actual.cambiar_imagen(1)
                            pass
                        elif animacion_imagen == 2:
                            # alien_actual.cambiar_imagen(2)
                            pass

                    alien_actual.mover_alien()
                    alien_actual.posicionar_alien()
                    # El alien impacta contra la protagonista
                    if protagonista.colision().colliderect(alien_actual.hitbox_alien()):
                        protagonista.nivel_energia -= protagonista.nivel_energia_total * alien_actual.danno_cerca
                        n_aliens_j.remove(alien_actual)
                        numero_aliens_vivos[0] -= 1
                        danno_p = mixer.Sound('personaje/minecraft-damage.wav')
                        danno_p.play()

                    # El alien ha sobrepasado a la protagonista
                    if alien_actual.posicion_alien_x <= protagonista.posicion_x:
                        protagonista.nivel_energia -= protagonista.nivel_energia_total * alien_actual.danno_cerca
                        n_aliens_j.remove(alien_actual)
                        numero_aliens_vivos[0] -= 1
                        danno_p = mixer.Sound('personaje/minecraft-damage.wav')
                        danno_p.play()

                    # Daño lejano al protagonista
                    if lejano_aliens is True:
                        protagonista.nivel_energia -= protagonista.nivel_energia_total * alien_actual.danno_lejos
                        print("Lejos", protagonista.nivel_energia)

                lejano_aliens = False
                animacion_aliens = False

                # Se comprueba si exiten balas y se comprueba la colision con los aliens
                for bala_actual in n_balas:
                    bala_actual.mover_bala()
                    if bala_actual.posicion_x >= 1300 or bala_actual.posicion_y <= 0 or bala_actual.posicion_y >= 800 \
                            or bala_actual.posicion_x <= 0:
                        n_balas.remove(bala_actual)
                        continue

                    # La protagonista le una bala propia
                    if protagonista.colision().colliderect(bala_actual.colisiones_bala()):
                        print("Autodaño")
                        protagonista.nivel_energia -= protagonista.nivel_energia_total * bala_actual.n_arma.danno
                        n_balas.remove(bala_actual)
                        continue
                    for alien_actual in n_aliens_j:
                        if alien_actual.hitbox_alien().colliderect(bala_actual.colisiones_bala()):
                            alien_actual.energia -= alien_actual.energia_total * bala_actual.n_arma.danno
                            if alien_actual.energia <= 0:
                                n_aliens_j.remove(alien_actual)
                                numero_aliens_vivos[0] -= 1

                                if alien_actual.energia_total == 40:
                                    puntuacion += 10
                                elif alien_actual.energia_total == 20:
                                    puntuacion += 20
                                elif alien_actual.energia_total == 30:
                                    puntuacion += 30

                            if bala_actual.n_arma.nombre == "Granada":
                                explosion = mixer.Sound('gun_sounds/grenade_explosion.wav')
                                explosion.play()
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), 0, -0.75, 450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), 0.75, -0.75,
                                         450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), 0.75, 0, 450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), 0.75, 0.75, 450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), 0, 0.75, 450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), -0.75, 0.75,
                                         450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), -0.75, 0, 450))
                                n_balas.append(
                                    Bala(bala_actual.posicion_x, bala_actual.posicion_y, Fragmentos(), -0.75, -0.75,
                                         450))
                            try:
                                n_balas.remove(bala_actual)
                            except:
                                print("ERROR")
                                pass

                if protagonista.nivel_energia <= 0:
                    print("MUERTO", protagonista.nivel_energia)
                    juego_terminado = 1

                # print(numero_aliens_vivos[0], len(n_aliens), numero_aliens)
                if numero_aliens_vivos[0] <= 0:
                    print("GANADOR", protagonista.nivel_energia)
                    juego_terminado = 2

                # pygame.time.wait(1000)
                # clock.tick(60)

                """# Cargar cursor
                cursor_x, cursor_y = pygame.mouse.get_pos()
                ventana.blit(cursor_imagen, (cursor_x, cursor_y))"""

                ventana.blit(fuente_puntuacion_maxima.render(f"Max puntuacion: {data['puntuacion_maxima']}", True,
                                                             (255, 255, 255)), (10, 10))
                ventana.blit(fuente_puntuacion.render(f"Puntuacion: {puntuacion}", True, (255, 255, 255)), (800, 10))
                pygame.display.update()




            elif juego_pausado is True:
                ventana.blit(fondo_pausa, (0, 0))
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        sys.exit()
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if 808 <= evento.pos[0] <= 1025 and 217 <= evento.pos[1] <= 293: # REANUDAR
                            juego_pausado = False
                        if 808 <= evento.pos[0] <= 1025 and 349 <= evento.pos[1] <= 425: # SALIR
                            menu()
                        if 830 <= evento.pos[0] <= 886 and 491 <= evento.pos[1] <= 545:  # SONIDO OFF
                            pygame.mixer.music.pause()
                        if 982 <= evento.pos[0] <= 1034 and 491 <= evento.pos[1] <= 545:  # SONIDO ON
                            pygame.mixer.music.unpause()



                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_ESCAPE:
                            if juego_pausado is False:
                                juego_pausado = True
                                pygame.mouse.set_visible(True)
                            else:
                                juego_pausado = False
                                pygame.mouse.set_visible(False)

                pygame.display.update()


            elif juego_terminado == 1:

                if puntuacion > data["puntuacion_maxima"]:
                    data["puntuacion_maxima"] = puntuacion

                f.seek(0)

                json.dump(data, f)

                f.truncate()

                ventana.fill((0, 0, 0))

                ventana.blit(game_over.render("Has muerto", True, (255, 255, 255)), (370, 220))

                ventana.blit(jugar_de_nuevo.render("Presiona ENTER para jugar de nuevo", True, (255, 255, 255)),

                             (250, 500))

                ventana.blit(salir.render(f"Presiona ESC para salir", True, (255, 255, 255)), (315, 650))

                for evento in pygame.event.get():

                    if evento.type == pygame.KEYDOWN:

                        if evento.key == pygame.K_RETURN:

                            v_n_aliens = 2

                            videojuego(arma1, arma2, v_n_aliens, v_t_l_aliens, v_n_cargador, 1)


                        elif evento.key == pygame.K_ESCAPE:

                            exit()

                    pygame.display.update()


            elif juego_terminado == 2:
                ventana.fill((0, 0, 0))
                ventana.blit(fuente_nivel.render(f"Nivel {nivel + 1}", True, (255, 255, 255)), (500, 300))
                ventana.blit(jugar_de_nuevo.render("Presiona ENTER para ir al siguiente nivel", True, (255, 255, 255)),
                             (150, 500))

                for evento in pygame.event.get():
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            videojuego(arma1, arma2, v_n_aliens + 2, v_t_l_aliens, v_n_cargador, nivel + 1)

                pygame.display.update()


### INTERFAZ #################################################
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
                    videojuego(arma1, arma2, 2, 2, 1, 1)

inicio()