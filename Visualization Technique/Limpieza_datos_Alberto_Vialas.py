import re
import matplotlib.pyplot as plot

# Leemos los datos
with open('datos_borrador.pgn', 'r') as archivo:
    datos = archivo.read()

# Utilizamos expresiones regulares para eliminar las cabeceras de las partidas
datos_limpios = re.sub(r'\[[^\]]+\]\n', '', datos)

# Obtenemos el número de partidas por cada apertura
conteo_aperturas = {}
respuestas_aperturas = {}
partidas = datos_limpios.strip().split('\n\n')  # Separamos las partidas
for partida in partidas:
    movimientos = partida.strip().split()[1:]  # Ignoramos el número de partida y capturamos los movimientos
    if len(movimientos) < 1:
        continue  # Saltamos partidas sin movimientos registrados
    apertura = movimientos[0]
    conteo_aperturas[apertura] = conteo_aperturas.get(apertura, 0) + 1

    if apertura not in respuestas_aperturas:
        respuestas_aperturas[apertura] = {}

    if len(movimientos) > 1:
        respuesta = movimientos[1]
        respuestas_aperturas[apertura][respuesta] = respuestas_aperturas[apertura].get(respuesta, 0) + 1

# Ordenamos las aperturas por número de partidas
aperturas_ordenadas = sorted(conteo_aperturas.items(), key=lambda x: x[1], reverse=True)

# Gráfico de barras para el número de partidas por apertura
aperturas, conteos = zip(*aperturas_ordenadas)
plot.figure(figsize=(12, 6))
plot.bar(aperturas, conteos)
plot.xticks(rotation=90)
plot.xlabel('Apertura')
plot.ylabel('Número de Partidas')
plot.title('Número de Partidas por Apertura')
plot.tight_layout()
plot.show()

# Gráfico de barras para las respuestas más comunes para las cuatro aperturas más utilizadas
top_aperturas = [apertura for apertura, _ in aperturas_ordenadas[:4]]
plot.figure(figsize=(12, 8))
for i, apertura in enumerate(top_aperturas):
    respuestas = respuestas_aperturas[apertura]
    respuestas_ordenadas = sorted(respuestas.items(), key=lambda x: x[1], reverse=True)
    top_respuestas = dict(respuestas_ordenadas[:5])  # Mostrar las 5 respuestas más comunes por apertura
    plot.subplot(2, 2, i + 1)
    plot.bar(top_respuestas.keys(), top_respuestas.values())
    plot.xticks(rotation=90)
    plot.xlabel('Respuesta')
    plot.ylabel('Número de Respuestas')
    plot.title(f'Respuestas para {apertura}')
plot.tight_layout()
plot.show()
