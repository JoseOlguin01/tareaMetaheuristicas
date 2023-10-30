def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Leer el número de puestos
            num_puestos = int(archivo.readline())

            # Leer las longitudes de los puestos
            longitudes = list(map(int, archivo.readline().split(',')))

            # Crear una matriz para almacenar las preferencias de compra
            preferencias = []
            for _ in range(num_puestos):
                linea = list(map(int, archivo.readline().split(',')))
                preferencias.append(linea)

            return num_puestos, longitudes, preferencias

    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", str(e))

    return None

def calcular_distancia_ponderada(longitudes, preferencias, puesto1, puesto2):
    if puesto1 == puesto2:
        return 0

    if puesto1 < puesto2:
        inicio = puesto1
        fin = puesto2
    else:
        inicio = puesto2
        fin = puesto1

    distancia_total = 0

    for i in range(inicio + 1, fin):
        distancia_total += longitudes[i - 1]

    if puesto1 < puesto2:
        distancia_total += longitudes[puesto1 - 1] / 2
        distancia_total += longitudes[puesto2 - 1] / 2

    distancia_ponderada = distancia_total * preferencias[puesto1 - 1][puesto2 - 1]

    return distancia_ponderada

def calcular_suma_distancias_ponderadas(longitudes, preferencias):
    num_puestos = len(longitudes)
    suma_distancias = 0

    for puesto1 in range(1, num_puestos + 1):
        for puesto2 in range(puesto1 + 1, num_puestos + 1):
            suma_distancias += calcular_distancia_ponderada(longitudes, preferencias, puesto1, puesto2)

    return suma_distancias

nombre_archivo = 'S3'  # Reemplaza con el nombre de tu archivo

datos = leer_archivo(nombre_archivo)
if datos:
    num_puestos, longitudes, preferencias = datos

    puesto1 = 2
    puesto2 = 5

    # distancia_ponderada = calcular_distancia_ponderada(longitudes, preferencias, puesto1, puesto2)
    # print(f"La distancia ponderada entre el puesto {puesto1} y el puesto {puesto2} es {distancia_ponderada}")

    suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
    print(f"La suma de las distancias ponderadas para todos los pares de puestos es {suma_distancias}")