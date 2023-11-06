import random
import math

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
    # return chr(65 + columnas_intercambiadas.index(columna)) 
    return str(columnas_intercambiadas.index(columna) + 1)

def intercambiar_columnas(preferencias, columnas_intercambiadas, columna1, columna2):
    for i in range(len(preferencias)):
        preferencias[i][columna1], preferencias[i][columna2] = preferencias[i][columna2], preferencias[i][columna1]
    columnas_intercambiadas[columna1], columnas_intercambiadas[columna2] = columnas_intercambiadas[columna2], columnas_intercambiadas[columna1]

nombre_archivo = 'QAP_sko56_04_n.txt'

datos = leer_archivo(nombre_archivo)
if datos:
    num_puestos, longitudes, preferencias = datos

    columnas_intercambiadas = list(range(1, num_puestos + 1))  # Utiliza números en lugar de letras

    nombre_columna = ' '.join([str(i) for i in columnas_intercambiadas])  # Utiliza números en lugar de letras
    suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
    print(f"x = {nombre_columna}, f(x) = {suma_distancias}")

    intercambio = input("Introduce los números de las columnas a intercambiar (por ejemplo, 1,2): ")
    columnas_a_intercambiar = list(map(int, intercambio.split(',')))
    if len(columnas_a_intercambiar) == 2:
        columna1 = columnas_a_intercambiar[0]
        columna2 = columnas_a_intercambiar[1]
        if 1 <= columna1 <= num_puestos and 1 <= columna2 <= num_puestos:
            intercambiar_columnas(preferencias, columnas_intercambiadas, columna1 - 1, columna2 - 1)  # Resta 1 para ajustar al índice
            nueva_suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
            nueva_nombre_columna = ' '.join([str(i) for i in columnas_intercambiadas])  # Utiliza números en lugar de letras
            print(f"x = {nueva_nombre_columna}, f(x) = {nueva_suma_distancias}")

def simulated_annealing_metropolis(longitudes, preferencias, Tmax, Tmin, enfriamiento, iteraciones):
    num_puestos = len(longitudes)
    mejor_orden = list(range(1, num_puestos + 1))  # Cambiado para iniciar desde 1 en lugar de 0
    mejor_suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
    mejor_nombre_columna = ''.join([str(i) for i in range(1, num_puestos + 1)])  # Utiliza números en lugar de letras

    orden_actual = list(range(1, num_puestos + 1))  # Cambiado para iniciar desde 1 en lugar de 0
    suma_distancias_actual = mejor_suma_distancias
    nombre_columna_actual = mejor_nombre_columna

    for i in range(iteraciones):
        T = Tmax - i * ((Tmax - Tmin) / iteraciones)

        columna1, columna2 = random.sample(range(1, num_puestos + 1), 2)  # Utiliza números en lugar de letras
        intercambiar_columnas(preferencias, orden_actual, columna1 - 1, columna2 - 1)  # Resta 1 para ajustar al índice
        nueva_suma_distancias = calcular_suma_distancias_ponderadas(longitudes, preferencias)
        nueva_nombre_columna = ' '.join([str(i) for i in orden_actual])  # Utiliza números en lugar de letras

        # Calcular la probabilidad de aceptación usando el criterio de Metrópolis con log-sum-exp trick
        exponente = min(0, (suma_distancias_actual - nueva_suma_distancias) / T)
        probabilidad_aceptacion = 1 / (1 + math.exp(exponente))

        # Aceptar la nueva solución con Metrópolis criteria
        if nueva_suma_distancias < suma_distancias_actual or random.random() < probabilidad_aceptacion:
            suma_distancias_actual = nueva_suma_distancias
            nombre_columna_actual = nueva_nombre_columna

            # Actualizar la mejor solución si es necesario
            if suma_distancias_actual < mejor_suma_distancias:
                mejor_suma_distancias = suma_distancias_actual
                mejor_orden = orden_actual[:]
                mejor_nombre_columna = nombre_columna_actual

        # Reducir la temperatura
        # Tmax *= enfriamiento

    return mejor_orden, mejor_nombre_columna, mejor_suma_distancias

# Parámetros del algoritmo
Tmax = 1000
Tmin = 1
enfriamiento = 0.95
iteraciones = 1000

# Ejecutar Simulated Annealing con el criterio de Metrópolis
mejor_orden, mejor_nombre_columna, mejor_suma_distancias = simulated_annealing_metropolis(longitudes, preferencias, Tmax, Tmin, enfriamiento, iteraciones)

print(f"Mejor orden de puestos: [{mejor_nombre_columna}]")
print(f"Suma de distancias ponderadas de la mejor solución: {mejor_suma_distancias}")