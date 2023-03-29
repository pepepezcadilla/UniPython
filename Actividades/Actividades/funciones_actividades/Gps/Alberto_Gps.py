#Importamos varias librerías, para acceder a internet, para cálculos, etc.
import requests #Hay que instalar esta librería, cmd en la carpeta "Python\Python310\Scripts", pip install requests
import json
import random
import time
from math import acos, cos, sin, radians
from geopy.geocoders import Nominatim #Hay que instalar esta librería, cmd en la carpeta "Python\Python310\Scripts", pip install geopy
from geopy.distance import geodesic
#import gpsd  ##esto es en caso de que el dispositivo tenga gps

#Función para calcular la distancia entre dos coordenadas.
def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))

    distancia = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1] - punto_2[1]))

    return distancia * 6371.01

#Estas lineas son para usar el paquete Gpsd, en caso de que nuestro dispositivo tenga GPS
##gpsd.connect()
##paquete=gpsd.get_current()
##localizaciob=paquete.position()

#Con estas línas conseguimos nuestra ip pública 
response = requests.get('https://api.ipify.org/?format=json')
data = response.json()
ip_address = data['ip']

#Con estas líneas geolocalizamos nuestra ip pública
response = requests.get(f'https://ipapi.co/{ip_address}/json/')
data = json.loads(response.text)

latitude = data['latitude']
longitude = data['longitude']

#las líneas anteriores son para obtener una localización estimada de dónde se encuentra el equipoautomáticamente, se pueden obviar y 
#establecer por teclado la latitud y la longitud

#Inicializa el objeto de geocodificación con la opción de OpenStreetMap Nominatim
geolocalizador = Nominatim(user_agent='TFMAlgorhitms')

#Define la dirección que quieres buscar
direccion = 'Calle de Alcalá 1 28014 Madrid España'

#Envía una solicitud de geocodificación para obtener las coordenadas de la dirección
resultado = geolocalizador.geocode(direccion)

#Extraemos las coordenadas de la respuesta
latitud = round(resultado.latitude, 4)
longitud = round(resultado.longitude, 4)

#Inicializamos las variables.
inicio=[round(latitude,4), round(longitude, 4)]
actual=inicio
anterior = actual
final=[latitud, longitud]
tiempo=0
distancia=0
distanciatotal=distancia_puntos(inicio, final)

#Creamos un bucle para simular que el equipo se está moviendo, modificando las coordenadas actuales
while(actual!=final):
    if(actual[0]!=final[0]):
        if(actual[0]>final[0]):
            aleat=random.randint(5, 10)/10000
            actual[0] -= aleat
        elif(actual[0]<final[0]):
            aleat=random.randint(5, 10)/10000
            actual[0] += aleat
    if(actual[1]!=final[1]):
        if(actual[1]>final[1]):
            aleat=random.randint(5, 10)/10000
            actual[1] -= aleat
        elif(actual[1]<final[1]):
            aleat=random.randint(5, 10)/10000
            actual[1] += aleat
    
    #Redondeamos las coordenadas para que tengan 4 decimales
    actual[0]=round(actual[0], 4)
    actual[1]=round(actual[1], 4)

    #Esperamos un tiempo aleatorio, para que la "carrera" no sea constante
    espera=random.randint(1, 3)
    time.sleep(espera)
    tiempo+=espera

    #Calculamos la distancia que hemos recorrido en esta iteración
    distancia_actual=distancia_puntos(actual, final)
    distancia_iteracion = distanciatotal-distancia_actual
    
    #Actualizamos distancia recorrida y tiempo total
    distancia += distancia_iteracion
    
    #Calculamos velocidad y ritmo actuales
    velocidad_actual = distancia_iteracion / espera
    if(distancia==0):
        ritmo_actual=0
    else:
        ritmo_actual = tiempo / distancia
    
    #Imprimimos los resultados de la iteración actual
    print(f"Iteración {tiempo}: Distancia recorrida = {distancia:.2f} km, Velocidad actual = {velocidad_actual:.2f} km/h, Ritmo actual = {ritmo_actual:.2f} min/km")


#Calculamos velocidad y ritmo medios y los mostramos
ritmo_medio=tiempo/distancia
velocidad_media=distancia/tiempo
print(f"Ritmo medio: {ritmo_medio:.2f} min/km, velocidad media: {velocidad_media:.2f} km/h")