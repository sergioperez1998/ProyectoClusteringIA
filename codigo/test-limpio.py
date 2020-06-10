from codigo.funcionesAuxiliares import *

# 0. Leer datos
datos_entrada = leer_datos('../data/entrada-profesor2.csv')

num_cluster = 3
circunferencias = []
iteraciones = 0

criterio_parada = 1  # 0 -> numero_iteraciones, 1 -> similitud_cluster
numero_iteraciones = 10
similitud_cluster = True

# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
inicializar_datos(datos_entrada, num_cluster, circunferencias)

# 2. Repetir (hasta condición de parada)
if criterio_parada == 0:
    criterio_iteraciones(numero_iteraciones, datos_entrada, circunferencias, iteraciones)
else:
    criterio_similitud(similitud_cluster, iteraciones, circunferencias, datos_entrada)

# 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
asignar_puntos(circunferencias, datos_entrada)

# 4. Mostrar salidas y gráfica
mostrar_resultados(datos_entrada, circunferencias, iteraciones)
