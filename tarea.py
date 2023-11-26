import random
import math
import time

# Leer los datos del archivo de texto y almacenarlos en variables
with open("QAP_sko56_04_n.txt", "r") as file:
    lines = file.readlines()
    n = int(lines[0])
    tamanos = list(map(int, lines[1].split(",")))
    clientes = [list(map(int, line.split(","))) for line in lines[2:]]

# Función para calcular la distancia ponderada entre puestos
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
        distancia_total += longitudes[i-1]

    if puesto1 < puesto2:
        distancia_total += longitudes[puesto1 - 1] / 2
        distancia_total += longitudes[puesto2 - 1] / 2

    distancia_ponderada = distancia_total * preferencias[puesto1 - 1][puesto2 - 1]

    return distancia_ponderada

# Función para calcular la suma de las distancias ponderadas
def calcular_suma_distancias_ponderadas(x_actual, clientes, n):
    num_puestos = n
    suma_distancias = 0

    for puesto1 in range(1, num_puestos + 1):
        for puesto2 in range(puesto1 + 1, num_puestos + 1):
            suma_distancias += calcular_distancia_ponderada(x_actual, clientes, puesto1, puesto2)

    return suma_distancias

# Función para generar un vecino cambiando el orden de dos puestos y sus clientes
def generar_vecino(x, tamanos, clientes):
    i, j = random.sample(range(n), 2)
    vecino_orden = x[:]
    vecino_tamanos = tamanos[:]
    vecino_clientes = [row[:] for row in clientes]  # Crear una copia de la lista de preferencias
    vecino_orden[i], vecino_orden[j] = vecino_orden[j], vecino_orden[i]
    vecino_tamanos[i], vecino_tamanos[j] = vecino_tamanos[j], vecino_tamanos[i]
    vecino_clientes[i], vecino_clientes[j] = vecino_clientes[j], vecino_clientes[i]
    return vecino_orden, vecino_tamanos, vecino_clientes

# Implementación del algoritmo Simulated Annealing
def simulated_annealing(tamanos, clientes, n, Tmax, Tmin, enfriamiento):
    start_time = time.time()  # Registra el tiempo de inicio
    x_actual = list(range(n))  # Orden inicial de los puestos. # Orden de lectura.
    random.shuffle(x_actual) # Solución inicial: ahora es aleatoria.
    mejor_solucion = x_actual
    energia_actual = calcular_suma_distancias_ponderadas(tamanos, clientes, n)
    mejor_energia = energia_actual
    iteraciones = 5000

    # Impresión de la solución inicial y su evaluación en la función objetivo con indices i (partiendo de i = 0)
    print("Solución inicial (x):", [i for i in x_actual])
    print("Energía inicial (f(x)):", energia_actual, '\n')
    
    for i in range(iteraciones):
        
        # Temperatura de inicio
        T = Tmax

        # Generación de una nueva solución vecina
        vecino_orden, vecino_tamanos, vecino_clientes = generar_vecino(x_actual, tamanos, clientes)
        energia_vecino = calcular_suma_distancias_ponderadas(vecino_tamanos, vecino_clientes, n)

        # Actualización de la solución
        if energia_vecino < energia_actual:
            x_actual = vecino_orden
            tamanos = vecino_tamanos
            clientes = vecino_clientes
            energia_actual = energia_vecino
            mejor_solucion = x_actual
            mejor_energia = energia_actual
        else:
            if T >= Tmin and random.random() < math.exp((energia_actual - energia_vecino) / T):
                x_actual = vecino_orden
                tamanos = vecino_tamanos
                clientes = vecino_clientes
                energia_actual = energia_vecino
                mejor_solucion = x_actual
                mejor_energia = energia_actual

        # Aplicando enfriamiento
        Tmax *= enfriamiento

    end_time = time.time()  # Registra el tiempo de finalización
    elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido

    # Impresión del tiempo medio de ejecución en milisegundos, aproximado a cuatro decimales
    tiempo_medio_ms = round((elapsed_time) * 1000, 4)

    return mejor_solucion, mejor_energia, tiempo_medio_ms

# Parámetros del algoritmo
Tmax = 1000
Tmin = 1
enfriamiento = 0.5
for i in range(10):
    print("----- EJECUCIÓN", i, ": -----")
    # Ejecutar Simulated Annealing
    mejor_orden, mejor_energia, tiempo_medio = simulated_annealing(tamanos, clientes, n, Tmax, Tmin, enfriamiento)

    # Métricas para análisis del código, comentado para entrega final
    # Impresión de la mejor solución con indices i + 1
    print("Mejor solución (x'):", [i for i in mejor_orden])
    print("Energía final (f(x')):", mejor_energia)
    print("Tiempo de ejecución (ms.):", tiempo_medio)
    print("Tiempo de ejecución (seg.):", round(tiempo_medio / 1000,4), '\n')