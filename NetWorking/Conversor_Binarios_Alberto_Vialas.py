def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        bit = int(binario[i])
        exponente = longitud - 1 - i
        decimal += bit * (2 ** exponente)
    return decimal

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

while True:
    print("Seleccione una opción:")
    print("1. Binario a Decimal")
    print("2. Decimal a Binario")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        binario = input("Ingrese el número binario: ")
        decimal = binario_a_decimal(binario)
        print("El número decimal es:", decimal)
    elif opcion == "2":
        decimal = int(input("Ingrese el número decimal: "))
        binario = decimal_a_binario(decimal)
        print("El número binario es:", binario)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
