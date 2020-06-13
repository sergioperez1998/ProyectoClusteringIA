from codigo.funcionesAuxiliares import *
import time
import sys

iteraciones_prueba = int(sys.argv[1])
estadisticas = []

for i in range(iteraciones_prueba):
    # 0. Leer datos
    datos_entrada = leer_datos(sys.argv[2])

    tipo_input = int(sys.argv[3])

    num_cluster = int(sys.argv[4])

    criterio_parada = int(sys.argv[5])  # 0 -> numero_iteraciones, 1 -> similitud_cluster

    if criterio_parada == 0:
        numero_iteraciones = int(sys.argv[6])
    similitud_cluster = True

    # 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
    circunferencias = []
    if tipo_input == 0:
        for n in range(num_cluster):
            centro_x = input("Introduzca la coordenada x del centro de la circunferencia: ")
            centro_y = input("Introduzca la coordenada y del centro de la circunferencia: ")
            radio = input("Introduzca el radio de la circunferencia: ")
            circunferencias.append(Circunferencia(Punto(float(centro_x), float(centro_y)), float(radio)))
    else:
        inicializar_datos(datos_entrada, num_cluster, circunferencias)
    # 2. Repetir (hasta condición de parada)
    tiempo = time.time()
    if criterio_parada == 0:
        iteraciones = criterio_iteraciones(numero_iteraciones, datos_entrada, circunferencias)
    else:
        iteraciones = criterio_similitud(similitud_cluster, circunferencias, datos_entrada)

    # 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
    asignar_puntos(circunferencias, datos_entrada,estadisticas)

    # 4. Mostrar salidas y gráfica
    # mostrar_resultados(datos_entrada, circunferencias, iteraciones)

print("--- %s seconds ---" % (time.time() - tiempo))

valor = []
for i in range(len(estadisticas)):
    valor.append(estadisticas[i][0])
minimo = min(valor)
maximo = max(valor)
media = sum(e for e in valor) / len(valor)
index = valor.index(minimo)

print("Número de iteraciones: ", + iteraciones_prueba)
print("Mínimo de puntos sin asignar: " + str(minimo))
print("Máximo de puntos sin asignar: " + str(maximo))
print("Media de puntos sin asignar: " + str(media))

mostrar_resultados(datos_entrada, estadisticas[index][1], iteraciones)
