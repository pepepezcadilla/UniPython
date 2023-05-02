import random
import pygame

# Nivel 1 ------------------------------------------------------------------------------------------------
# CAMBIAR
class Callejon:
    def __init__(self):
        self.callejon = []
        for y in range(10):
            fila = []
            for x in range(30):
                fila.append(None)
            self.callejon.append(fila)
    
    def elementos(self):
        cantidad = 0
        for fila in self.callejon:
            cantidad += fila.count(None)
        entidades = 10 * 30 - cantidad
        return entidades


def nivel_1():
    pass


# Protagonista ------------------------------------------------------------------------------------------------
class Protagonista:
    def __init__(self, armas):
        self.armas = armas
        self.nivel_energia = 10
        self.cargador = [1]
        self.x = 0
        self.y = 5
        self.nivel_energia_total = self.nivel_energia

    def mover(self, direccion):
        # Mueve al protagonista hacia la dirección especificada
        if direccion == "arriba":
            if self.y > 0:
                self.y -= 1
        elif direccion == "abajo":
            if self.y < len(self.callejon) - 1:
                self.y += 1
        elif direccion == "izquierda":
            if self.x > 0:
                self.x -= 1
        elif direccion == "derecha":
            if self.x < len(self.callejon[0]) - 1:
                self.x += 1
        elif direccion == "diagonal_arriba_izquierda":
            if self.y > 0 and self.x > 0:
                self.y -= 1
                self.x -= 1
        elif direccion == "diagonal_arriba_derecha":
            if self.y > 0 and self.x < len(self.callejon[0]) - 1:
                self.y -= 1
                self.x += 1
        elif direccion == "diagonal_abajo_izquierda":
            if self.y < len(self.callejon) - 1 and self.x > 0:
                self.y += 1
                self.x -= 1
        elif direccion == "diagonal_abajo_derecha":
            if self.y < len(self.callejon) - 1 and self.x < len(self.callejon[0]) - 1:
                self.y += 1
                self.x += 1
        # Actualiza el callejón con la nueva posición del protagonista
        self.callejon[self.y][self.x] = self


# Armas ------------------------------------------------------------------------------------------------



class Arma:
    def __init__(self, nombre, balas, punteria_lejos, punteria_cerca, danno):
        self.nombre = nombre
        self.balas = balas
        self.punteria_lejos = punteria_lejos
        self.punteria_cerca = punteria_cerca
        self.danno = danno
        self.balas_totales = balas

    def disparar(self, callejon, protagonista):
        if self.balas > 0:
            self.balas -= 1
            distancia_cerca = False
            danno_propio = False
            contador_y = protagonista.y
            existe_alien = False

            for i in range(len(callejon[0])):
                contador_y += 1
                if contador_y == 30:
                    break
                if callejon[protagonista.x][contador_y][0] == "A":
                    if i <= 5:
                        danno_propio = True

                    if i <= 9:
                        distancia_cerca = True
                        break

                    # Ver el tema colisiones/ ver cuanto ocupa una bala
                    existe_alien = True

            if existe_alien is True:
                if distancia_cerca is True:
                    probabilidad_acierto = self.punteria_cerca
                else:
                    probabilidad_acierto = self.punteria_lejos

                if danno_propio is True:
                    protagonista.nivel_energia -= protagonista.nivel_energia_total * self.danno

                print("prob", probabilidad_acierto)
                if probabilidad_acierto >= random.randint(1, 100):
                    # Comprobar si existe un alien
                    print("¡Has acertado!")
                    return self.danno
                else:
                    print("Has fallado")
                    return 0
            else:
                print("No existen aliens")
        else:
            print("No quedan balas")
            return 0

    def recargar(self, protagonista):
        if protagonista.cargador[0] > 0:
            protagonista.cargador[0] -= 1
            self.balas = self.balas_totales // 2
        else:
            print("No quedan cargadores")


class Pistola(Arma):
    def __init__(self):
        super().__init__("Pistola", 15, 20, 80, 0.3)


class Metralleta(Arma):
    def __init__(self):
        super().__init__("Metralleta", 50, 10, 90, 0.3)


class Escopeta(Arma):
    def __init__(self):
        super().__init__("Escopeta", 5, 30, 70, 0.4)


class Cuchillo(Arma):
    def __init__(self):
        super().__init__("Cuchillo", 15, 5, 95, 0.1)


class Granada(Arma):
    def __init__(self):
        super().__init__("Granada", 2, 95, 5, 0.5)


class Lanzallamas(Arma):
    def __init__(self):
        super().__init__("Lanzallamas", 2, 85, 15, 0.6)


# Aliens ------------------------------------------------------------------------------------------------

class Alien:
    def __init__(self, energia, danno_lejos, danno_cerca, velocidad):
        self.energia = energia
        self.danno_lejos = danno_lejos
        self.danno_cerca = danno_cerca
        self.velocidad = velocidad
        if velocidad == 0.5:
            self.velocidad_casillas = 1
        elif velocidad == 1:
            self.velocidad_casillas = 2
        elif velocidad == 1.5:
            self.velocidad_casillas = 3
        self.x = 0
        self.y = 0

    def mover(self, direccion):
        # Mueve el alien hacia la dirección especificada
        if direccion == "arriba":
            for i in range(self.velocidad_casillas):
                if self.y > 0:
                    self.y -= 1
                else:
                    break
        elif direccion == "abajo":
            for i in range(self.velocidad_casillas):
                if self.y < len(self.callejon) - 1:
                    self.y += 1
                else:
                    break
        elif direccion == "izquierda":
            for i in range(self.velocidad_casillas):
                if self.x > 0:
                    self.x -= 1
                else:
                    break
        elif direccion == "diagonal_arriba_izquierda":
            for i in range(self.velocidad_casillas):
                if self.y > 0 and self.x > 0:
                    self.y -= 1
                    self.x -= 1
                else:
                    break
        elif direccion == "diagonal_abajo_izquierda":
            for i in range(self.velocidad_casillas):
                if self.y < len(self.callejon) - 1 and self.x > 0:
                    self.y += 1
                    self.x -= 1
                else:
                    break
        # Actualiza el callejón con la nueva posición del alien
        self.callejon[self.y][self.x] = self

    def ataque_mov(self, protagonista):
        protagonista.nivel_energia -= protagonista.nivel_energia * self.danno_lejos

    def ataque_contacto(self, protagonista):
        protagonista.nivel_energia -= protagonista.nivel_energia * self.danno_cerca

def apareceAlien(conjuntoaliens, calle):
    if calle.elementos() < 5:
        alien = conjuntoaliens.desencolar()
        alien.x = 30
        alien.y = random.randint(0, 9)
        calle.callejon[alien.y][alien.x] = alien


class Alien1(Alien):
    def __init__(self):
        super().__init__(40, 0.0, 1.0, 1)


class Alien2(Alien):
    def __init__(self):
        super().__init__(20, 0.05, 0.5, 0.5)


class Alien3(Alien):
    def __init__(self):
        super().__init__(30, 0.05, 0.3, 1.5)

class ColaAliens():

    def __init__(self):
        self.items=[]

    def encolar(self, alien):
        self.items.append(alien)

    def desencolar(self):
        return self.items.pop(0)
    
def aliensaleatorios(numerodealiens):
    coladealiens = ColaAliens()
    aliens = [Alien1(), Alien2(), Alien3()]
    for i in range(numerodealiens-3):
        aliens.append(random.choice([Alien1(), Alien2(), Alien3()]))
    random.shuffle(aliens)
    for alien in aliens:
        coladealiens.encolar(alien)
    return coladealiens


def turnos(calle, personaje, conjuntoaliens):
    victoria=False
    while(victoria!=True):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # Salir del juego
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                # Tecla presionada
                if evento.key == pygame.K_1:
                    armaseleccionada = personaje.armas[0]
                elif evento.key ==pygame.K_2:
                    armaseleccionada = personaje.armas[1]
                elif evento.key == pygame.K_w:
                    personaje.mover("arriba")
                elif evento.key == pygame.K_s:
                    personaje.mover("abajo")
                elif evento.key == pygame.K_a:
                    personaje.mover("izquierda")
                elif evento.key == pygame.K_d:
                    personaje.mover("abajo")
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    armaseleccionada.disparar()
        for i in (random.randint(0, 4)):
            conjuntoaliens = apareceAlien(conjuntoaliens, calle)

def inicio(armas):
    armasusables = []
    armas_disponibles = {
        1: Pistola(),
        2: Metralleta(),
        3: Escopeta(),
        4: Cuchillo(),
        5: Granada(),
        6: Lanzallamas()
    }
    for arma in armas:
        if arma in armas_disponibles:
            armasusables.append(armas_disponibles[arma])

    calle = Callejon()
    personaje = Protagonista(armasusables)
    conjuntoaliens = aliensaleatorios(random.randint(5, 15)) #Hay que hacer que el usuario pueda elegir los aliens que quiere
    conjuntoaliens = apareceAlien(conjuntoaliens, calle)
    turnos()