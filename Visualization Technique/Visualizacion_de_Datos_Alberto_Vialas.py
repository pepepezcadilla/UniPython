import matplotlib.pyplot as plt

with open('partidas.csv', 'r') as file:
    data = file.readlines()

movimientos = []
aperturas = []

for line in data:
    movimiento, apertura = line.strip().split(': ')
    movimientos.append(movimiento)
    aperturas.append(int(apertura.replace('.', '')))

fig, ax = plt.subplots()
ax.bar(movimientos, aperturas)
ax.set_xlabel('Movimientos de Apertura')
ax.set_ylabel('Número de Aperturas')
ax.set_title('Número de Aperturas por Movimiento de Apertura')
ax.set_xticklabels(movimientos, rotation=45)

start, end = ax.get_ylim()
ax.yaxis.set_ticks(range(int(start), int(end)+1, 500000))

plt.show()