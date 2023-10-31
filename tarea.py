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

def obtener_nombre_columna(columna, columnas_intercambiadas):
    return chr(65 + columnas_intercambiadas.index(columna))  # Convierte el número de columna a letra según el orden actual

def intercambiar_columnas(preferencias, columnas_intercambiadas, columna1, columna2):
    for i in range(len(preferencias)):
        preferencias[i][columna1], preferencias[i][columna2] = preferencias[i][columna2], preferencias[i][columna1]
    columnas_intercambiadas[columna1], columnas_intercambiadas[columna2] = columnas_intercambiadas[columna2], columnas_intercambiadas[columna1]

nombre_archivo = 'S5'

datos = leer_archivo(nombre_archivo)
if datos:
    num_puestos, longitudes, preferencias = datos

    columnas_intercambiadas = [chr(65 + i) for i in range(num_puestos)]

    nombre_columna = ''.join(columnas_intercambiadas)
    suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
    print(f"x = {nombre_columna}, f(x) = {suma_distancias}")

    intercambio = input("Introduce las letras de las columnas a intercambiar (por ejemplo, A,B): ")
    columnas_a_intercambiar = intercambio.split(',')
    if len(columnas_a_intercambiar) == 2:
        columna1 = columnas_intercambiadas.index(columnas_a_intercambiar[0])
        columna2 = columnas_intercambiadas.index(columnas_a_intercambiar[1])
        if 0 <= columna1 < num_puestos and 0 <= columna2 < num_puestos:
            intercambiar_columnas(preferencias, columnas_intercambiadas, columna1, columna2)
            nueva_suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
            nueva_nombre_columna = ''.join(columnas_intercambiadas)
            print(f"x = {nueva_nombre_columna}, f(x) = {nueva_suma_distancias}")
