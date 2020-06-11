from codigo.funcionesAuxiliares import *

iteraciones_prueba = 50
estadisticas = []
for i in range(iteraciones_prueba):
    print(i)
    # 0. Leer datos
    datos_entrada = leer_datos('../data/entrada-profesor2.csv')

    num_cluster = 3
    circunferencias = []

    criterio_parada = 1  # 0 -> numero_iteraciones, 1 -> similitud_cluster
    numero_iteraciones = 1000
    similitud_cluster = True

    # 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
    inicializar_datos(datos_entrada, num_cluster, circunferencias)

    # 2. Repetir (hasta condición de parada)
    if criterio_parada == 0:
        iteraciones = criterio_iteraciones(numero_iteraciones, datos_entrada, circunferencias)
    else:
        iteraciones = criterio_similitud(similitud_cluster, circunferencias, datos_entrada)

    # 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
    asignar_puntos(circunferencias, datos_entrada, estadisticas)

    # 4. Mostrar salidas y gráfica
    #mostrar_resultados(datos_entrada, circunferencias, iteraciones)

print(estadisticas)