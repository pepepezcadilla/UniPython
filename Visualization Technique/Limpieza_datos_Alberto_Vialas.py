import re
import matplotlib.pyplot as plt

# Paso 1: Limpieza de los datos
with open('datos_borrador.pgn', 'r') as file:
    data = file.read()

# Utilizamos expresiones regulares para eliminar las cabeceras de las partidas
cleaned_data = re.sub(r'\[[^\]]+\]\n', '', data)

# Paso 2: Visualización de datos
# Obtener el número de partidas por cada apertura
opening_counts = {}
opening_responses = {}
games = cleaned_data.strip().split('\n\n')  # Separar las partidas
for game in games:
    moves = game.strip().split()[1:]  # Ignorar el número de partida y capturar los movimientos
    if len(moves) < 1:
        continue  # Saltar partidas sin movimientos registrados
    opening = moves[0]
    opening_counts[opening] = opening_counts.get(opening, 0) + 1

    if opening not in opening_responses:
        opening_responses[opening] = {}

    if len(moves) > 1:
        response = moves[1]
        opening_responses[opening][response] = opening_responses[opening].get(response, 0) + 1

# Ordenar las aperturas por número de partidas
sorted_openings = sorted(opening_counts.items(), key=lambda x: x[1], reverse=True)

# Excluir la etiqueta 'No Data'
sorted_openings = [(opening, count) for opening, count in sorted_openings if opening != 'No Data']

# Gráfico de barras para el número de partidas por apertura
openings, counts = zip(*sorted_openings)
plt.figure(figsize=(12, 6))
plt.bar(openings, counts)
plt.xticks(rotation=90)
plt.xlabel('Apertura')
plt.ylabel('Número de Partidas')
plt.title('Número de Partidas por Apertura')
plt.tight_layout()
plt.show()

# Gráfico de barras para las respuestas más comunes para las cuatro aperturas más utilizadas
top_openings = [opening for opening, _ in sorted_openings[:4]]
plt.figure(figsize=(12, 8))
for i, opening in enumerate(top_openings):
    responses = opening_responses[opening]
    sorted_responses = sorted(responses.items(), key=lambda x: x[1], reverse=True)
    top_responses = dict(sorted_responses[:5])  # Mostrar las 5 respuestas más comunes por apertura
    plt.subplot(2, 2, i + 1)
    plt.bar(top_responses.keys(), top_responses.values())
    plt.xticks(rotation=90)
    plt.xlabel('Respuesta')
    plt.ylabel('Número de Respuestas')
    plt.title(f'Respuestas para {opening}')
plt.tight_layout()
plt.show()
