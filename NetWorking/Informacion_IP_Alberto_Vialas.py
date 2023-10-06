def calcular_info_red(ip_str, mascara_str):
    try:
        # Parsear la dirección IP y la máscara de subred
        ip_parts = [int(x) for x in ip_str.split(".")]
        mascara_parts = [int(x) for x in mascara_str.split(".")]

        # Validar que los valores estén en el rango correcto
        if (len(ip_parts) != 4 or
            any(x < 0 or x > 255 for x in ip_parts) or
            any(x < 0 or x > 255 for x in mascara_parts)):
            return "Dirección IP o máscara de subred inválida."

        # Calcular la dirección de red y la dirección de broadcast
        direccion_de_red = [ip & mascara for ip, mascara in zip(ip_parts, mascara_parts)]
        direccion_de_broadcast = [(ip | ~mascara) & 255 for ip, mascara in zip(ip_parts, mascara_parts)]

        # Clasificar la red en función del primer octeto de la dirección IP
        primer_octeto = ip_parts[0]
        if 1 <= primer_octeto <= 126:
            clase = "A"
        elif 128 <= primer_octeto <= 191:
            clase = "B"
        elif 192 <= primer_octeto <= 223:
            clase = "C"
        else:
            clase = "No definida"

        # Calcular la cantidad de bits para red y bits para host
        bits_para_red = sum([bin(mascara).count('1') for mascara in mascara_parts])
        bits_para_host = 32 - bits_para_red

        # Calcular el nombre de red
        nombre_de_red = ".".join(map(str, direccion_de_red))

        # Calcular la dirección del primer host y del último host
        primer_host = direccion_de_red.copy()
        primer_host[-1] += 1
        ultimo_host = direccion_de_broadcast.copy()
        ultimo_host[-1] -= 1

        # Calcular el número máximo de hosts
        numero_maximo_de_hosts = 2 ** bits_para_host - 2

        return {
            "Clase de red": clase,
            "Bits para red": bits_para_red,
            "Bits para host": bits_para_host,
            "Nombre de red": nombre_de_red,
            "IP del primer host": ".".join(map(str, primer_host)),
            "IP del último host": ".".join(map(str, ultimo_host)),
            "Número máximo de hosts": numero_maximo_de_hosts
        }

    except ValueError:
        return "Dirección IP o máscara de subred inválida."

if __name__ == "__main__":
    ip = input("Ingrese la dirección IP: ")
    mascara = input("Ingrese la máscara de subred: ")
    info_red = calcular_info_red(ip, mascara)
    for key, value in info_red.items():
        print(f"{key}: {value}")
