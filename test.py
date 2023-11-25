# import random
# import math

# # Leer los datos del archivo de texto y almacenarlos en variables
# with open("QAP_sko56_04_n.txt", "r") as file:
#     lines = file.readlines()
#     n = int(lines[0])
#     tamanos = list(map(int, lines[1].split(",")))
#     clientes = [list(map(int, line.split(","))) for line in lines[2:]]

# # Función para calcular la distancia ponderada entre puestos
# def calcular_distancia_ponderada(longitudes, preferencias, puesto1, puesto2):
#     if puesto1 == puesto2:
#         return 0

#     if puesto1 < puesto2:
#         inicio = puesto1
#         fin = puesto2
#     else:
#         inicio = puesto2
#         fin = puesto1

#     distancia_total = 0

#     for i in range(inicio + 1, fin):
#         distancia_total += longitudes[i-1]

#     if puesto1 < puesto2:
#         distancia_total += longitudes[puesto1 - 1] / 2
#         distancia_total += longitudes[puesto2 - 1] / 2

#     distancia_ponderada = distancia_total * preferencias[puesto1 - 1][puesto2 - 1]

#     return distancia_ponderada

# # Función para calcular la suma de las distancias ponderadas
# def calcular_suma_distancias_ponderadas(x_actual, clientes, n):
#     num_puestos = n
#     suma_distancias = 0

#     for puesto1 in range(1, num_puestos + 1):
#         for puesto2 in range(puesto1 + 1, num_puestos + 1):
#             suma_distancias += calcular_distancia_ponderada(x_actual, clientes, puesto1, puesto2)

#     return suma_distancias

# # Función para generar un vecino aleatorio cambiando el orden de dos puestos y sus clientes
# def generar_vecino(x, tamanos, clientes):
#     i, j = random.sample(range(n), 2)
#     vecino_orden = x[:]
#     vecino_tamanos = tamanos[:]
#     vecino_clientes = [row[:] for row in clientes]  # Crear una copia de la lista de preferencias
#     vecino_orden[i], vecino_orden[j] = vecino_orden[j], vecino_orden[i]
#     vecino_tamanos[i], vecino_tamanos[j] = vecino_tamanos[j], vecino_tamanos[i]
#     vecino_clientes[i], vecino_clientes[j] = vecino_clientes[j], vecino_clientes[i]
#     return vecino_orden, vecino_tamanos, vecino_clientes

# # Implementación del algoritmo Simulated Annealing
# def simulated_annealing(tamanos, clientes, n, Tmax, Tmin, enfriamiento, iteraciones):
#     x_actual = list(range(n))  # Orden inicial de los puestos
#     mejor_solucion = x_actual
#     #print("Orden1:",x_actual)
#     #print("tamano1:", tamanos)
#     #print("orden1:", clientes)
#     energia_actual = calcular_suma_distancias_ponderadas(tamanos, clientes, n)
#     mejor_energia = energia_actual

#     for i in range(iteraciones):
#         T = Tmax - i * ((Tmax - Tmin) / iteraciones)
        
#         vecino_orden, vecino_tamanos, vecino_clientes = generar_vecino(x_actual, tamanos,clientes)
#         #print("Orden2: ",vecino_orden)
#         #print("tamano2: ", vecino_tamanos)
#         #print("orden2: ", vecino_clientes)
#         energia_vecino = calcular_suma_distancias_ponderadas(vecino_tamanos,vecino_clientes, n)

#         if energia_vecino < energia_actual or random.random() < math.exp((energia_actual - energia_vecino) / T):
#             x_actual = vecino_orden
#             tamanos = vecino_tamanos
#             clientes = vecino_clientes
#             energia_actual = energia_vecino

#         if energia_actual < mejor_energia:
#             mejor_solucion = x_actual
#             mejor_energia = energia_actual

#     return mejor_solucion, mejor_energia

# # Parámetros del algoritmo
# Tmax = 1000
# Tmin = 1
# enfriamiento = 0.95
# iteraciones = 1000

# # Ejecutar Simulated Annealing
# mejor_orden, mejor_energia = simulated_annealing(tamanos, clientes, n, Tmax, Tmin, enfriamiento, iteraciones)

# print("Mejor orden de puestos:", [x + 1 for x in mejor_orden])
# print("Energía (distancia total ponderada) de la mejor solución:", mejor_energia)


import random
import math

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
def simulated_annealing(tamanos, clientes, n, Tmax, Tmin, enfriamiento, iteraciones):
    x_actual = list(range(n))  # Orden inicial de los puestos
    mejor_solucion = x_actual
    energia_actual = calcular_suma_distancias_ponderadas(tamanos, clientes, n)
    mejor_energia = energia_actual

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
            if T > 0 and random.random() < math.exp((energia_actual - energia_vecino) / T):
                x_actual = vecino_orden
                tamanos = vecino_tamanos
                clientes = vecino_clientes
                energia_actual = energia_vecino
                mejor_solucion = x_actual
                mejor_energia = energia_actual

        # Aplicando enfriamiento
        Tmax *= enfriamiento

    # Impresión de la mejor solución con indices i (partiendo de i = 0)
    print("Mejor solución:", x_actual)
    print("Energía:", energia_actual)

    return mejor_solucion, mejor_energia

# Parámetros del algoritmo
Tmax = 1000
Tmin = 1
enfriamiento = 0.02
iteraciones = 1000

# Ejecutar Simulated Annealing
mejor_orden, mejor_energia = simulated_annealing(tamanos, clientes, n, Tmax, Tmin, enfriamiento, iteraciones)
# Impresión de la mejor solución con indices i + 1
print("Mejor orden de puestos:", [i + 1 for i in mejor_orden])
print("Energía (distancia total ponderada) de la mejor solución:", mejor_energia)