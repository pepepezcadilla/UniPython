import sqlite3
import math

# Verificamos si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Conectamos con la base de datos, consultamos y creamos el registro si no existe
def get_primo_db(position):
    conn = sqlite3.connect("primos.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS primos (posicion INT PRIMARY KEY, value INT)")

    cursor.execute("SELECT value FROM primos WHERE posicion=?", (posicion,))
    resultado = cursor.fetchone()

    if resultado is not None:
        conn.close()
        return resultado[0]
    else:
        contprimo = 0
        num = 2
        while True:
            if es_primo(num):
                contprimo += 1
                if contprimo == posicion:
                    cursor.execute("INSERT INTO primos (posicion, value) VALUES (?, ?)", (posicion, num))
                    conn.commit()
                    conn.close()
                    return num
            num += 1

# Ejecutamos el programa leyendo desde un archivo
try:
    with open("NetWorking/primos.txt", "r") as file:
        posicion = int(file.readline())
        primo = get_primo_db(posicion)
        print(f"El primo en la posición {posicion} es {primo}")
except FileNotFoundError:
    print("El archivo 'primos.txt' no se encontró.")
except ValueError:
    print("El archivo 'primos.txt' debe contener un número válido.")