import sqlite3
import random

def crear_base_de_datos():
    # Crear y conectar a la base de datos
    conn = sqlite3.connect('acronimos.db')
    cursor = conn.cursor()

    # Crear una tabla para almacenar los acrónimos y definiciones
    cursor.execute('''CREATE TABLE IF NOT EXISTS acronimos (
                        id INTEGER PRIMARY KEY,
                        acronimo TEXT NOT NULL UNIQUE,
                        definicion TEXT NOT NULL
                    )''')

    # Insertar datos en la base de datos (verificando si el acrónimo ya existe)
    acronimos_definiciones = [
    ('LAN', 'Local Area Network'),
    ('WAN', 'Wide Area Network'),
    ('TCP', 'Transmission Control Protocol'),
    ('IP', 'Internet Protocol'),
    ('HTTP', 'Hypertext Transfer Protocol'),
    ('DNS', 'Domain Name System'),
    ('FTP', 'File Transfer Protocol'),
    ('VPN', 'Virtual Private Network'),
    ('SSID', 'Service Set Identifier'),
    ('SMTP', 'Simple Mail Transfer Protocol'),
    ('MAC', 'Media Access Control'),
    ('HTTPS', 'Hypertext Transfer Protocol Secure'),
    ('DHCP', 'Dynamic Host Configuration Protocol'),
    ('LAN', 'Local Area Network'),
    ('ISP', 'Internet Service Provider')
]

    for acronimo, definicion in acronimos_definiciones:
        try:
            cursor.execute("INSERT INTO acronimos (acronimo, definicion) VALUES (?, ?)", (acronimo, definicion))
        except sqlite3.IntegrityError:
            print(f"Acrónimo '{acronimo}' ya existe en la base de datos. Se omite la inserción.")

    conn.commit()

def buscar_definicion(acronimo):
    cursor.execute("SELECT definicion FROM acronimos WHERE acronimo=?", (acronimo,))
    definicion = cursor.fetchone()
    return definicion[0] if definicion else "Acrónimo no encontrado."

def jugar():
    while True:
        cursor.execute("SELECT acronimo, definicion FROM acronimos ORDER BY RANDOM() LIMIT 1")
        acronimo, definicion = cursor.fetchone()
        print(f"Definición: {definicion}")
        respuesta = input("Adivina el acrónimo: ").strip().upper()
        if respuesta == acronimo:
            print("¡Correcto!")
            continuar = input("¿Deseas seguir jugando? (S/N): ").strip().lower()
            if continuar != 's':
                break
        else:
            print("Respuesta incorrecta. Inténtalo de nuevo.")

def main():
    crear_base_de_datos()

    # Conectar a la base de datos
    conn = sqlite3.connect('acronimos.db')
    global cursor
    cursor = conn.cursor()

    while True:
        print("\nMenú:")
        print("1. Diccionario")
        print("2. Juego")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            acronimo = input("Introduce un acrónimo: ").strip().upper()
            definicion = buscar_definicion(acronimo)
            print(f"Definición: {definicion}")
        elif opcion == '2':
            jugar()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

    # Cerrar la conexión a la base de datos
    conn.close()

if __name__ == "__main__":
    main()
