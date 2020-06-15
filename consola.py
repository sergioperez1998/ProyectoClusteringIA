from codigo.funcionesAuxiliares import *
import time
import sys
import argparse

# ...
parser = argparse.ArgumentParser(
    prog="Proyecto Clustering IA 2020",
    description="Interfaz de consola del Proyecto de Clustering IA 2020.",
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument(
    "-np",
    "-numeroPruebas",
    required=True,
    type=int,
    help="Número de pruebas a realizar."
)
parser.add_argument(
    "-de",
    "-datosEntrada",
    required=True,
    help="Ruta completa del csv de entrada."
)
parser.add_argument(
    "-i",
    "-inicializacion",
    choices=[0, 1],
    required=True,
    type=int,
    help="""Modo de inicialización.
         Si elige 0 tendrá que introducir a mano el centro y radio de las circunferencias.
         Si elige el modo 1 se generarán automáticamente."""
)
parser.add_argument(
    "-nc",
    "-numeroCluster",
    required=True,
    type=int,
    help="Número de cluster iniciales."
)
parser.add_argument(
    "-cp",
    "-criterioParada",
    choices=[0, 1],
    required=True,
    type=int,
    help="""Criterio de parada.
         Si elige 0 tendrá que añadir el parámero -ni con el número de iteraciones a parar.
         Si elige el modo 1 se utilizará el criterio de similitud de clúster."""
)
parser.add_argument(
    "-ni",
    "-numeroIteraciones",
    type=int,
    help="""Número de iteraciones si se elige el criterio de parada por iteraciones"""
)

args = parser.parse_args()

iteraciones_prueba = args.np
estadisticas = []

for i in range(iteraciones_prueba):
    # 0. Leer datos
    datos_entrada = leer_datos(args.de)

    tipo_input = args.i

    num_cluster = args.nc

    criterio_parada = args.cp  # 0 -> numero_iteraciones, 1 -> similitud_cluster

    if criterio_parada == 0:
        numero_iteraciones = args.ni
    similitud_cluster = True

    # 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
    circunferencias = []
    if tipo_input == 0:
        for j in range(num_cluster):
            centro_x = float(input("Introduzca la coordenada x del centro de la circunferencia: "))
            centro_y = float(input("Introduzca la coordenada y del centro de la circunferencia: "))
            radio = float(input("Introduzca el radio de la circunferencia: "))
            circunferencias.append(Circunferencia(Punto(centro_x, centro_y), radio))
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

valor = []
for i in range(len(estadisticas)):
    valor.append(estadisticas[i][0])
minimo = min(valor)
maximo = max(valor)
media = sum(e for e in valor) / len(valor)
index = valor.index(minimo)

print("Número de iteraciones: ", + iteraciones_prueba)
print("Tiempo de ejecución: %s segundos" % (time.time() - tiempo))
print("Mínimo de puntos sin asignar: " + str(minimo))
print("Máximo de puntos sin asignar: " + str(maximo))
print("Media de puntos sin asignar: " + str(media))

mostrar_resultados(datos_entrada, estadisticas[index][1], iteraciones)
