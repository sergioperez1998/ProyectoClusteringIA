from codigo.clustering import *
import argparse

# Configuración de la consola
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
datos_entrada = args.de
tipo_input = args.i  # 0 -> manual, 1 -> automático
num_cluster = args.nc
criterio_parada = args.cp  # 0 -> numero_iteraciones, 1 -> similitud_cluster
numero_iteraciones = args.ni

circunferencias_entrada = []
if tipo_input == 0:
    for i in range(num_cluster):
        centro_x = float(input("Introduzca la coordenada x del centro de la circunferencia: "))
        centro_y = float(input("Introduzca la coordenada y del centro de la circunferencia: "))
        radio = float(input("Introduzca el radio de la circunferencia: "))
        circunferencias_entrada.append(Circunferencia(Punto(centro_x, centro_y), radio))

clustering(iteraciones_prueba, datos_entrada, tipo_input, num_cluster, criterio_parada, numero_iteraciones,
           circunferencias_entrada)
