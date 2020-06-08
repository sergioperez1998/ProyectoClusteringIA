from codigo.funcionesAuxiliares import *
from codigo.circunferencia import Circunferencia
import random


# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
# 2. Repetir (hasta condición de parada)
# 2.1. actualizar grados de pertenencia de los puntos a las circunferencias
# 2.2. actualizar centros y radios
# 3. Asignar cada punto únicamente a su cluster de mayor grado de pertenencia,
# y devolver la información completa para cada cluster (centro, radio y lista de puntos asignados a él).

# 0. Leer datos
#datos_entrada = leer_datos('../data/entrada.csv')

# 1. Inicialización de circunferencias iniciales (centro y radio de cada una)
#tres_puntos = random.sample(datos_entrada, 3)
#circulo = encontrar_circulo(tres_puntos[0], tres_puntos[1], tres_puntos[2])
circulo = encontrar_circulo(Punto(13, 14), Punto(14, 10), Punto(8, 14))

#circunferencia = Circunferencia(circulo[0], circulo[1], [tres_puntos[0], tres_puntos[1], tres_puntos[2]])
circunferencia = Circunferencia(circulo[0], circulo[1], [Punto(13, 14), Punto(14, 10), Punto(8, 14)])
circunferencia2 = Circunferencia(Punto(7, 7), 6.87, [])

# 2. Repetir (hasta condición de parada)
circunferencias = [circunferencia, circunferencia2]
grado_pertenencia(Punto(5, 5), circunferencias)

