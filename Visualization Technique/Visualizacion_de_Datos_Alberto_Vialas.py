import matplotlib.pyplot as plot

# Leemos el archivo
with open('partidas.csv', 'r') as archivo:
    datos = archivo.readlines()

movimientos = []
aperturas = []

# Separamos las lineas del archivo y lo almacenamos en los array que acabamos de crear
for line in datos:
    movimiento, apertura = line.strip().split(': ')
    movimientos.append(movimiento)
    aperturas.append(int(apertura.replace('.', '')))

# Configuramos el gráfico, le ponemos los títulos y le asignamos los valores
figura, ejes = plot.subplots()
ejes.bar(movimientos, aperturas)
ejes.set_xlabel('Movimientos de Apertura')
ejes.set_ylabel('Número de Aperturas')
ejes.set_title('Número de Aperturas por Movimiento de Apertura')
ejes.set_xticklabels(movimientos, rotation=45)

# Configuramos el eje y para que muestre los valores que queremos
start, end = ejes.get_ylim()
ejes.yaxis.set_ticks(range(int(start), int(end)+1, 500000))

# Mostramos el gráfico
plot.show()