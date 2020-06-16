from codigo.funcionesAuxiliares import *
import time
import copy

def clustering(iteraciones_prueba, datos_entrada, tipo_input, num_cluster, criterio_parada, numero_iteraciones,
               circunferencias_entrada):
    estadisticas = []
    tiempo = time.time()
    for i in range(iteraciones_prueba):
        # 0. Leer datos
        print(i)
        datos = leer_datos(datos_entrada)

        similitud_cluster = True

        # 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
        circunferencias = []
        if tipo_input == 1:
            inicializar_datos(datos, num_cluster, circunferencias)
        else:
            circunferencias = copy.deepcopy(circunferencias_entrada)

        # 2. Repetir (hasta condición de parada)
        if criterio_parada == 0:
            iteraciones = criterio_iteraciones(numero_iteraciones, datos, circunferencias)
        else:
            iteraciones = criterio_similitud(similitud_cluster, circunferencias, datos)

        # 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
        asignar_puntos(circunferencias, datos, estadisticas)

    datos_salida = mostrar_resultados(datos, estadisticas, iteraciones, iteraciones_prueba, tiempo)
    return datos_salida
