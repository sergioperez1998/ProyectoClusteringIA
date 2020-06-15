from codigo.funcionesAuxiliares import *
import time

iteraciones_prueba = 100
estadisticas = []

tiempo = time.time()
for i in range(iteraciones_prueba):
    print(i)
    # 0. Leer datos
    datos_entrada = leer_datos('../data/entrada-profesor.csv')

    num_cluster = 2
    circunferencias = []

    criterio_parada = 0  # 0 -> numero_iteraciones, 1 -> similitud_cluster
    numero_iteraciones = 100
    similitud_cluster = True

    # 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
    inicializar_datos(datos_entrada, num_cluster, circunferencias)

    # 2. Repetir (hasta condición de parada)
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
